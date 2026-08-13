import asyncio
import inspect
import logging
import typing

from .. import events, utils, errors
from ..tl import types, functions
from .._updates import GapError
from ..helpers import get_running_loop
from ..version import __version__


if typing.TYPE_CHECKING:
    from .soroushclient import SoroushClient


Callback = typing.Callable[[typing.Any], typing.Any]

_WORKER_POOL_SIZE = 50

# Update types that should be dispatched to handlers
_UPDATABLE_TYPES = (
    types.UpdateNewMessage,
    types.UpdateNewChannelMessage,
    types.UpdateEditMessage,
    types.UpdateEditChannelMessage,
    types.UpdateDeleteMessages,
    types.UpdateDeleteChannelMessages,
    types.UpdateChatParticipantAdd,
    types.UpdateChatParticipantDelete,
    types.UpdateChannelParticipant,
    types.UpdateUserStatus,
    types.UpdateUserTyping,
    types.UpdateChatUserTyping,
    types.UpdateChannelUserTyping,
    types.UpdatePinnedChannelMessages,
    types.UpdatePinnedMessages,
)


class UpdateMethods:

    def add_event_handler(self: 'SoroushClient', callback, event):
        """
        Registers a callback to be called when a matching event occurs.

        Args:
            callback: The callable to invoke.
            event: An EventBuilder instance (e.g. events.NewMessage(...)).
        """
        if isinstance(event, type):
            event = event()
        self._event_builders.append((event, callback))

    def remove_event_handler(self: 'SoroushClient', callback, event=None):
        """
        Removes one or all registered event handler(s) for the given callback.
        """
        found = 0
        i = len(self._event_builders)
        while i:
            i -= 1
            ev, cb = self._event_builders[i]
            if cb == callback and (event is None or type(ev) == (type(event) if not isinstance(event, type) else event)):
                del self._event_builders[i]
                found += 1
        return found

    # region Public methods

    async def _run_until_disconnected(self: 'SoroushClient'):
        try:
            await self(functions.updates.GetStateRequest())

            self._start_worker_pool()

            print('Bot Started.')

            result = await self.disconnected

            if getattr(self, '_updates_error', None) is not None:
                raise self._updates_error

            return result
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print('Bot Start Failed !')
            self._log[__name__].exception('Failed to start bot')
        finally:
            await self.disconnect()

    def run_until_disconnected(self: 'SoroushClient'):
        if self.loop.is_running():
            return self._run_until_disconnected()
        try:
            return self.loop.run_until_complete(self._run_until_disconnected())
        except KeyboardInterrupt:
            pass
        finally:
            self.disconnect()

    # endregion

    # region Decorators

    def on_message(self: 'SoroushClient', filters=None):
        def decorator(func):
            self.add_event_handler(func, events.NewMessage(filters=filters))
            return func
        return decorator

    def on_group(self: 'SoroushClient', filters=None):
        def decorator(func):
            from ..filters import filters as f
            final_filters = f.group
            if filters:
                final_filters &= filters
            self.add_event_handler(func, events.NewMessage(filters=final_filters))
            return func
        return decorator

    def on_edited_message(self: 'SoroushClient', filters=None):
        def decorator(func):
            self.add_event_handler(func, events.MessageEdited(filters=filters))
            return func
        return decorator

    def on_channel(self: 'SoroushClient', filters=None):
        def decorator(func):
            from ..filters import filters as f
            final_filters = f.channel
            if filters:
                final_filters &= filters
            self.add_event_handler(func, events.NewMessage(filters=final_filters))
            return func
        return decorator

    def on_me(self: 'SoroushClient', filters=None):
        def decorator(func):
            from ..filters import filters as f
            final_filters = f.me
            if filters:
                final_filters &= filters
            self.add_event_handler(func, events.NewMessage(filters=final_filters))
            return func
        return decorator

    def on_deleted_messages(self: 'SoroushClient', filters=None):
        """
        Decorator to register a handler for deleted messages.

        Args:
            filters: Optional filters to apply to the event.

        Example:
            @client.on_deleted_messages()
            async def handler(client, event):
                for msg_id in event.deleted_ids:
                    print(f"Message {msg_id} deleted")
        """
        def decorator(func):
            self.add_event_handler(func, events.MessageDeleted(filters=filters))
            return func
        return decorator

    def on_chat_action(self: 'SoroushClient', filters=None):
        """
        Decorator to register a handler for chat actions
        (user joined, left, kicked, title/photo changed, pinned, etc.).

        Args:
            filters: Optional filters to apply to the event.

        Example:
            @client.on_chat_action()
            async def handler(client, event):
                if event.user_joined:
                    await event.reply("Welcome!")
        """
        def decorator(func):
            self.add_event_handler(func, events.ChatAction(filters=filters))
            return func
        return decorator

    def on_user_status(self: 'SoroushClient', filters=None):
        """
        Decorator to register a handler for user status changes
        (online/offline/typing).

        Args:
            filters: Optional filters to apply to the event.

        Example:
            @client.on_user_status()
            async def handler(client, event):
                if event.online:
                    print(f"User {event.user_id} is online")
        """
        def decorator(func):
            self.add_event_handler(func, events.UserUpdate(filters=filters))
            return func
        return decorator

    def on_raw_update(self: 'SoroushClient', types=None):
        """
        Decorator to register a handler for raw, unparsed updates.

        This is a fallback handler for advanced debugging. It receives
        the raw update dictionary/object directly.

        Args:
            types: Optional type or list of types to filter updates by.

        Example:
            @client.on_raw_update()
            async def handler(client, update):
                print(update)
        """
        def decorator(func):
            self.add_event_handler(func, events.Raw(types=types))
            return func
        return decorator

    def on_error(self: 'SoroushClient', exception_class):
        def decorator(func):
            if not hasattr(self, '_error_handlers'):
                self._error_handlers = {}
            self._error_handlers[exception_class] = func
            return func
        return decorator

    # endregion

    # region Private methods — Worker Pool

    def _start_worker_pool(self: 'SoroushClient'):
        """
        Spawns a pool of persistent background workers that continuously
        pull updates from the queue and execute matched event handlers.
        """
        self._worker_pool = [
            self.loop.create_task(self._worker_loop(i))
            for i in range(_WORKER_POOL_SIZE)
        ]

    async def _worker_loop(self: 'SoroushClient', worker_id: int):
        """
        Persistent worker coroutine. Pulls preprocessed updates from
        the queue, dispatches them, and signals task completion.
        Exceptions inside user handlers are caught and logged without
        crashing the worker.
        """
        while True:
            try:
                update = await self._update_queue.get()
                try:
                    await self._dispatch_update(update)
                except Exception as e:
                    self._log[__name__].exception(
                        'Unhandled exception in handler (worker %d)', worker_id)
                finally:
                    self._update_queue.task_done()
            except asyncio.CancelledError:
                break
            except Exception as e:
                self._log[__name__].exception(
                    'Fatal error in worker %d', worker_id)
                break

    async def _dispatch_update(self: 'SoroushClient', update):
        """
        Matches a preprocessed update against all registered event builders
        and executes the matched handler callbacks. Runs inside a worker.
        """
        if not self._mb_entity_cache.self_id:
            # Prevent 50 workers from calling get_me() concurrently
            if not getattr(self, '_fetching_me', False):
                try:
                    self._fetching_me = True
                    await self.get_me()
                except Exception:
                    pass
                finally:
                    self._fetching_me = False
            else:
                # Briefly wait for the other worker to finish fetching 'me'
                for _ in range(20):
                    if self._mb_entity_cache.self_id:
                        break
                    await asyncio.sleep(0.05)

        from ..events import (
            NewMessage, MessageEdited, MessageDeleted,
            ChatAction, UserUpdate, Raw
        )

        event = None
        if isinstance(update, (types.UpdateNewMessage, types.UpdateNewChannelMessage)):
            event = NewMessage.build(update, None, self._mb_entity_cache.self_id)
        elif isinstance(update, (types.UpdateEditMessage, types.UpdateEditChannelMessage)):
            event = MessageEdited.build(update, None, self._mb_entity_cache.self_id)
        elif isinstance(update, (types.UpdateDeleteMessages, types.UpdateDeleteChannelMessages)):
            event = MessageDeleted.build(update, None, self._mb_entity_cache.self_id)
        elif isinstance(update, (
            types.UpdateChatParticipantAdd,
            types.UpdateChatParticipantDelete,
            types.UpdateChannelParticipant,
            types.UpdatePinnedChannelMessages,
            types.UpdatePinnedMessages,
        )):
            event = ChatAction.build(update, None, self._mb_entity_cache.self_id)
        elif isinstance(update, (
            types.UpdateUserStatus,
            types.UpdateUserTyping,
            types.UpdateChatUserTyping,
            types.UpdateChannelUserTyping,
        )):
            event = UserUpdate.build(update, None, self._mb_entity_cache.self_id)
        elif isinstance(update, (types.UpdateNewMessage, types.UpdateNewChannelMessage)):
            # Check for service messages that are ChatActions
            msg = update.message
            if isinstance(msg, types.MessageService) and isinstance(msg.action, (
                types.MessageActionChatJoinedByLink,
                types.MessageActionChatAddUser,
                types.MessageActionChatDeleteUser,
                types.MessageActionChatCreate,
                types.MessageActionChannelCreate,
                types.MessageActionChatEditTitle,
                types.MessageActionChatEditPhoto,
                types.MessageActionChatDeletePhoto,
                types.MessageActionPinMessage,
                types.MessageActionGameScore,
            )):
                event = ChatAction.build(update, None, self._mb_entity_cache.self_id)
            else:
                event = NewMessage.build(update, None, self._mb_entity_cache.self_id)

        # For Raw handlers, always dispatch with the raw update
        raw_event = update

        if not event and not any(
            isinstance(ev, Raw) for ev, _ in self._event_builders
        ):
            return

        if event:
            event._set_client(self)

        for builder, callback in self._event_builders:
            # Handle Raw events specially: pass the raw update directly
            if isinstance(builder, Raw):
                if not builder.resolved:
                    await builder.resolve(self)

                if builder.filters:
                    if not await builder.filters(self, raw_event):
                        continue

                try:
                    await callback(self, raw_event)
                except Exception as e:
                    if hasattr(self, '_error_handlers'):
                        handled = False
                        for exc_class, handler in self._error_handlers.items():
                            if isinstance(e, exc_class):
                                await handler(e)
                                handled = True
                                break
                        if not handled:
                            self._log[__name__].exception('Unhandled exception in handler')
                    else:
                        self._log[__name__].exception('Unhandled exception in handler')
                continue

            if event is None:
                continue

            if not isinstance(event, builder.Event):
                continue

            if not builder.resolved:
                await builder.resolve(self)

            if builder.filters:
                if not await builder.filters(self, event):
                    continue

            try:
                await callback(self, event)
            except Exception as e:
                if hasattr(self, '_error_handlers'):
                    handled = False
                    for exc_class, handler in self._error_handlers.items():
                        if isinstance(e, exc_class):
                            await handler(e)
                            handled = True
                            break
                    if not handled:
                        self._log[__name__].exception('Unhandled exception in handler')
                else:
                    self._log[__name__].exception('Unhandled exception in handler')

    # endregion

    # region Private methods — Update Loop

    async def _update_loop(self: 'SoroushClient'):
        """
        Main update fetching loop. Fetches raw updates from the server
        or local queue, preprocesses them, and pushes them to the worker
        queue via put_nowait(). Does NOT execute any handlers directly.
        """
        self._updates_error = None
        try:
            while self.is_connected():
                get_diff = self._message_box.get_difference()
                if get_diff:
                    try:
                        diff = await self(get_diff)
                    except Exception as e:
                        self._log[__name__].debug('Failed to get difference: %s', e)
                        self._message_box.end_difference()
                        continue

                    updates, users, chats = self._message_box.apply_difference(
                        diff, self._mb_entity_cache)
                    _preprocess_updates = await self._preprocess_updates(
                        updates, users, chats)
                    for u in _preprocess_updates:
                        self._update_queue.put_nowait(u)
                    continue

                got_updates = []
                try:
                    got_updates.append(self._updates_queue.get_nowait())
                    while True:
                        got_updates.append(self._updates_queue.get_nowait())
                except asyncio.QueueEmpty:
                    pass

                if got_updates:
                    for update in got_updates:
                        processed = []
                        try:
                            users, chats = self._message_box.process_updates(
                                update, self._mb_entity_cache, processed)
                        except GapError:
                            continue

                        _preprocess_updates = await self._preprocess_updates(
                            processed, users, chats)
                        for u in _preprocess_updates:
                            self._update_queue.put_nowait(u)
                    continue

                # CRITICAL FIX: Safe deadline calculation and Anti-CPU-Lock
                deadline = self._message_box.check_deadlines()
                if deadline is None:
                    deadline_delay = None
                else:
                    deadline_delay = deadline - get_running_loop().time()

                if deadline_delay is None or deadline_delay > 0:
                    try:
                        if deadline_delay is None:
                            update = await self._updates_queue.get()
                        else:
                            update = await asyncio.wait_for(
                                self._updates_queue.get(), deadline_delay)
                    except asyncio.TimeoutError:
                        continue
                else:
                    # YIELD CONTROL: Prevent asyncio starvation loop!
                    await asyncio.sleep(0.01)
                    continue

                processed = []
                try:
                    users, chats = self._message_box.process_updates(
                        update, self._mb_entity_cache, processed)
                except GapError:
                    continue

                _preprocess_updates = await self._preprocess_updates(
                    processed, users, chats)
                for u in _preprocess_updates:
                    self._update_queue.put_nowait(u)

        except asyncio.CancelledError:
            pass
        except Exception as e:
            self._log[__name__].exception('Fatal error handling updates')
            self._updates_error = e
            await self.disconnect()

    async def _preprocess_updates(self, updates, users, chats):
        self._mb_entity_cache.extend(users, chats)
        entities = {utils.get_peer_id(x): x for x in (users + chats)}
        for u in updates:
            u._entities = entities
        return updates

    # endregion