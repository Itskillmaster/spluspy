<div align="center">

# SplusPy

**A modern async Python library for Soroush Plus**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Itskillmaster/spluspy/blob/main/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/spluspy)](https://pypi.org/project/spluspy/)
[![Python versions](https://img.shields.io/pypi/pyversions/spluspy)](https://pypi.org/project/spluspy/)
[![Downloads](https://img.shields.io/pypi/dm/spluspy)](https://pypi.org/project/spluspy/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)

[English](#-features) | [فارسی](#-ویژگی‌ها)

---

**SplusPy** is a modern, asynchronous Python library for interacting with [Soroush Plus](https://web.splus.ir) — both as a user account and a bot account.

Built from the ground up with clean architecture, it's designed to feel like [Telethon](https://github.com/LonamiWebs/Telethon) or [Pyrogram](https://github.com/pyrogram/pyrogram), but specifically for the Soroush Plus ecosystem.

**SplusPy** یک کتابخانه پایتون مدرن و ناهمگام (Asynchronous) برای تعامل با [سروش پلاس](https://web.splus.ir) است — هم به عنوان حساب کاربری و هم به عنوان حساب ربات.

این کتابخانه از صفر با معماری تمیز طراحی شده و الهام گرفته از [Telethon](https://github.com/LonamiWebs/Telethon) و [Pyrogram](https://github.com/pyrogram/pyrogram) است، اما مخصوص اکوسیستم سروش پلاس می‌باشد.

</div>

---

## English

### Features

| Feature | Description |
|---------|-------------|
| **No API Key Required** | Built-in Soroush Plus credentials |
| **Fully Asynchronous** | Built with Python's `asyncio` |
| **Sync Support** | Use without `async/await` via `spluspy.sync` |
| **Bot & User Support** | Both account types |
| **Event-Driven Handlers** | Powerful event system with decorators |
| **Filter System** | Composable filters (`&`, `\|`, `~`) |
| **Inline & Reply Buttons** | Interactive keyboards |
| **Conversation API** | For interactive bot flows |
| **FSM (Finite State Machine)** | Built-in state management for bots |
| **Plugin System** | Dynamic plugin loading |
| **Middleware** | Pre/post processing of updates |
| **Scheduler** | Built-in task scheduler |
| **Multiple Storage Backends** | Memory, SQLite, Redis, PostgreSQL |
| **Rate Limiting** | Token bucket algorithm with flood wait handling |
| **AFK Auto-Reply** | Smart auto-responder with per-chat rate limiting |
| **Chat Administration** | Ban, mute, pin, purge — high-level admin API |
| **Message Mirroring** | Real-time message cloning between chats |
| **Batch Operations** | Send, delete, forward multiple messages at once |
| **File Transfer with Progress** | Upload/download with progress tracking |
| **Professional Logging** | Structured, namespaced loggers |
| **Type Hints Everywhere** | Full type safety |
| **Clean Architecture** | SOLID principles, modular design |

### Requirements

- Python 3.10+
- No external API keys needed (built-in Soroush Plus credentials)

### Installation

```bash
pip install spluspy
```

For faster encryption:

```bash
pip install spluspy[speed]
```

With Redis backend:

```bash
pip install spluspy[redis]
```

With PostgreSQL backend:

```bash
pip install spluspy[postgres]
```

All optional dependencies:

```bash
pip install spluspy[all]
```

### Quick Start

#### Simplest Bot

```python
from spluspy import Client

bot = Client("my_session")

@bot.on_message()
async def handler(client, message):
    await message.reply("Hello!")

bot.run()
```

#### User Account

```python
from spluspy import Client

client = Client("session_name")

@client.on_message()
async def handler(client, message):
    await message.reply("Hey there!")

async def main():
    await client.start(phone="+98XXXXXXXXXX")
    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
```

#### Sync Usage (No Async/Await)

```python
from spluspy.sync import Client

bot = Client("session")

@bot.on_message()
def handler(client, message):
    message.reply("Hello!")

bot.run()
```

---

## Complete API Reference

---

### Client

The main entry point for all SplusPy operations. Manages authentication, event dispatching, middleware, plugins, and API interactions. Supports both bot mode (`bot_token`) and user mode (`phone`).

#### Constructor

```python
Client(
    session: Union[str, Session] = "spluspy",
    session_name: Optional[str] = None,
    *,
    session_string: Optional[str] = None,
    api_id: Optional[int] = None,
    api_hash: Optional[str] = None,
    bot_token: Optional[str] = None,
    phone: Optional[str] = None,
    proxy: Optional[dict[str, Any]] = None,
    flood_sleep_threshold: int = 60,
    max_retries: Optional[int] = None,
    request_timeout: float = 30.0,
    log_level: int = logging.CRITICAL,
    log_file: Optional[str] = None,
    log_dir: str = "logs",
    errors_only: bool = False,
) -> None
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `session` | `str \| Session` | `"spluspy"` | Session name or a `Session` object. Used to persist authentication data. |
| `session_name` | `str \| None` | `None` | Alternative name for the session file. Overrides `session` if provided. |
| `session_string` | `str \| None` | `None` | A portable base64 session string for deploying without files. |
| `api_id` | `int \| None` | `None` | Custom API ID. If `None`, uses built-in Soroush Plus credentials. |
| `api_hash` | `str \| None` | `None` | Custom API hash. If `None`, uses built-in Soroush Plus credentials. |
| `bot_token` | `str \| None` | `None` | Bot token for bot mode. If `None`, runs in user mode. |
| `phone` | `str \| None` | `None` | Phone number for user mode authentication. |
| `proxy` | `dict \| None` | `None` | Proxy configuration (e.g. `{"proxy_type": "socks5", "addr": "127.0.0.1", "port": 1080}`). |
| `flood_sleep_threshold` | `int` | `60` | Seconds to auto-sleep on `FloodWait` errors before raising. |
| `max_retries` | `int \| None` | `None` | Maximum retry attempts for failed requests. `None` = infinite. |
| `request_timeout` | `float` | `30.0` | Timeout in seconds for API requests. |
| `log_level` | `int` | `CRITICAL` | Logging level (e.g. `logging.INFO`, `logging.DEBUG`). |
| `log_file` | `str \| None` | `None` | Path to log file. `None` = console only. |
| `log_dir` | `str` | `"logs"` | Directory for log files. |
| `errors_only` | `bool` | `False` | If `True`, only logs errors (suppresses info/debug). |

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `session_name` | `str` | Returns the session name. |
| `is_connected` | `bool` | Whether the client is currently connected to the server. |
| `middleware` | `MiddlewareManager` | Access the middleware manager to add/remove middleware. |
| `plugins` | `PluginManager` | Access the plugin manager to load/unload plugins. |
| `scheduler` | `Scheduler` | Access the built-in task scheduler. |

#### Event Registration Methods

##### `on(event, **kwargs) -> Callable`

Register a handler for any event type. The `event` parameter accepts an `EventBuilder` or an `Event` subclass. Optional `priority` kwarg controls execution order (lower = first).

```python
@bot.on(NewMessage(), priority=HandlerPriority.HIGH)
async def handler(client, event):
    pass
```

##### `on_message(*message_filters, **kwargs) -> Callable`

Register a handler that fires on new messages. Multiple filter arguments are ANDed together. The handler receives `(client, message)`.

| Parameter | Type | Description |
|-----------|------|-------------|
| `*message_filters` | `Filter` | One or more filters. All must pass for the handler to fire. |
| `priority` | `int` | Execution priority. Default: `HandlerPriority.NORMAL` (50). |

```python
@bot.on_message(filters.text & filters.private)
async def handler(client, message):
    await message.reply("Hello!")
```

##### `on_edited_message(*message_filters, **kwargs) -> Callable`

Register a handler for edited messages. Same filter/priority API as `on_message`.

##### `on_callback_query(**kwargs) -> Callable`

Register a handler for inline button callback queries. Handler receives `(client, callback_query)`.

> **Note:** Not supported on Soroush+ user sessions. Exists for API compatibility.

##### `on_inline_query(**kwargs) -> Callable`

Register a handler for inline queries. Handler receives `(client, inline_query)`.

> **Note:** Not supported on Soroush+ user sessions. Exists for API compatibility.

##### `on_chat_action(**kwargs) -> Callable`

Register a handler for chat actions (joins, leaves, pins, etc.). Handler receives `(client, action_event)`.

##### `on_user_update(**kwargs) -> Callable`

Register a handler for user status changes (online/offline/typing). Handler receives `(client, user_update)`.

##### `on_message_deleted(**kwargs) -> Callable`

Register a handler for deleted messages. Handler receives `(client, deleted_event)`.

##### `on_message_read(**kwargs) -> Callable`

Register a handler for read receipts. Handler receives `(client, read_event)`.

##### `on_error(*exception_types, priority=HandlerPriority.LOW) -> Callable`

Register a global error handler. If no exception types are specified, catches all errors. The handler receives an `ErrorEvent` object.

```python
@bot.on_error(FloodWait, Unauthorized)
async def error_handler(client, event):
    print(f"Error: {event.exception}")
```

#### Connection Lifecycle

##### `async connect() -> None`

Connect to the Soroush Plus server. Attempts adapter-based connection first, falls back to built-in MTProto. Must be called before sending/receiving messages in user mode.

##### `async disconnect() -> None`

Disconnect from the server. Stops the scheduler, closes middleware and sessions.

##### `async start() -> None`

Start the client with interactive prompts for phone/password/code authentication. Automatically connects and handles the full auth flow.

##### `async stop() -> None`

Alias for `disconnect()`. Stops the client.

##### `async run_until_disconnected() -> None`

Run the event loop until the client is disconnected. Handles transient disconnections gracefully with automatic reconnection.

##### `run() -> None`

**Blocking** entry point. Connects, runs until disconnected, then cleans up. Tries `uvloop` for better performance. This is the simplest way to run a bot:

```python
bot = Client("session")
bot.run()  # Blocks forever
```

#### Message Sending

##### `async send_message(chat_id, text=None, *, reply_to=None, parse_mode=None, link_preview=True, **kwargs) -> Message`

Send a text message to a chat.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `chat_id` | `int` | (required) | Target chat/user ID. |
| `text` | `str \| None` | `None` | Message text. |
| `reply_to` | `int \| None` | `None` | Message ID to reply to. |
| `parse_mode` | `str \| None` | `None` | `"html"`, `"markdown"`, or `None` for raw text. |
| `link_preview` | `bool` | `True` | Whether to show link previews. |

**Returns:** `Message` — the sent message object.

##### `async edit_message(message, *, text=None, parse_mode=None, delay=0, **kwargs) -> Message`

Edit a previously sent message's text. If `delay` is set, waits that many seconds before editing (non-blocking).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | `Message \| int` | (required) | Message object or message ID. |
| `text` | `str \| None` | `None` | New text content. |
| `delay` | `int` | `0` | Seconds to wait before editing. |

##### `async delete_messages(*messages, **kwargs) -> bool`

Delete one or more messages. Accepts `Message` objects or integer IDs.

**Returns:** `True` on success.

##### `async delete_message(chat_id, message_id, *, delay=0) -> bool`

Delete a single message with an optional delay before deletion.

##### `async forward_messages(chat_id, *messages) -> Message`

Forward one or more messages to another chat. Returns a placeholder `Message`.

##### `async send_photo(chat_id, photo, *, caption=None, **kwargs) -> Message`

Send a photo. `photo` can be a file path (`str`), `bytes`, or a file-like object.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `chat_id` | `int` | (required) | Target chat/user ID. |
| `photo` | `str \| bytes \| IO` | (required) | Photo file path, bytes, or file-like object. |
| `caption` | `str \| None` | `None` | Caption text for the photo. |

##### `async send_video(chat_id, video, *, caption=None, duration=0, width=0, height=0, supports_streaming=True, thumb=None, force_document=False, progress_callback=None, reply_to=None, **kwargs) -> Message`

Send a video. Duration, width, and height are auto-detected if left at `0`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `video` | `str \| bytes \| IO` | (required) | Video file. |
| `caption` | `str \| None` | `None` | Video caption. |
| `duration` | `int` | `0` | Duration in seconds (auto-detected if 0). |
| `width` | `int` | `0` | Width in pixels (auto-detected if 0). |
| `height` | `int` | `0` | Height in pixels (auto-detected if 0). |
| `supports_streaming` | `bool` | `True` | Whether the video supports streaming. |
| `progress_callback` | `Callable \| None` | `None` | Callback for upload progress: `fn(current, total)`. |

##### `async send_voice(chat_id, voice, *, caption=None, duration=0, progress_callback=None, reply_to=None, **kwargs) -> Message`

Send a voice note (audio message).

##### `async send_document(chat_id, document, *, caption=None, file_name=None, force_document=True, progress_callback=None, reply_to=None, **kwargs) -> Message`

Send a document/file. `force_document=True` ensures the file is sent as a document, not auto-detected.

##### `async send_audio(chat_id, audio, *, caption=None, duration=0, performer=None, title=None, progress_callback=None, reply_to=None, **kwargs) -> Message`

Send an audio file with optional metadata (performer, title).

##### `async send_animation(chat_id, animation, *, caption=None, duration=0, width=0, height=0, thumb=None, progress_callback=None, reply_to=None, **kwargs) -> Message`

Send an animation (GIF).

##### `async send_location(chat_id, lat, lon, *, reply_to=None) -> Message`

Send a geographic location.

| Parameter | Type | Description |
|-----------|------|-------------|
| `lat` | `float` | Latitude (-90 to 90). |
| `lon` | `float` | Longitude (-180 to 180). |

##### `async send_contact(chat_id, phone, first_name, last_name="", *, vcard="", reply_to=None) -> Message`

Send a contact card.

##### `async send_poll(chat_id, question, options, *, correct_option=None, explanation=None, is_anonymous=True, allows_multiple_answers=False) -> Message`

Send a poll to a chat.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `question` | `str` | (required) | Poll question. |
| `options` | `list[str]` | (required) | List of answer options (2-10). |
| `correct_option` | `int \| None` | `None` | Index of the correct answer (for quizzes). |
| `explanation` | `str \| None` | `None` | Explanation shown after voting. |
| `is_anonymous` | `bool` | `True` | Whether the poll is anonymous. |
| `allows_multiple_answers` | `bool` | `False` | Whether users can select multiple options. |

##### `async send_dice(chat_id, emoji="🎲", *, reply_to=None) -> Message`

Send a dice animation. Supported emojis: `🎲` (dice), `🎯` (darts), `🏀` (basketball), `⚽` (football), `🎳` (bowling), `🎰` (slot machine).

##### `async send_reaction(chat_id, message, emoji) -> bool`

React to a message with an emoji.

**Returns:** `True` on success.

##### `async send_sticker(chat_id, sticker, *, emoji=None, sticker_set=None, progress_callback=None, reply_to=None, **kwargs) -> Message`

Send a sticker.

##### `async send_video_note(chat_id, video, *, caption=None, duration=0, width=0, height=0, progress_callback=None, reply_to=None, **kwargs) -> Message`

Send a round video note.

##### `async send_chat_action(chat_id, action="typing") -> bool`

Send a typing indicator or upload progress status.

Supported actions: `"typing"`, `"upload_photo"`, `"record_video"`, `"upload_video"`, `"record_audio"`, `"upload_audio"`, `"upload_document"`, `"find_location"`, `"record_voice"`, `"upload_voice"`, `"choose_sticker"`.

#### Chat Management

##### `async ban_user(chat_id, user_id) -> bool`

Ban a user from a chat. The user cannot rejoin unless unbanned.

##### `async unban_user(chat_id, user_id) -> bool`

Unban a previously banned user, allowing them to rejoin the chat.

##### `async mute_user(chat_id, user_id) -> bool`

Mute a user (restrict them from sending any messages in the chat).

##### `async unmute_user(chat_id, user_id) -> bool`

Unmute a user, restoring their ability to send messages.

##### `async safe_ban_user(chat_id, user_id) -> bool`

Ban a user, catching permission errors gracefully. Never raises — returns `False` on failure.

##### `async safe_send_message(chat_id, text=None, *, reply_to=None, parse_mode=None, link_preview=True, **kwargs) -> Message`

Send a message, catching permission errors gracefully. Never raises — returns a fallback `Message` on failure.

##### `async unblock_chat_member(chat_id, user_id) -> bool`

Remove a user from the account's block list.

##### `async get_chat_blocked_users(chat_id) -> list[dict]`

Fetch all blocked users in a chat. Returns a list of dicts with `user_id` and `date` keys.

##### `async join_chat(chat_id) -> Any`

Join a chat by ID, username, or invite link. Returns a `Chat` object.

**Raises typed exceptions:** `InvalidInviteLinkError`, `InviteLinkExpiredError`, `ChatFullError`, `ChatDeactivatedError`, `MembershipRequiredError`, `FloodWait`, `ChatNotFound`, `JoinChatError`.

##### `async leave_chat(chat_id) -> bool`

Leave a chat. Auto-detects whether it's a channel or basic group.

##### `async leave_group(chat_id) -> bool`

Leave a basic group specifically.

##### `async leave_channel(chat_id) -> bool`

Leave a channel or supergroup specifically.

##### `async get_all_groups() -> list[dict]`

Get all groups and channels the user is a member of. Returns list of dicts with `id`, `title`, `type` keys.

##### `async leave_all_groups(exclude_ids=None) -> dict`

Leave all basic groups. Returns a dict with `success`, `failed`, `skipped` counts and `details`.

##### `async leave_all_channels(exclude_ids=None) -> dict`

Leave all channels. Returns a dict with `success`, `failed`, `skipped` counts and `details`.

##### `async leave_all(exclude_ids=None) -> dict`

Leave all groups and channels at once. Returns summary dict.

##### `async delete_all_private(*, revoke=False, exclude_ids=None, delay=1.0, on_progress=None) -> dict`

Delete all private chat dialogs. Returns summary dict with counts and details.

##### `async pin_chat_message(chat_id, message_id, notify=True) -> bool`

Pin a message by ID. If `notify=True`, all members are notified.

##### `async unpin_chat_message(chat_id, message_id) -> bool`

Unpin a specific message by ID.

##### `async pin_message(chat_id, message, *, notify=False) -> bool`

Pin a message. Accepts either a `Message` object or an integer message ID.

##### `async unpin_message(chat_id, message) -> bool`

Unpin a message. Accepts either a `Message` object or an integer message ID.

##### `async unpin_all_messages(chat_id) -> bool`

Unpin all pinned messages in a chat at once.

##### `async mark_read(chat_id, message=None) -> bool`

Mark a specific message (or all messages in a chat) as read.

#### Info Retrieval

##### `async get_me() -> Any`

Get the currently authenticated user. Returns a `User` object or `None`.

##### `async get_chat(chat_id) -> Any`

Get a chat entity by ID or username.

##### `async get_full_chat(chat_id) -> Optional[Chat]`

Get full chat info including title and `member_count`. Supports numeric IDs, usernames, and invite link hashes.

##### `async is_chat_member(chat_id) -> bool`

Check if the current user is a member of the specified chat.

##### `async get_user(user_id) -> Optional[User]`

Get full user info by ID or `@username`. Returns a `User` with bio, status, and all other fields.

##### `async get_bio(user_id) -> Optional[str]`

Get a user's biography/about text.

##### `async get_first_name(user_id) -> Optional[str]`

Get a user's first name.

##### `async get_last_name(user_id) -> Optional[str]`

Get a user's last name.

##### `async get_full_name(user_id) -> Optional[str]`

Get a user's full name (first + last name combined).

##### `async get_username(user_id) -> Optional[str]`

Get a user's username without the `@` prefix.

##### `async get_user_link(user_id) -> Optional[str]`

Get a `t.me/` profile link for the user.

##### `async get_description(chat_id) -> Optional[str]`

Get a group/channel description (about text).

##### `async get_group_link(chat_id) -> Optional[str]`

Get the `t.me/` invite link for a group or channel.

##### `async get_group_id(username) -> Optional[int]`

Resolve a `@username` to a chat/channel integer ID.

##### `async get_chat_info(chat_id) -> Optional[dict]`

Get comprehensive chat info as a dictionary with keys: `id`, `title`, `username`, `link`, `description`, `member_count`, `type`.

##### `async get_user_info(user_id) -> Optional[dict]`

Get comprehensive user info as a dictionary with keys: `id`, `first_name`, `last_name`, `full_name`, `username`, `link`, `bio`, `phone`, `is_bot`, `is_premium`, `status`.

##### `async get_messages(chat_id, *, limit=100, **kwargs) -> list[Message]`

Get messages from a chat. Returns list of `Message` objects, newest first.

##### `async iter_messages(chat_id, *, limit=1000, offset_id=0, search=None, batch_size=100) -> AsyncGenerator[Message, None]`

Async generator yielding messages in memory-efficient batches. Ideal for processing large histories without loading everything into memory.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `chat_id` | `int \| str` | (required) | Chat to iterate messages from. |
| `limit` | `int` | `1000` | Maximum number of messages to yield. |
| `offset_id` | `int` | `0` | Start from this message ID (newer messages). |
| `search` | `str \| None` | `None` | Search query to filter messages. |
| `batch_size` | `int` | `100` | Number of messages to fetch per API call. |

##### `async search_messages(chat_id, query, *, limit=100) -> list[Message]`

Search for messages in a chat by text query.

##### `async get_history(chat_id, *, limit=100) -> list[Message]`

Alias for `get_messages()`.

##### `async get_members(chat_id, *, limit=100) -> list[ChatMember]`

Alias for `get_chat_members()`.

##### `async iter_chat_members(chat_id, *, limit=200, batch_size=100) -> AsyncGenerator[ChatMember, None]`

Async generator yielding chat members in batches.

##### `async iter_members(chat_id, *, limit=200, batch_size=100) -> AsyncGenerator[ChatMember, None]`

Alias for `iter_chat_members()`.

##### `async iter_dialogs(*, limit=500, batch_size=100) -> AsyncGenerator[Chat, None]`

Async generator yielding dialogs (chats) in batches.

##### `async get_contacts() -> list[User]`

Get the account's contact list as `User` objects.

##### `async resolve_username(username) -> int`

Resolve a username to a numeric ID. Returns `0` if not found.

##### `async resolve_peer(peer) -> Any`

Resolve a peer identifier to an MTProto `InputPeer` object. Supports integer IDs, `@username`, and phone numbers.

#### Profile Management

##### `async update_profile(first_name=None, last_name=None, about=None, bio=None) -> bool`

Update the current user's profile fields. Returns `True` on success.

##### `async set_profile_photo(photo) -> bool`

Upload and set a new profile photo. `photo` can be a file path or `bytes`.

##### `async delete_profile_photo(photo_id=None) -> bool`

Delete a profile photo. Pass `None` to delete the most recent one.

##### `async set_username(username) -> bool`

Change the current user's username. Pass an empty string `""` to remove it.

##### `async set_offline(offline=True) -> bool`

Set the user's online/offline appearance. `True` = appear offline.

#### Low-level

##### `async invoke(*args, **kwargs) -> Any`

Invoke a raw MTProto API method. This is a low-level escape hatch for API methods not covered by the high-level interface.

##### `async export_session_string() -> str`

Export the current session as a portable base64 string. Useful for deploying without session files.

#### Conversation

##### `conversation(chat_id, *, timeout=30.0, exclusive=True) -> Conversation`

Create an interactive conversation context manager for request/response style messaging. See [Conversation API](#conversation-api) below.

---

### Conversation API

A context-managed conversational flow for interactive bot dialogs. Used with `async with client.conversation(peer) as conv:`.

#### Constructor

```python
Conversation(
    client: Client,
    peer: Union[int, str],
    timeout: Optional[float] = 30.0,
    exclusive: bool = True,
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `client` | `Client` | (required) | The SplusPy client instance. |
| `peer` | `int \| str` | (required) | Chat ID or username to converse with. |
| `timeout` | `float` | `30.0` | Default timeout in seconds for waiting responses. |
| `exclusive` | `bool` | `True` | If `True`, only captures messages from the target peer. |

#### Methods

##### `async send_message(text, **kwargs) -> Message`

Send a message in this conversation.

##### `async get_response(timeout=None) -> Message`

Wait for the next incoming message from the conversation peer. Raises `ConversationTimeoutError` if no message arrives within the timeout.

##### `async wait_response(timeout=None) -> Message`

Alias for `get_response()`.

##### `async send_and_wait(text, *, timeout=None, **kwargs) -> Message`

Send a message and wait for a reply in a single call. Convenience method combining `send_message` + `get_response`.

##### `empty() -> bool`

Returns `True` if the internal message queue is empty.

##### `clear() -> None`

Discard any unread messages in the internal queue.

#### Usage Example

```python
async with client.conversation(chat_id, timeout=30) as conv:
    await conv.send_message("What is your name?")
    response = await conv.get_response()
    await conv.send_and_wait(f"Nice to meet you, {response.text}!")
```

---

### Client Chat Management Mixin Methods

Additional chat management methods available on the `Client` instance.

##### `async get_chat_members(chat_id, limit=200) -> list[Any]`

Get a list of members in a channel/megagroup using raw MTProto. Returns `User` objects.

##### `async restrict_user(chat_id, user_id, send_messages=False, until_date=0, *, send_media=False, send_stickers=False, send_gifs=False, send_inline=False, embed_links=False, send_polls=False, change_info=False, invite_users=False, pin_messages=False, manage_topics=False) -> bool`

Restrict a user in a megagroup/channel with fine-grained permission control.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `send_messages` | `bool` | `False` | Allow sending messages. |
| `send_media` | `bool` | `False` | Allow sending media. |
| `send_stickers` | `bool` | `False` | Allow sending stickers. |
| `send_gifs` | `bool` | `False` | Allow sending GIFs. |
| `send_inline` | `bool` | `False` | Allow using inline bots. |
| `embed_links` | `bool` | `False` | Allow embedding links. |
| `send_polls` | `bool` | `False` | Allow sending polls. |
| `change_info` | `bool` | `False` | Allow changing chat info. |
| `invite_users` | `bool` | `False` | Allow inviting users. |
| `pin_messages` | `bool` | `False` | Allow pinning messages. |
| `manage_topics` | `bool` | `False` | Allow managing topics. |
| `until_date` | `int` | `0` | Restriction expiry timestamp. `0` = permanent. |

##### `async promote_member(chat_id, user_id, is_admin=True, privileges=None, *, rank="") -> bool`

Promote or demote a user in a megagroup/channel. `privileges` is a dict of permission booleans. `rank` sets the admin rank title.

##### `async set_chat_permissions(chat_id, send_messages=None, send_media=None, send_stickers=None, send_gifs=None, send_polls=None, embed_links=None, invite_users=None, change_info=None, pin_messages=None) -> bool`

Set the default chat permissions for all non-admin members. `True` = allowed, `False` = restricted, `None` = no change.

##### `async set_chat_title(chat_id, title) -> bool`

Change the title of a channel or supergroup.

##### `async set_chat_about(chat_id, about) -> bool`

Change the about/description text of a chat (max 70 characters).

##### `async set_chat_photo(chat_id, file_path) -> bool`

Upload and set a new photo for a channel or supergroup.

##### `async start_group_call(chat_id, title=None) -> bool`

Start a group call (voice chat) in a supergroup. Requires admin rights with `manage_call` permission.

##### `async stop_group_call(chat_id) -> bool`

Stop (discard) an active group call in a supergroup.

---

### Client Media Mixin Methods

Low-level media operations using raw MTProto.

| Constant | Value | Description |
|----------|-------|-------------|
| `UPLOAD_CHUNK_SIZE` | `524288` (512 KB) | Default upload chunk size. |
| `DOWNLOAD_CHUNK_SIZE` | `1048576` (1 MB) | Default download chunk size. |
| `MAX_SMALL_FILE_SIZE` | `10485760` (10 MB) | Max size for small file uploads. |

##### `async send_file(chat_id, file_path, caption="", progress_callback=None, *, force_document=False, force_photo=False, thumb=None, attributes=None, voice_note=False, video_note=False, background=False, clear_draft=False, noforwards=False, schedule_date=None, reply_to=None, duration=0, width=0, height=0, performer=None, title=None, supports_streaming=True, sticker_emoji=None, sticker_set=None) -> Any`

Send a file using raw MTProto upload with chunked transfer. Auto-detects photo vs document based on file type.

##### `async send_location_media(chat_id, lat, lon, *, reply_to=None) -> Any`

Send a geographic location using raw MTProto.

##### `async send_contact_media(chat_id, phone, first_name, last_name="", vcard="", *, reply_to=None) -> Any`

Send a contact card using raw MTProto.

##### `async send_dice_media(chat_id, emoticon="🎲", *, reply_to=None) -> Any`

Send a dice animation using raw MTProto.

##### `async download_media(message, file_name=None, progress_callback=None, *, dc_id=None) -> Optional[str]`

Download a file from a message. Returns the path to the downloaded file, or `None` on failure.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `message` | `Message \| Any` | (required) | Message containing the media. |
| `file_name` | `str \| None` | `None` | Custom file name for the download. |
| `progress_callback` | `Callable \| None` | `None` | Progress callback: `fn(current, total)`. |
| `dc_id` | `int \| None` | `None` | Data center ID override. |

---

### Message Model

The `Message` dataclass represents a received or sent message.

#### Attributes

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `id` | `int` | `0` | Unique message identifier. |
| `text` | `str` | `""` | Message text or media caption. |
| `date` | `datetime \| None` | `None` | Message timestamp. |
| `chat_id` | `int` | `0` | Chat this message belongs to. |
| `chat` | `Chat \| None` | `None` | Resolved `Chat` object. |
| `sender_id` | `int \| None` | `None` | Sender user ID. |
| `sender` | `User \| None` | `None` | Resolved `User` object. |
| `media` | `Media \| None` | `None` | Attached media object. |
| `media_type` | `MessageMediaType` | `NONE` | Kind of media (`PHOTO`, `VIDEO`, etc.). |
| `reply_to` | `int \| None` | `None` | ID of the message being replied to. |
| `reply_to_sender_id` | `int \| None` | `None` | Sender ID from the reply header. |
| `reply_to_message` | `Message \| None` | `None` | Full replied-to message object. |
| `entities` | `list[MessageEntity]` | `[]` | Formatting entities (bold, links, etc.). |
| `forward_origin` | `dict \| None` | `None` | Forward origin information. |
| `views` | `int` | `0` | View count for channel messages. |
| `edit_date` | `datetime \| None` | `None` | Last edit timestamp. |
| `is_group` | `bool` | `False` | Whether from a group chat. |
| `is_channel` | `bool` | `False` | Whether from a channel. |
| `is_private` | `bool` | `False` | Whether from a private chat. |
| `new_chat_members` | `list` | `[]` | Users who joined (service messages). |
| `left_chat_member` | `User \| None` | `None` | User who left (service messages). |
| `service_type` | `str \| None` | `None` | Type of service event. |

#### Properties

| Property | Return Type | Description |
|----------|-------------|-------------|
| `message_id` | `int` | Alias for `id`. |
| `is_forwarded` | `bool` | Whether message was forwarded. |
| `is_reply` | `bool` | Whether message is a reply to another message. |
| `is_media` | `bool` | Whether message contains any media attachment. |

#### Methods

##### `async reply(text=None, *, parse_mode=None, link_preview=True, buttons=None, file=None, **kwargs) -> Message`

Reply to this message (sends with reply header).

##### `async edit(text=None, *, parse_mode=None, link_preview=True, buttons=None, delay=0) -> Message`

Edit this message's text. If `delay > 0`, waits before editing.

##### `async delete(*, delay=0) -> bool`

Delete this message. If `delay > 0`, waits before deleting.

##### `async forward(chat_id) -> Message`

Forward this message to another chat (keeps the forward header).

##### `async copy(chat_id) -> Message`

Copy this message to another chat (no forward header).

##### `async get_reply_message() -> Optional[Message]`

Fetch the full message that this message replies to.

##### `async pin(notify=True) -> bool`

Pin this message in its chat.

##### `async unpin() -> bool`

Unpin this message from its chat.

##### `async react(emoji) -> bool`

React to this message with an emoji.

##### `async mark_read() -> bool`

Mark this message as read.

##### `async unblock_sender() -> bool`

Unblock the sender of this message.

##### `async download(file_path=None, *, progress=None) -> Optional[str]`

Download the media attached to this message. Returns the local file path.

Aliases: `download_media()`, `download_file()`, `save()`.

##### `async reply_photo(photo, caption=None, **kwargs) -> Message`

Reply with a photo.

##### `async reply_video(video, caption=None, **kwargs) -> Message`

Reply with a video.

##### `async reply_voice(voice, caption=None, **kwargs) -> Message`

Reply with a voice note.

##### `async reply_document(document, caption=None, **kwargs) -> Message`

Reply with a document.

##### `async reply_audio(audio, caption=None, *, duration=0, performer=None, title=None, **kwargs) -> Message`

Reply with an audio file.

##### `async reply_animation(animation, caption=None, **kwargs) -> Message`

Reply with a GIF/animation.

##### `async reply_sticker(sticker, **kwargs) -> Message`

Reply with a sticker.

##### `async reply_location(lat, lon) -> Message`

Reply with a geographic location.

##### `async reply_contact(phone, first_name, last_name="", *, vcard="") -> Message`

Reply with a contact card.

##### `async reply_poll(question, options, *, is_anonymous=True, allows_multiple_answers=False) -> Message`

Reply with a poll.

##### `async reply_dice(emoji="🎲") -> Message`

Reply with a dice animation.

##### `async reply_video_note(video, *, caption=None, duration=0, **kwargs) -> Message`

Reply with a round video note.

---

### User Model

Represents a Soroush Plus user.

#### Attributes

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `id` | `int` | (required) | Unique user identifier. |
| `first_name` | `str` | `""` | First name. |
| `last_name` | `str` | `""` | Last name. |
| `username` | `str \| None` | `None` | Username without `@`. |
| `phone` | `str \| None` | `None` | Phone number. |
| `bio` | `str \| None` | `None` | Biography/about text. |
| `is_bot` | `bool` | `False` | Whether this is a bot account. |
| `is_self` | `bool` | `False` | Whether this is the current authenticated user. |
| `is_premium` | `bool` | `False` | Whether user has premium subscription. |
| `status` | `UserStatus` | `EMPTY` | Online status. |

#### Properties

| Property | Return Type | Description |
|----------|-------------|-------------|
| `full_name` | `str` | Combined first + last name. |
| `mention` | `str` | `@username` if available, otherwise full name. |
| `link` | `str \| None` | `https://t.me/username` profile link. `None` if no username. |

---

### Chat Model

Represents a Soroush Plus chat (private, group, supergroup, or channel).

#### Attributes

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `id` | `int` | (required) | Unique chat identifier. |
| `title` | `str` | `""` | Chat title. |
| `type` | `ChatType` | `PRIVATE` | Type of chat. |
| `username` | `str \| None` | `None` | Public username. |
| `description` | `str \| None` | `None` | Chat description. |
| `member_count` | `int` | `0` | Number of members. |

#### Properties

| Property | Return Type | Description |
|----------|-------------|-------------|
| `is_private` | `bool` | Whether it's a private (1-to-1) chat. |
| `is_group` | `bool` | Whether it's a group or supergroup. |
| `is_supergroup` | `bool` | Whether it's a supergroup. |
| `is_channel` | `bool` | Whether it's a channel. |
| `link` | `str \| None` | Deep link to the chat. |
| `display_name` | `str` | Human-readable name (title or username). |

#### Subclasses

- `Channel(Chat)` — Pre-set type to `CHANNEL`.
- `Group(Chat)` — Pre-set type to `GROUP` or `SUPERGROUP`.

---

### ChatMember Model

Represents a member of a chat.

#### Attributes

| Field | Type | Description |
|-------|------|-------------|
| `user` | `User` | The user object. |
| `status` | `ChatMemberStatus` | Membership status. |
| `joined_date` | `datetime \| None` | When they joined. |
| `invited_by` | `int \| None` | Who invited them. |
| `restricted_until` | `int \| None` | Restriction expiry timestamp. |

#### Properties

| Property | Return Type | Description |
|----------|-------------|-------------|
| `user_id` | `int` | Shortcut to `user.id`. |
| `is_creator` | `bool` | Whether this is the chat creator/owner. |
| `is_admin` | `bool` | Whether they have admin rights (includes creator). |
| `is_banned` | `bool` | Whether they are banned. |
| `is_left` | `bool` | Whether they have left the chat. |

---

### Button Factory

Static factory methods for creating keyboard buttons. All methods are `@staticmethod`.

#### Inline Buttons

##### `Button.inline(text, callback_data) -> InlineKeyboardButton`

Create an inline keyboard button with callback data.

| Parameter | Type | Description |
|-----------|------|-------------|
| `text` | `str` | Button display text. |
| `callback_data` | `bytes` | Data sent back when button is pressed. |

##### `Button.url(text, url) -> InlineKeyboardButton`

Create an inline button that opens a URL.

##### `Button.switch_inline(text, query="") -> InlineKeyboardButton`

Create an inline button that switches to inline mode with a pre-filled query.

##### `Button.switch_inline_current(text, query="") -> InlineKeyboardButton`

Same as `switch_inline` but keeps the user in the current chat.

#### Reply Buttons

##### `Button.text(text, resize=True, one_time=False) -> ReplyMarkup`

Create a single-button reply keyboard.

#### Special Buttons

##### `Button.request_location(text="Share Location") -> KeyboardButton`

Create a button that requests the user's location.

##### `Button.request_phone(text="Share Phone") -> KeyboardButton`

Create a button that requests the user's phone number.

##### `Button.clear() -> ReplyMarkup`

Create a special reply markup that removes/hides the current keyboard.

#### Keyboard Builders

##### `Button.build_inline(*rows) -> ReplyMarkup`

Build an inline keyboard from rows of buttons.

```python
keyboard = Button.build_inline(
    [Button.inline("Option 1", b"opt1"), Button.inline("Option 2", b"opt2")],
    [Button.url("Visit", "https://example.com")]
)
```

##### `Button.build_reply(*rows, resize=True, one_time=False) -> ReplyMarkup`

Build a reply keyboard from rows of buttons.

```python
kb = Button.build_reply(
    [Button.text("Menu"), Button.text("Settings")],
    [Button.text("Help")]
)
```

---

### CallbackQuery Model

Represents a callback query from an inline button press.

#### Attributes

| Field | Type | Description |
|-------|------|-------------|
| `id` | `str` | Unique callback query identifier. |
| `data` | `bytes \| None` | Raw callback data bytes. |
| `chat_instance` | `str` | Chat instance identifier. |
| `from_user` | `User` | The user who pressed the button. |
| `message` | `Message \| None` | The message containing the button. |

#### Properties

| Property | Return Type | Description |
|----------|-------------|-------------|
| `text` | `str \| None` | Decoded callback data as UTF-8 string. |

#### Methods

##### `async answer(text=None, show_alert=False, cache_time=0) -> bool`

Answer the callback query. Shows a popup notification if `show_alert=True`.

##### `async edit_message(text=None, reply_markup=None) -> bool`

Edit the message that contains the inline keyboard.

---

### InlineQuery Model

Represents an inline query from a user.

#### Attributes

| Field | Type | Description |
|-------|------|-------------|
| `id` | `str` | Unique inline query identifier. |
| `query` | `str` | The search query text. |
| `offset` | `str` | Pagination offset. |
| `chat_type` | `str \| None` | Chat type context. |
| `from_user` | `User` | The user who sent the query. |

#### Methods

##### `async answer(results, cache_time=300, is_personal=True, next_offset=None) -> bool`

Answer the inline query with a list of result dictionaries.

---

### Events

#### Event (Base Class)

Abstract base for all events. All events support propagation control.

##### `stop_propagation() -> None`

Stop the event from being passed to subsequent handlers with lower priority.

##### `is_propagation_stopped` (property) -> `bool`

Returns `True` if propagation was stopped by a handler.

#### HandlerPriority

Controls the order in which handlers are executed.

| Value | Int | Description |
|-------|-----|-------------|
| `FIRST` | `0` | Executes first, before all others. |
| `HIGH` | `10` | Executes early. |
| `NORMAL` | `50` | Default priority. |
| `LOW` | `100` | Executes late. |
| `LAST` | `200` | Executes last, after all others. |

#### NewMessage Event

Fired when a new message is received.

##### Fields

| Field | Type | Description |
|-------|------|-------------|
| `message` | `Message` | The incoming message. |
| `pattern_match` | `Pattern.Match \| None` | Regex match result (if `filters.regex` was used). |

##### Properties

`text`, `chat_id`, `sender_id`, `is_private`, `is_group`, `is_channel`, `raw_text`, `sender`, `chat`, `reply_to`, `reply_to_sender_id`, `reply_to_message`, `media`, `photo`, `video`, `voice`, `document`, `sticker`, `forward_origin`, `new_chat_members`, `left_chat_member`, `service_type`.

##### Methods

```python
async def reply(self, text: str, **kwargs) -> Message
async def respond(self, text: str, **kwargs) -> Message  # Send without reply header
async def delete(self, **kwargs) -> bool
async def edit(self, text: str, **kwargs) -> Message
async def forward(self, chat_id: int) -> Message
async def pin(self, notify=False) -> bool
async def react(self, emoji: str) -> bool
async def mark_read(self) -> bool
async def download(self, file_path=None) -> Optional[str]
```

#### ErrorEvent

Fired when a handler raises an exception.

| Field | Type | Description |
|-------|------|-------------|
| `exception` | `Exception` | The raised exception. |
| `handler` | `Callable \| None` | The handler that failed. |
| `update` | `Any` | The original update. |

| Property | Type | Description |
|----------|------|-------------|
| `message` | `str` | Error message string. |
| `type` | `str` | Exception class name. |

#### ChatAction Event

Fired on chat actions (joins, leaves, pins).

| Property | Type | Description |
|----------|------|-------------|
| `is_join` | `bool` | Whether a user joined. |
| `is_leave` | `bool` | Whether a user left. |
| `is_pin` | `bool` | Whether a message was pinned. |
| `user_name` | `str` | Display name of the user. |

#### UserUpdate Event

Fired when a user's online status changes.

| Property | Type | Description |
|----------|------|-------------|
| `is_online` | `bool` | Whether the user came online. |
| `is_offline` | `bool` | Whether the user went offline. |

#### MessageDeleted Event

Fired when messages are deleted. Fields: `deleted_ids` (list of ints), `chat_id`.

#### MessageRead Event

Fired when messages are read. Fields: `read_ids` (list of ints), `chat_id`, `max_id`.

#### Album Event

Fired when a group of media messages is received (e.g., multiple photos sent at once).

| Field | Type | Description |
|-------|------|-------------|
| `messages` | `list[Message]` | All messages in the album. |
| `chat_id` | `int` | The chat where the album was received. |
| `group_id` | `str` | Album group identifier. |

| Property | Type | Description |
|----------||-------------|
| `total` | `int` | Number of messages in the album. |

---

### Filters

Filters are composable predicates that determine which messages trigger a handler. Use `&` (AND), `|` (OR), and `~` (NOT) to combine them.

#### Chat-Type Filters

| Filter | Matches |
|--------|---------|
| `filters.private` | Messages from private (1-to-1) chats. |
| `filters.group` | Messages from group or supergroup chats. |
| `filters.channel` | Messages from channels. |

#### Content-Type Filters

| Filter | Matches |
|--------|---------|
| `filters.text` | Messages with non-empty text. |
| `filters.photo` | Messages containing a photo. |
| `filters.video` | Messages containing a video. |
| `filters.audio` | Messages containing audio. |
| `filters.voice` | Messages containing a voice note. |
| `filters.document` | Messages containing a document. |
| `filters.sticker` | Messages containing a sticker. |
| `filters.animation` | Messages containing a GIF. |
| `filters.contact` | Messages containing a contact card. |
| `filters.location` | Messages containing a location. |
| `filters.poll` | Messages containing a poll. |
| `filters.video_note` | Messages containing a video note. |
| `filters.dice` | Messages containing a dice animation. |
| `filters.media` | Messages with any media attachment. |

#### State Filters

| Filter | Matches |
|--------|---------|
| `filters.reply` | Messages that are replies to other messages. |
| `filters.forwarded` | Forwarded messages. |
| `filters.me` | Messages sent by the current user. |
| `filters.bot` | Messages sent by bots. |
| `filters.outgoing` | Outgoing (outbound) messages. |
| `filters.incoming` | Incoming (inbound) messages. |
| `filters.mentioned` | Messages where the current user is mentioned. |
| `filters.new_chat_members` | Service messages: users joined. |
| `filters.left_chat_member` | Service messages: user left/was removed. |
| `filters.service` | Any system/service message. |

#### Factory Functions

##### `filters.command(*commands, prefixes=None) -> Command`

Create a command filter. Matches messages starting with `/` or `!` followed by the given command names.

```python
@bot.on_message(filters.command("start", "help"))
async def handler(client, message):
    # Matches /start, /help, !start, !help
    pass
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `*commands` | `str` | (required) | Command names to match. |
| `prefixes` | `list[str] \| None` | `None` | Custom prefixes. Default: `["/", "!"]`. |

##### `filters.regex(pattern, flags=0) -> Regex`

Create a regex filter. The match object is stored on `message.pattern_match`.

```python
@bot.on_message(filters.regex(r"(\d+)"))
async def handler(client, message):
    number = message.pattern_match.group(1)
```

##### `filters.user(*user_ids) -> UserFilter`

Create a user ID filter. Matches messages from specific users.

##### `filters.chat(*chat_ids) -> ChatFilter`

Create a chat ID filter. Matches messages from specific chats.

##### `filters.text_contains(substring, case_sensitive=True) -> TextContains`

Filter messages that contain a specific substring.

##### `filters.text_startswith(prefix) -> TextStartsWith`

Filter messages that start with a specific prefix.

##### `filters.text_endswith(suffix) -> TextEndsWith`

Filter messages that end with a specific suffix.

##### `filters.length(min=0, max=999999) -> Length`

Filter messages by text length.

##### `filters.from_callable(func) -> Filter`

Wrap any callable as a filter. If the argument is already a `Filter`, returns it as-is.

#### Composition Examples

```python
# AND: private AND text
@bot.on_message(filters.private & filters.text)

# OR: photo OR video
@bot.on_message(filters.photo | filters.video)

# NOT: NOT outgoing
@bot.on_message(~filters.outgoing)

# Complex: (private OR group) AND text AND NOT bot
@bot.on_message((filters.private | filters.group) & filters.text & ~filters.bot)
```

---

### FSM (Finite State Machine)

#### State

Represents a single FSM state. Auto-named via the `__set_name__` descriptor protocol when assigned as a class attribute.

```python
State(name: Optional[str] = None)
```

| Property | Type | Description |
|----------|------|-------------|
| `name` | `str` | The state name (auto-derived from class attribute name). |

#### StateTransition

Represents a state transition with an optional async guard function.

```python
StateTransition(target: State, guard: Optional[Callable] = None)
```

##### `async check(update) -> bool`

Check whether this transition is allowed. If no guard is set, always returns `True`.

#### FSMContext

Per-user context for reading/writing FSM state and data.

```python
FSMContext(storage: Storage, user_id: int, prefix: str = "fsm")
```

| Property | Type | Description |
|----------|------|-------------|
| `key` | `str` | Full storage key including prefix and user ID. |
| `state_key` | `str` | Key for storing the current state. |
| `data_key` | `str` | Key for storing user data. |
| `user_id` | `int` | The user this context belongs to. |

##### `async get_state() -> Optional[State]`

Get the current state for this user. Returns `None` if no state is set.

##### `async set_state(state) -> None`

Set the current state for this user. Pass `None` to clear the state.

##### `async get_data() -> dict[str, Any]`

Get all stored data for this user in the current state.

##### `async set_data(**kwargs) -> None`

Update the stored data with the provided key-value pairs.

##### `async get(key, default=None) -> Any`

Get a single data value by key.

##### `async set(key, value) -> None`

Set a single data value.

##### `async reset() -> None`

Clear both the state and all data for this user.

##### `async finish() -> None`

Alias for `reset()`. Clears state and data.

#### StateMachine

Factory for `FSMContext` with decorator-based state routing.

```python
StateMachine(storage: Storage)
```

##### `def state(state, *, on_enter=None, on_leave=None) -> Callable`

Decorator that registers a handler for a specific state.

```python
@sm.state(Form.name)
async def handle_name(ctx, message):
    await ctx.set(name=message.text)
    return StateTransition(to=Form.age)
```

##### `def on_enter(state) -> Callable`

Decorator that registers a callback when entering a state.

##### `def on_leave(state) -> Callable`

Decorator that registers a callback when leaving a state.

##### `def fallback() -> Callable`

Decorator that registers a handler for unmatched states (no registered handler for the current state).

##### `def context(user_id, prefix="fsm") -> FSMContext`

Create an `FSMContext` for a specific user.

##### `async handle(update, user_id) -> bool`

Route an update to the appropriate state handler. Returns `True` if a handler was found and executed.

#### Usage Example

```python
from spluspy.fsm import State, StateMachine, StateTransition
from spluspy.storage import SQLiteStorage

storage = SQLiteStorage("fsm.db")
sm = StateMachine(storage)

class Registration:
    name = State()
    age = State()
    complete = State()

@sm.state(Registration.name)
async def handle_name(ctx, message):
    await ctx.set(name=message.text)
    return StateTransition(to=Registration.age)

@sm.state(Registration.age)
async def handle_age(ctx, message):
    await ctx.set(age=message.text)
    return StateTransition(to=Registration.complete)

@sm.state(Registration.complete)
async def handle_complete(ctx, message):
    data = await ctx.get()
    await message.reply(f"Done: {data}")
    await ctx.finish()
```

---

### Storage Backends

#### Storage (Abstract Base)

All storage backends implement this interface.

```python
async def get(key: str) -> Optional[Any]
async def set(key: str, value: Any, ttl: Optional[int] = None) -> None
async def delete(key: str) -> bool
async def exists(key: str) -> bool
async def clear() -> None
```

#### MemoryStorage

In-memory non-persistent storage with optional TTL support. Data is lost when the process exits.

```python
MemoryStorage()
```

**Use case:** Development, testing, short-lived sessions.

#### SQLiteStorage

Persistent SQLite-backed storage. Automatically creates the database and table on `start()`.

```python
SQLiteStorage(db_path: str = "spluspy_storage.db")
```

| Method | Description |
|--------|-------------|
| `async start()` | Open the database and create the table if needed. |
| `async close()` | Close the database connection. |

**Use case:** Single-user bots, local persistence.

#### RedisStorage

Persistent Redis-backed storage. Requires `pip install spluspy[redis]`.

```python
RedisStorage(
    url: str = "redis://localhost:6379/0",
    prefix: str = "spluspy:",
    default_ttl: Optional[int] = None,
)
```

| Extra Method | Description |
|--------------|-------------|
| `async increment(key, amount=1) -> int` | Atomically increment a counter. |
| `async set_hash(key, mapping, ttl=None)` | Store a dict as a Redis hash. |
| `async get_hash(key) -> dict` | Retrieve a Redis hash as a dict. |

**Use case:** Multi-process deployments, shared state.

#### PostgresStorage

Persistent PostgreSQL-backed storage. Requires `pip install spluspy[postgres]`.

```python
PostgresStorage(
    dsn: str = "postgresql://localhost/spluspy",
    table: str = "spluspy_kv",
    prefix: str = "",
)
```

| Extra Method | Description |
|--------------|-------------|
| `async cleanup_expired() -> int` | Remove expired entries. Returns count removed. |
| `async keys(pattern="*") -> list[str]` | List all keys matching a pattern. |

**Use case:** Enterprise deployments, existing PostgreSQL infrastructure.

#### Factory Function

```python
def get_storage(backend: str = "memory", **kwargs) -> Storage
```

Create a storage by name: `"memory"`, `"sqlite"`, `"redis"`, `"postgres"`.

#### EntityCache (Storage)

SQLite-backed peer resolution cache for caching user/chat entities.

```python
EntityCache(storage: Optional[Storage] = None)
```

| Method | Description |
|--------|-------------|
| `async start()` | Initialize the cache. |
| `async get(entity_id) -> Optional[dict]` | Get entity by ID. |
| `async get_by_username(username) -> Optional[dict]` | Get entity by username. |
| `async get_by_phone(phone) -> Optional[dict]` | Get entity by phone. |
| `async put(entity_id, access_hash, entity_type="user", *, username=None, phone=None)` | Store an entity. |
| `async put_entity(entity)` | Store an entity from an object. |
| `async put_many(entities) -> int` | Store multiple entities. Returns count stored. |
| `async remove(entity_id) -> bool` | Remove an entity by ID. |
| `async clear()` | Remove all cached entities. |
| `async count() -> int` | Get the number of cached entities. |

---

### Middleware

#### Middleware (Abstract Base)

All middleware must implement `on_update`. The handler chain is executed in FIFO order.

```python
class Middleware(ABC):
    @abstractmethod
    async def on_update(self, update: Any, handler: Handler) -> Any

    async def on_startup(self) -> None   # Called when client starts
    async def on_shutdown(self) -> None  # Called when client stops
```

#### MiddlewareManager

Manages an ordered chain of middleware. Errors in one middleware are isolated and don't break the chain.

```python
MiddlewareManager()
```

| Method | Description |
|--------|-------------|
| `add(mw: Middleware)` | Add middleware to the end of the chain. |
| `remove(mw: Middleware)` | Remove middleware from the chain. |
| `async execute(update, final_handler) -> Any` | Execute the middleware chain. |
| `async startup()` | Notify all middleware of client startup. |
| `async shutdown()` | Notify all middleware of client shutdown. |

#### RateLimitMiddleware

Rate limiting middleware for automatic flood wait handling.

```python
RateLimitMiddleware(
    rate: float = 1.0,
    capacity: float = 1.0,
    flood_sleep_threshold: int = 60,
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `rate` | `float` | `1.0` | Token refill rate (tokens per second). |
| `capacity` | `float` | `1.0` | Maximum burst capacity. |
| `flood_sleep_threshold` | `int` | `60` | Max seconds to sleep on flood wait. |

| Method | Description |
|--------|-------------|
| `async on_update(update, handler) -> Any` | Process update through rate limiter. |
| `handle_flood_wait(method, seconds)` | Register a flood wait event. |
| `get_stats() -> dict` | Get rate limiter statistics. |

#### Usage Example

```python
from spluspy.middleware import Middleware

class LoggingMiddleware(Middleware):
    async def on_update(self, update, handler):
        print(f"Update: {update}")
        result = await handler(update)
        print("Handler completed")
        return result

bot.middleware.add(LoggingMiddleware())
```

---

### Utils

#### LRUCache

Thread-safe LRU cache with optional TTL (time-to-live) for automatic expiration.

```python
LRUCache(max_size: int = 1024, default_ttl: Optional[float] = None)
```

| Method | Description |
|--------|-------------|
| `async get(key) -> Optional[V]` | Get a value by key. Returns `None` if not found or expired. |
| `async set(key, value, ttl=None)` | Set a key-value pair. Optional per-entry TTL override. |
| `async delete(key) -> bool` | Delete a key. Returns `True` if the key existed. |
| `async exists(key) -> bool` | Check if a key exists and is not expired. |
| `async clear()` | Remove all entries. |
| `async size() -> int` | Get the current number of entries. |
| `get_stats() -> dict` | Returns `size`, `max_size`, `hits`, `misses`, `hit_rate`. |

```python
cache = LRUCache(max_size=1000, ttl=300)  # 5-minute TTL
await cache.set("key", "value")
value = await cache.get("key")
stats = cache.get_stats()  # {'hits': 42, 'misses': 3, 'hit_rate': 0.933, ...}
```

#### RateLimiter

Multi-endpoint rate limiter using the token bucket algorithm with flood wait handling.

```python
RateLimiter(default_rate: float = 1.0, default_capacity: float = 1.0, flood_sleep_threshold: int = 60)
```

| Method | Description |
|--------|-------------|
| `async acquire(method="default")` | Wait until a token is available for the given method. |
| `register_flood_wait(method, seconds)` | Register a flood wait for the method (prevents requests until the wait expires). |
| `limit(method="default", rate=None, capacity=None) -> Callable` | Decorator that rate-limits a function. |
| `get_wait_time(method="default") -> float` | Get remaining wait time for the method (0 = ready). |
| `clear_flood_wait(method)` | Clear the flood wait state for a method. |

#### TokenBucket

Low-level token bucket implementation.

```python
TokenBucket(rate: float = 1.0, capacity: float = 1.0)
```

| Method | Description |
|--------|-------------|
| `async acquire(tokens=1.0, blocking=True) -> bool` | Acquire tokens. If `blocking=True`, waits until available. Returns `True` on success. |

#### ChatLockManager

Per-chat granular locking to eliminate global lock contention in concurrent operations.

```python
ChatLockManager()
```

| Method | Description |
|--------|-------------|
| `acquire(key: int)` | Acquire a lock for a specific chat (async context manager). |
| `release(key: int)` | Release the lock for a chat. |
| `is_locked(key: int) -> bool` | Check if a chat is currently locked. |
| `locked_count() -> int` | Number of currently locked chats. |
| `pending_count() -> int` | Number of pending lock requests. |

#### Helper Functions

```python
def generate_random_id() -> int
# Generate a random 64-bit integer ID.

def timestamp_to_datetime(ts: Optional[int]) -> Optional[datetime]
# Convert a Unix timestamp to a datetime object.

def datetime_to_timestamp(dt: Optional[Union[datetime, date]]) -> Optional[int]
# Convert a datetime/date to a Unix timestamp.

def sanitize_filename(name: str) -> str
# Remove or replace unsafe characters from a filename.

def parse_mode(mode: Optional[str]) -> Optional[str]
# Normalize a parse mode string.

def chunk_list(items: list, size: int) -> list[list]
# Split a list into chunks of the given size.

def truncate(text: str, max_length: int = 4096) -> str
# Truncate text to a maximum length, adding "..." if truncated.
```

#### Batch Operations

```python
async def batch_send(client, chat_id, messages, *, delay=0.1, parse_mode=None) -> list[Message]
# Send multiple text messages sequentially with a delay between each.

async def batch_delete(client, chat_id, messages, *, batch_size=100) -> bool
# Delete multiple messages in batches.

async def batch_forward(client, target_chat, source_chat, messages, *, batch_size=100, delay=0.1) -> list[Message]
# Forward multiple messages in batches.

async def batch_get_messages(client, chat_id, message_ids, *, batch_size=100) -> list[Message]
# Fetch multiple messages by ID in batches.
```

#### File Transfer

```python
class TransferProgress:
    total: int          # Total file size in bytes
    transferred: int    # Bytes transferred so far
    speed: float        # Transfer speed in bytes/sec
    elapsed: float      # Elapsed time in seconds
    eta: float          # Estimated time remaining in seconds
    percent -> float    # Completion percentage (0-100)

class ProgressTracker:
    ProgressTracker(callback=None, update_interval=0.1)
    def update(self, chunk_size: int) -> None  # Called after each chunk
    def finish(self) -> None                    # Called when transfer completes
```

```python
# Upload with progress
tracker = ProgressTracker(on_progress=lambda p: print(f"{p.percent}%"))
await bot.send_document(chat_id, "large_file.zip", progress=tracker)

# Download with progress
await message.download(progress=tracker)
```

#### TargetResolver

Resolves message targets from various sources (reply, username, ID, etc.).

```python
TargetResolver(client: Client)
```

| Method | Description |
|--------|-------------|
| `async resolve(message, *, args=None) -> TargetResolution` | Resolve a target from a message context. |

```python
@dataclass
class TargetResolution:
    user_id: Optional[int]      # Resolved user ID
    message_id: Optional[int]   # Resolved message ID
    source: str                 # Resolution source: "reply", "username", "id", etc.
    display_name: Optional[str] # Human-readable name
```

```python
def resolve_reply_sender(message: Message) -> Optional[int]
# Synchronously extract the sender ID from a reply header.
```

#### Logger Utilities

```python
def setup_logging(level="INFO", log_file=None, log_dir="logs", max_bytes=10*1024*1024,
                  backup_count=5, use_color=True, console_output=True,
                  reconnect_only=False, errors_only=False) -> None
# Configure the logging system.

def get_logger(name=None, level=None) -> logging.Logger
# Get a named logger instance.

def set_level(level: Union[str, int]) -> None
# Change the global log level.

def log() -> logging.Logger
# Get the default root logger.

def log_event(logger, event: str, **data) -> None
# Log a structured event.

def log_request(logger, method: str, **params) -> None
# Log an API request.

def log_response(logger, method: str, status="OK", **data) -> None
# Log an API response.

def log_error(logger, error: Exception, context="") -> None
# Log an error with context.

def log_user_action(logger, action: str, user_id: int, chat_id=0, target_id=0, detail="") -> None
# Log a user action.

def log_security(logger, event: str, user_id: int, chat_id=0, reason="") -> None
# Log a security-related event.

def log_performance(logger, operation: str, duration_ms: float, **extra) -> None
# Log a performance measurement.
```

#### Version Check

```python
async def check_for_update() -> Optional[str]
# Check PyPI for a newer version. Returns version string or None.

def print_update_notice(new_version: str) -> None
# Print a formatted update notice to the console.

async def check_and_notify() -> None
# Check and print update notice if available. Call at startup.
```

---

### AfkManager

Smart auto-responder for AFK (Away From Keyboard) mode with per-chat rate limiting.

#### Constructor

```python
AfkManager(
    client: Client,
    message: str = "I'm currently AFK. I'll reply when I'm back.",
    *,
    cooldown: float = 60.0,
    max_replies: Optional[int] = 10,
    only_private: bool = False,
    only_mentions: bool = False,
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `client` | `Client` | (required) | The SplusPy client instance. |
| `message` | `str` | auto-reply text | Default AFK response message. |
| `cooldown` | `float` | `60.0` | Minimum seconds between replies to the same user. |
| `max_replies` | `int \| None` | `10` | Maximum total auto-replies per AFK session. `None` = unlimited. |
| `only_private` | `bool` | `False` | If `True`, only auto-reply in private chats. |
| `only_mentions` | `bool` | `False` | If `True`, only auto-reply when mentioned. |

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `is_afk` | `bool` | Whether AFK mode is currently active. |
| `afk_reason` | `str` | The reason for being AFK. |
| `afk_since` | `float \| None` | Unix timestamp when AFK mode started. |
| `total_replies` | `int` | Total number of auto-replies sent during this AFK session. |

#### Methods

##### `set_afk(enabled, *, reason="", message=None) -> None`

Enable or disable AFK mode.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `enabled` | `bool` | (required) | `True` to activate AFK, `False` to deactivate. |
| `reason` | `str` | `""` | Reason for being AFK (shown in the auto-reply). |
| `message` | `str \| None` | `None` | Override the default AFK message for this session. |

##### `async handle(message) -> bool`

Process an incoming message while AFK. Handles rate limiting and auto-reply. Returns `True` if a reply was sent.

##### `get_stats() -> dict`

Returns a dictionary with keys: `is_afk`, `afk_reason`, `afk_since`, `total_replies`, `active_chats`, `cooldown`, `max_replies`.

#### Usage Example

```python
from spluspy import Client, filters
from spluspy.afk import AfkManager

bot = Client("my_account")
afk = AfkManager(bot, message="I'm currently AFK. Back soon!")

@bot.on_message(filters.command("afk"))
async def set_afk(client, message):
    afk.set_afk(True, reason="Lunch break")
    await message.reply("I'm now AFK!")

@bot.on_message(filters.command("back"))
async def unset_afk(client, message):
    afk.set_afk(False)
    await message.reply(f"Back! Sent {afk.total_replies} auto-replies.")

@bot.on_message(filters.private & filters.incoming)
async def auto_reply(client, message):
    if afk.is_afk:
        await afk.handle(message)
```

---

### ChatAdmin

High-level chat administration API with batch operations and admin logging.

#### Constructor

```python
ChatAdmin(client: Client)
```

#### Methods

##### `async ban_user(chat_id, user_id, *, delete_messages=False) -> bool`

Ban a user from a chat. Optionally delete their recent messages.

##### `async unban_user(chat_id, user_id) -> bool`

Unban a user, allowing them to rejoin.

##### `async mute_user(chat_id, user_id, *, duration=None) -> bool`

Mute a user. `duration` in seconds; `None` = permanent.

##### `async unmute_user(chat_id, user_id) -> bool`

Unmute a user.

##### `async pin_chat_message(chat_id, message_id, notify=True) -> bool`

Pin a message by ID.

##### `async unpin_chat_message(chat_id, message_id) -> bool`

Unpin a message by ID.

##### `async pin_message(chat_id, message, *, notify=False) -> bool`

Pin a message (accepts `Message` object or int).

##### `async unpin_message(chat_id, message) -> bool`

Unpin a message (accepts `Message` object or int).

##### `async unpin_all(chat_id) -> bool`

Unpin all pinned messages in a chat.

##### `async purge_messages(chat_id, *, limit=100, before=None, after=None) -> int`

Delete a batch of messages. Returns the count of deleted messages.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `chat_id` | `int` | (required) | Target chat. |
| `limit` | `int` | `100` | Maximum messages to delete. |
| `before` | `int \| None` | `None` | Only delete messages with ID less than this. |
| `after` | `int \| None` | `None` | Only delete messages with ID greater than this. |

##### `async get_admin_log(chat_id, *, limit=100) -> list[dict]`

Get admin event log. Returns list of dicts with `id`, `date`, `user_id`, `action` keys.

##### `async bulk_action(chat_id, action, user_ids, *, delay=0.5, **kwargs) -> dict[int, bool]`

Perform bulk ban/unban/mute/unmute. Returns a dict mapping `user_id -> success`.

| Parameter | Type | Description |
|-----------|------|-------------|
| `action` | `str` | One of: `"ban"`, `"unban"`, `"mute"`, `"unmute"`. |
| `user_ids` | `list[int]` | List of user IDs to action. |
| `delay` | `float` | Delay between each action (to avoid flood). |

---

### MessageMirror

Real-time message cloning between chats.

#### Constructor

```python
MessageMirror(client: Client)
```

#### Methods

##### `add_route(source, targets, *, filter_func=None, strip_forward=True, strip_sender=False, add_prefix=None) -> None`

Add a complete mirroring route from a source chat to one or more target chats.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `source` | `int` | (required) | Source chat ID to mirror from. |
| `targets` | `list[int]` | (required) | Target chat IDs to mirror to. |
| `filter_func` | `Callable \| None` | `None` | Optional filter function: `fn(message) -> bool`. |
| `strip_forward` | `bool` | `True` | Remove forward headers from mirrored messages. |
| `strip_sender` | `bool` | `False` | Remove sender info from mirrored messages. |
| `add_prefix` | `str \| None` | `None` | Add a text prefix to mirrored messages. |

##### `add_source(source) -> None`

Add a source chat for mirroring.

##### `add_target(target, *, source=None) -> None`

Add a target chat. If `source` is `None`, targets the most recently added source.

##### `remove_route(source) -> None`

Remove a mirroring route by source chat ID.

##### `async start() -> None`

Start the mirroring engine. Begins listening for new messages.

##### `async stop() -> None`

Stop the mirroring engine.

##### `get_stats() -> dict`

Returns: `active` (bool), `routes` (int), `total_mirrored` (int), `sources` (list of ints).

#### Usage Example

```python
from spluspy.mirror import MessageMirror

mirror = MessageMirror(bot)

mirror.add_route(
    source=-1001234567890,
    targets=[-1009876543210, -1001112223334],
    strip_forward=True,
    strip_sender=False,
    add_prefix="[Mirror]"
)

await mirror.start()
```

---

### Scheduler

#### Scheduler (Low-level)

Manages scheduled and recurring tasks.

```python
Scheduler()
```

| Property | Type | Description |
|----------|------|-------------|
| `running` | `bool` | Whether the scheduler is running. |

| Method | Description |
|--------|-------------|
| `add(name, callback, *, interval=None, delay=0.0, max_runs=None) -> ScheduledTask` | Schedule a task. |
| `remove(name) -> bool` | Remove a task by name. |
| `get(name) -> Optional[ScheduledTask]` | Get a task by name. |
| `async start()` | Start the scheduler loop. |
| `async stop()` | Stop the scheduler loop. |

#### MessageScheduler

High-level message scheduling for bots.

```python
MessageScheduler(client: Client)
```

| Property | Type | Description |
|----------|------|-------------|
| `pending_count` | `int` | Number of pending scheduled tasks. |

| Method | Description |
|--------|-------------|
| `async start()` | Start the scheduler. |
| `async stop()` | Stop the scheduler. |
| `schedule_message(chat_id, text, *, delay=None, when=None, name=None) -> ScheduledTask` | Schedule a single message. |
| `schedule_interval(chat_id, text, *, interval, name=None, max_runs=None) -> ScheduledTask` | Schedule a recurring message. |
| `schedule_callback(name, callback, *, delay=None, interval=None, max_runs=None) -> ScheduledTask` | Schedule a custom callback. |
| `cancel(name) -> bool` | Cancel a scheduled task by name. |

#### Usage Example

```python
from spluspy.scheduler.scheduler import MessageScheduler

scheduler = MessageScheduler(bot)

# Send a message every hour
scheduler.schedule_interval("hourly_greeting", chat_id, "Hello!", interval=3600)

# Send a message after a delay (5 minutes)
scheduler.schedule_once("reminder", chat_id, "Don't forget!", delay=300)

# Cancel a scheduled task
scheduler.cancel("hourly_greeting")
```

---

### Error Hierarchy

All errors inherit from `SplusPyError(Exception)`.

```
SplusPyError
├── SoroushPlusAPIError(message, code=0)
│   ├── RPCError(message, code=0)
│   │   ├── FloodWait(seconds, message="")      # Has .seconds attribute
│   │   ├── Unauthorized(message, code=0)
│   │   ├── Forbidden(message, code=0)
│   │   ├── BadRequest(message, code=0)
│   │   │   ├── ChatNotFound(message, code=0)
│   │   │   ├── UserNotFound(message, code=0)
│   │   │   └── MessageNotFound(message, code=0)
│   │   └── ...
│   ├── SessionExpiredError(message)
│   └── SessionError(message)
├── AuthError(message)
├── ValidationError(message)
├── TimeoutError(message)
├── ConnectionError(message)
├── PluginError(message)
├── FSMError(message)
├── StorageError(message)
├── JoinChatError(message, link="")
│   ├── InvalidInviteLinkError(link, reason="...")
│   ├── InviteLinkExpiredError(link="", reason="...")
│   ├── ChatFullError(chat_id="", limit=0)
│   ├── ChatDeactivatedError(chat_id="")
│   └── MembershipRequiredError(chat_id="", reason="...")
└── FloodWaitError(message)   # From rate limiter
```

#### Error Handling Example

```python
from spluspy.errors import FloodWait, Unauthorized, BadRequest

@bot.on_message()
async def safe_handler(client, message):
    try:
        await message.reply("Hello!")
    except FloodWait as e:
        await asyncio.sleep(e.seconds)  # Wait the required time
    except Unauthorized:
        await message.reply("Not authorized!")
    except BadRequest as e:
        print(f"Bad request: {e}")
```

#### Global Error Handler

```python
from spluspy.events import ErrorHandlerBuilder

error_handler = ErrorHandlerBuilder()
error_handler.on(FloodWait)(lambda e: print(f"Flood wait: {e.seconds}s"))
error_handler.on(Unauthorized)(lambda e: print("Unauthorized"))

bot.on_error(error_handler.build())
```

---

### Plugin System

#### Plugin

Represents a loaded plugin.

```python
Plugin(name: str, module: Any, enabled: bool = True)
```

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | Plugin name (derived from module filename). |
| `module` | `Any` | The loaded Python module. |
| `enabled` | `bool` | Whether the plugin is enabled. |

#### PluginManager

Discovers, loads, and manages plugins.

```python
PluginManager(client: Client)
```

| Property | Type | Description |
|----------|------|-------------|
| `plugins` | `dict[str, Plugin]` | Mapping of loaded plugins by name. |

| Method | Description |
|--------|-------------|
| `load(path) -> list[Plugin]` | Load all plugins from a directory or single module file. |
| `unload(name) -> bool` | Unload a plugin by name. Returns `True` if unloaded. |
| `reload(name) -> Optional[Plugin]` | Reload a plugin. Returns the reloaded `Plugin` or `None`. |

#### Plugin Structure

Plugins are Python modules that define a `register(client)` function:

```python
# plugins/hello.py
def register(client):
    @client.on_message(filters.command("hello"))
    async def hello_handler(client, message):
        await message.reply("Hello from plugin!")
```

```python
# main.py
from spluspy import Client

bot = Client("session")
bot.plugins.load("plugins")  # Load all plugins from the "plugins" directory
bot.run()
```

---

### Sync Wrapper

The `spluspy.sync` module provides a synchronous wrapper around the async `Client`. Every async method is wrapped so it can be called without `await`.

```python
from spluspy.sync import Client

bot = Client("session")

@bot.on_message()
def handler(client, message):
    # No async/await needed!
    message.reply("Hello!")

bot.run()
```

The sync `Client` has the same constructor and all the same methods as the async `Client`, but without `async/await`:

```python
# Lifecycle
bot.start()
bot.stop()
bot.connect()
bot.disconnect()
bot.run()

# Messages (no await!)
bot.send_message(chat_id, "Hello!")
bot.edit_message(message, text="New text")
bot.delete_messages(msg1, msg2)

# All other methods work the same way
bot.get_me()
bot.get_messages(chat_id)
bot.ban_user(chat_id, user_id)
```

---

### Enums

```python
class ChatType(str, Enum):
    PRIVATE = "private"
    GROUP = "group"
    SUPERGROUP = "supergroup"
    CHANNEL = "channel"

class MessageMediaType(str, Enum):
    NONE = "none"
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"
    VOICE = "voice"
    VIDEO_NOTE = "video_note"
    STICKER = "sticker"
    ANIMATION = "animation"
    CONTACT = "contact"
    LOCATION = "location"
    POLL = "poll"
    DICE = "dice"

class ParseMode(str, Enum):
    NONE = "none"
    MARKDOWN = "markdown"
    MARKDOWN_V2 = "markdown_v2"
    HTML = "html"

class UserStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    LAST_SEEN = "last_seen"
    RECENTLY = "recently"
    LAST_WEEK = "last_week"
    LAST_MONTH = "last_month"
    LONG_AGO = "long_ago"
    EMPTY = "empty"

class ChatMemberStatus(IntEnum):
    CREATOR = 4
    ADMIN = 3
    MEMBER = 2
    RESTRICTED = 1
    LEFT = 0
    BANNED = -1
```

---

### Media Types

All media types are dataclasses with `slots=True`, inheriting from `Media`.

| Class | Key Attributes |
|-------|----------------|
| `Media` | `media_type`, `raw` |
| `Photo` | `width`, `height`, `file_id`, `file_size`, `file_name` |
| `Video` | `width`, `height`, `duration`, `file_id`, `file_size`, `file_name`, `thumb` |
| `Audio` | `duration`, `performer`, `title`, `file_id`, `file_size`, `file_name` |
| `Document` | `file_id`, `file_size`, `file_name`, `mime_type` |
| `Voice` | `duration`, `file_id`, `file_size`, `mime_type` |
| `VideoNote` | `duration`, `file_id`, `file_size`, `mime_type` |
| `Sticker` | `sticker_id`, `emoji`, `set_name`, `width`, `height`, `is_animated` |
| `Animation` | `file_name`, `width`, `height`, `duration`, `file_id`, `file_size` |
| `Contact` | `phone_number`, `first_name`, `last_name`, `user_id` |
| `Location` | `latitude`, `longitude` |
| `PollMedia` / `Poll` | `question`, `options`, `is_anonymous`, `total_voter_count` |
| `Dice` | `emoji`, `value` |

---

### Object Types

| Class | Attributes |
|-------|------------|
| `MessageEntity` | `type`, `offset`, `length`, `url`, `user_id`, `language`, `custom_emoji_id` |
| `InlineKeyboardButton` | `text`, `callback_data`, `url`, `switch_inline_query`, `switch_inline_query_current_chat` |
| `KeyboardButton` | `text`, `request_contact`, `request_location` |
| `ReplyMarkup` | `inline_keyboard`, `keyboard`, `is_one_time`, `is_resize`, `selective`, `placeholder` |
| `ForceReply` | `selective`, `placeholder` |
| `MessageReplyHeader` | `reply_to_msg_id`, `reply_to_peer_id`, `quote` |

---

### Project Structure

```
spluspy/
├── __init__.py          # Public API
├── __version__.py       # Version info
├── cli.py               # CLI entry point
├── config.py            # Configuration
├── compat.py            # Compatibility layer
├── afk.py               # AFK auto-responder
├── admin.py             # Chat administration
├── mirror.py            # Message mirroring engine
├── client/              # Client and conversation API
│   ├── client.py        # Main Client class
│   ├── conversation.py  # Conversation API
│   ├── chat_mixin.py    # Chat management mixin
│   └── media_mixin.py   # Media operations mixin
├── models/              # Domain models (Message, User, Chat, Media, etc.)
│   ├── message.py       # Message dataclass
│   ├── user.py          # User dataclass
│   ├── chat.py          # Chat, Channel, Group dataclasses
│   ├── bot.py           # Button factory
│   ├── media.py         # Media type dataclasses
│   ├── objects.py       # MessageEntity, ReplyMarkup, etc.
│   └── enums.py         # ChatType, UserStatus, etc.
├── events/              # Event types and builders
├── filters/             # Composable message filters
├── errors/              # Custom exception hierarchy
├── session/             # Session backends (SQLite, Memory, String)
├── network/             # TCP connections and connection pool
├── storage/             # Key-value storage backends
├── plugins/             # Plugin loader
├── middleware/          # Middleware system
├── fsm/                 # Finite state machine
├── scheduler/           # Task scheduler
├── utils/               # Logger, cache, helpers
├── sync/                # Synchronous client wrapper
└── _engine/             # Low-level MTProto engine
```

---

### CLI

```bash
# Run a bot
spluspy run bot.py

# Run with custom session name
spluspy run bot.py --session my_bot

# Get session info
spluspy session-info my_session.session

# Show version
spluspy version

# Validate a bot script for syntax errors
spluspy validate bot.py
```

### Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install spluspy
RUN pip install --no-cache-dir spluspy[all]

# Copy your bot script
COPY bot.py .

# Run the bot
CMD ["python", "bot.py"]
```

Build and run:

```bash
docker build -t my-spluspy-bot .
docker run -v ./sessions:/app/sessions my-spluspy-bot
```

---

## فارسی

### ویژگی‌ها

| ویژگی | توضیحات |
|-------|---------|
| **بدون نیاز به API Key** | کلیدهای سروش پلاس به صورت داخلی |
| **ناهمگام کامل** | ساخته شده با `asyncio` پایتون |
| **پشتیبانی از حالت همگام** | استفاده بدون `async/await` از طریق `spluspy.sync` |
| **پشتیبانی ربات و کاربر** | هر دو نوع حساب |
| **هندلرهای رویدادمحور** | سیستم رویداد قدرتمند با دکوراتورها |
| **سیستم فیلتر** | فیلترهای قابل ترکیب (`&`, `\|`, `~`) |
| **دکمه‌های اینلاین و ریپلای** | کیبوردهای تعاملی |
| **API مکالمه** | برای جریان‌های تعاملی ربات |
| **FSM (ماشین حالت محدود)** | مدیریت وضعیت داخلی برای ربات‌ها |
| **سیستم پلاگین** | بارگذاری پویای پلاگین‌ها |
| **میان‌افزار (Middleware)** | پردازش قبل/بعد از به‌روزرسانی‌ها |
| **زمان‌بند (Scheduler)** | زمان‌بندی داخلی وظایف |
| **بک‌اندهای ذخیره‌سازی متعدد** | حافظه، SQLite، Redis، PostgreSQL |
| **محدودیت نرخ (Rate Limiting)** | الگوریتم سطل توکن با مدیریت انتظار سیلاب |
| **پاسخ خودکار AFK** | پاسخگوی هوشمند با محدودیت نرخ به ازای هر چت |
| **مدیریت چت** | مسدود کردن، بی‌صدا کردن، سنجاق، پاکسازی — API مدیریتی |
| **آینه‌سازی پیام** | کلون کردن پیام و رسانه به صورت بلادرنگ بین چت‌ها |
| **عملیات دسته‌ای** | ارسال، حذف، فوروارد چندین پیام به صورت همزمان |
| **انتقال فایل با پیشرفت** | آپلود/دانلود با ردیابی پیشرفت |
| **لاگ حرفه‌ای** | لاگرهای ساختاریافته و فضای نام‌دار |
| **نوع‌نویسی در همه جا** | ایمنی کامل نوع |
| **معماری تمیز** | اصول SOLID، طراحی ماژولار |

### پیش‌نیازها

- پایتون 3.10 به بالا
- نیازی به کلید API خارجی نیست (کلیدهای سروش پلاس به صورت داخلی)

### نصب

```bash
pip install spluspy
```

برای رمزگذاری سریع‌تر:

```bash
pip install spluspy[speed]
```

با بک‌اند Redis:

```bash
pip install spluspy[redis]
```

با بک‌اند PostgreSQL:

```bash
pip install spluspy[postgres]
```

همه وابستگی‌های اختیاری:

```bash
pip install spluspy[all]
```

### شروع سریع

#### ساده‌ترین ربات

```python
from spluspy import Client

bot = Client("my_session")

@bot.on_message()
async def handler(client, message):
    await message.reply("سلام!")

bot.run()
```

#### حساب کاربری

```python
from spluspy import Client

client = Client("session_name")

@client.on_message()
async def handler(client, message):
    await message.reply("سلام دنیا!")

async def main():
    await client.start(phone="+98XXXXXXXXXX")
    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
```

#### استفاده همگام (بدون Async/Await)

```python
from spluspy.sync import Client

bot = Client("session")

@bot.on_message()
def handler(client, message):
    message.reply("سلام!")

bot.run()
```

### رویدادها

| دکوراتور | رویداد |
|----------|--------|
| `@bot.on_message()` | پیام جدید |
| `@bot.on_edited_message()` | ویرایش پیام |
| `@bot.on_callback_query()` | کلیک دکمه اینلاین |
| `@bot.on_inline_query()` | کوئری اینلاین |
| `@bot.on_chat_action()` | پیوستن/خروج/سنجاق |
| `@bot.on_user_update()` | تغییر وضعیت |
| `@bot.on_message_deleted()` | حذف پیام |
| `@bot.on_message_read()` | رسید خواندن |
| `@bot.on_error()` | مدیریت خطای سراسری |

#### اولویت رویداد

```python
from spluspy.events import HandlerPriority

@bot.on_message(priority=HandlerPriority.FIRST)
async def high_priority_handler(client, message):
    pass

@bot.on_message(priority=HandlerPriority.LOW)
async def low_priority_handler(client, message):
    pass
```

#### توقف انتشار

```python
@bot.on_message()
async def stopper(client, message):
    if message.text == "/stop":
        message.stop_propagation()
        await message.reply("توقف!")
```

### فیلترها

```python
from spluspy import filters

@bot.on_message(filters.text)                    # فقط متن
@bot.on_message(filters.private)                 # چت‌های خصوصی
@bot.on_message(filters.group)                   # گروه‌ها
@bot.on_message(filters.command("start"))        # دستور /start
@bot.on_message(filters.regex(r"\d+"))           # تطابق با عبارت باقاعده
@bot.on_message(filters.user(123))               # کاربر خاص
@bot.on_message(filters.text & filters.private)  # ترکیبی
@bot.on_message(filters.photo | filters.video)   # عکس یا ویدیو
```

### متدهای پیام

```python
await message.reply("سلام")              # پاسخ
await message.edit("متن جدید")           # ویرایش
await message.delete()                    # حذف
await message.forward(chat_id)            # فوروارد
await message.copy(chat_id)               # کپی (بدون هدر فوروارد)
await message.pin()                       # سنجاق
await message.react("❤️")                 # واکنش
await message.mark_read()                 # علامت خواندن
await message.download()                  # دانلود رسانه
await message.reply_photo("photo.jpg")    # پاسخ با عکس
await message.reply_video("video.mp4")    # پاسخ با ویدیو
await message.reply_document("file.pdf")  # پاسخ با سند
```

### دکمه‌ها

```python
from spluspy import Button

# کیبورد اینلاین
keyboard = Button.build_inline([
    Button.inline("گزینه ۱", b"opt1"),
    Button.inline("گزینه ۲", b"opt2")
])
await bot.send_message(chat_id, "انتخاب کنید:", buttons=keyboard)

# کیبورد ریپلای
kb = Button.build_reply([
    Button.text("منو"),
    Button.text("تنظیمات")
])
await bot.send_message(chat_id, "انتخاب کنید:", buttons=kb)

# حذف کیبورد
await bot.send_message(chat_id, "تمام", buttons=Button.clear())
```

### FSM (ماشین حالت محدود)

```python
from spluspy.fsm import State, StateMachine
from spluspy.storage import MemoryStorage

storage = MemoryStorage()
fsm = StateMachine(storage)

class Form:
    name = State()
    age = State()

@bot.on_message(filters.command("register"))
async def start_register(client, message):
    ctx = fsm.context(message.sender_id)
    await ctx.set_state(Form.name)
    await message.reply("نام شما چیست؟")

@bot.on_message(filters.private)
async def process_form(client, message):
    ctx = fsm.context(message.sender_id)
    state = await ctx.get_state()

    if state == Form.name:
        await ctx.set_data(name=message.text)
        await ctx.set_state(Form.age)
        await message.reply("سن شما چقدر است؟")
    elif state == Form.age:
        data = await ctx.get_data()
        await ctx.reset()
        await message.reply(f"ثبت شد! نام: {data.get('name')}, سن: {message.text}")
```

### بک‌اندهای ذخیره‌سازی

```python
from spluspy.storage import MemoryStorage, SQLiteStorage, RedisStorage, PostgresStorage, get_storage

# حافظه (پیش‌فرض)
storage = MemoryStorage()

# SQLite
storage = SQLiteStorage("data.db")

# Redis
storage = RedisStorage(host="localhost", port=6379, db=0)

# PostgreSQL
storage = PostgresStorage(dsn="postgresql://user:pass@localhost/db")

# تابع کارخانه
storage = get_storage("redis", host="localhost")
```

### سیستم پلاگین

```python
# plugins/hello.py
def register(client):
    @client.on_message(filters.command("hello"))
    async def hello_handler(client, message):
        await message.reply("سلام از پلاگین!")
```

```python
# main.py
from spluspy import Client

bot = Client("session")
bot.plugins.load("plugins")
bot.run()
```

### میان‌افزار (Middleware)

```python
from spluspy.middleware import Middleware

class LoggingMiddleware(Middleware):
    async def on_update(self, update, handler):
        print(f"به‌روزرسانی دریافت شد: {update}")
        result = await handler(update)
        print(f"هندلر تکمیل شد")
        return result

bot.middleware.add(LoggingMiddleware())
```

### محدودیت نرخ

```python
from spluspy.utils import RateLimiter

limiter = RateLimiter(max_calls=10, period=60)

@bot.on_message()
async def limited_handler(client, message):
    if not limiter.allow():
        await message.reply("محدودیت نرخ! دوباره تلاش کنید.")
        return
    await message.reply("باشه")
```

### پاسخ خودکار AFK

```python
from spluspy import Client, filters
from spluspy.afk import AfkManager

bot = Client("my_account")
afk = AfkManager(bot, message="الان AFK هستم. زود برمی‌گردم!")

@bot.on_message(filters.command("afk"))
async def set_afk(client, message):
    afk.set_afk(True, reason="ناهار")
    await message.reply("الان AFK هستم!")

@bot.on_message(filters.command("back"))
async def unset_afk(client, message):
    afk.set_afk(False)
    await message.reply(f"برگشتم! {afk.total_replies} پاسخ خودکار ارسال شد.")
```

### مدیریت چت

```python
from spluspy.admin import ChatAdmin

admin = ChatAdmin(bot)

await admin.ban_user(chat_id, user_id)
await admin.unban_user(chat_id, user_id)
await admin.mute_user(chat_id, user_id)
await admin.unmute_user(chat_id, user_id)
await admin.pin_message(chat_id, message)
await admin.unpin_message(chat_id, message)
await admin.unpin_all(chat_id)
await admin.purge_messages(chat_id, limit=100)

# عملیات دسته‌ای
await admin.bulk_action(chat_id, "ban", [user_id1, user_id2])

# لاگ مدیریتی
events = await admin.get_admin_log(chat_id, limit=50)
```

### آینه‌سازی پیام

```python
from spluspy.mirror import MessageMirror

mirror = MessageMirror(bot)

mirror.add_route(
    source=-1001234567890,
    targets=[-1009876543210, -1001112223334],
    strip_forward=True,
    strip_sender=False,
    add_prefix="[Mirror]"
)

await mirror.start()
```

### زمان‌بند

```python
from spluspy.scheduler.scheduler import MessageScheduler

scheduler = MessageScheduler(bot)

# ارسال پیام هر ساعت
scheduler.schedule_interval("hourly_greeting", chat_id, "سلام!", interval=3600)

# ارسال پیام با تاخیر
scheduler.schedule_once("reminder", chat_id, "فراموش نکن!", delay=300)

# لغو وظیفه زمان‌بندی شده
scheduler.cancel("hourly_greeting")
```

### مدیریت خطا

```python
from spluspy import filters
from spluspy.errors import FloodWait, Unauthorized, BadRequest

@bot.on_message()
async def safe_handler(client, message):
    try:
        await message.reply("سلام!")
    except FloodWait as e:
        await asyncio.sleep(e.seconds)
    except Unauthorized:
        await message.reply("غیرمجاز!")
    except BadRequest as e:
        print(f"درخواست نادرست: {e}")
```

### عملیات دسته‌ای

```python
# ارسال چندین پیام
messages = ["سلام ۱", "سلام ۲", "سلام ۳"]
results = await bot.batch_send(chat_id, messages)

# حذف چندین پیام
await bot.batch_delete(chat_id, [msg1, msg2, msg3])

# فوروارد چندین پیام
await bot.batch_forward(chat_id, [msg1, msg2])
```

### انتقال فایل با پیشرفت

```python
from spluspy.utils import ProgressTracker

# آپلود با پیشرفت
tracker = ProgressTracker(on_progress=lambda p: print(f"{p.percent}%"))
await bot.send_document(chat_id, "فایل_بزرگ.zip", progress=tracker)

# دانلود با پیشرفت
await message.download(progress=tracker)
```

### رابط خط فرمان (CLI)

```bash
# اجرای ربات
spluspy run bot.py

# اجرا با نشست سفارشی
spluspy run bot.py --session my_bot

# اطلاعات نشست
spluspy session-info my_session.session

# نمایش نسخه
spluspy version

# اعتبارسنجی اسکریپت ربات
spluspy validate bot.py
```

### Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir spluspy[all]

COPY bot.py .

CMD ["python", "bot.py"]
```

ساخت و اجرا:

```bash
docker build -t my-spluspy-bot .
docker run -v ./sessions:/app/sessions my-spluspy-bot
```

### ساختار پروژه

```
spluspy/
├── __init__.py          # API عمومی
├── __version__.py       # اطلاعات نسخه
├── cli.py               # نقطه ورود CLI
├── config.py            # پیکربندی
├── compat.py            # لایه سازگاری
├── afk.py               # پاسخگوی خودکار AFK
├── admin.py             # مدیریت چت
├── mirror.py            # موتور آینه‌سازی پیام
├── client/              # کلاینت و API مکالمه
│   ├── client.py        # کلاس اصلی Client
│   ├── conversation.py  # API مکالمه
│   ├── chat_mixin.py    # میکسین مدیریت چت
│   └── media_mixin.py   # میکسین عملیات رسانه
├── models/              # مدل‌های دامنه
│   ├── message.py       # داده‌کلاس Message
│   ├── user.py          # داده‌کلاس User
│   ├── chat.py          # داده‌کلاس Chat, Channel, Group
│   ├── bot.py           # کارخانه Button
│   ├── media.py         # انواع رسانه
│   ├── objects.py       # MessageEntity, ReplyMarkup, و غیره
│   └── enums.py         # ChatType, UserStatus, و غیره
├── events/              # انواع رویداد و بیلدرها
├── filters/             # فیلترهای قابل ترکیب پیام
├── errors/              # سلسله مراتب استثنای سفارشی
├── session/             # بک‌اندهای نشست
├── network/             # اتصالات TCP و استخر اتصال
├── storage/             # بک‌اندهای ذخیره‌سازی کلید-مقدار
├── plugins/             # بارگذار پلاگین
├── middleware/          # سیستم میان‌افزار
├── fsm/                 # ماشین حالت محدود
├── scheduler/           # زمان‌بند وظایف
├── utils/               # لاگر، کش، کمک‌کننده‌ها
├── sync/                # کلاینت همگام‌سازی شده
└── _engine/             # موتور MTProto سطح پایین
```

### سلسله مراتب خطاها

```
SplusPyError
├── SoroushPlusAPIError
│   ├── RPCError
│   │   ├── FloodWait
│   │   ├── Unauthorized
│   │   ├── Forbidden
│   │   ├── BadRequest
│   │   │   ├── ChatNotFound
│   │   │   ├── UserNotFound
│   │   │   └── MessageNotFound
│   │   └── ...
│   ├── SessionExpiredError
│   └── SessionError
├── AuthError
├── ValidationError
├── TimeoutError
├── ConnectionError
├── PluginError
├── FSMError
├── StorageError
├── JoinChatError
│   ├── InvalidInviteLinkError
│   ├── InviteLinkExpiredError
│   ├── ChatFullError
│   ├── ChatDeactivatedError
│   └── MembershipRequiredError
└── FloodWaitError (محدودیت نرخ)
```

---

## Contributing / مشارکت

### English

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Set up the development environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e ".[dev]"
   ```
4. Make your changes
5. Run linting and formatting:
   ```bash
   ruff check spluspy/
   black spluspy/
   ```
6. Run type checking:
   ```bash
   mypy spluspy/
   ```
7. Run tests: `pytest`
8. Submit a pull request

### فارسی

1. مخزن را Fork کنید
2. شاخه ویژگی بسازید (`git checkout -b feature/your-feature`)
3. محیط توسعه را راه‌اندازی کنید:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e ".[dev]"
   ```
4. تغییرات خود را اعمال کنید
5. لینتر و فرمت‌کننده را اجرا کنید:
   ```bash
   ruff check spluspy/
   black spluspy/
   ```
6. بررسی نوع را اجرا کنید:
   ```bash
   mypy spluspy/
   ```
7. تست‌ها را اجرا کنید: `pytest`
8. درخواست Pull ارسال کنید

---

## License / مجوز

MIT License — see [LICENSE](LICENSE) for details.

مجوز MIT — جزئیات را در [LICENSE](LICENSE) مشاهده کنید.

---

## Disclaimer / سلب مسئولیت

**English:**
SPlusPy is an unofficial third-party library. Use it responsibly and ensure your applications comply with Soroush Plus's Terms of Service.

**فارسی:**
SPlusPy یک کتابخانه غیررسمی و شخص ثالث است. مسئولانه از آن استفاده کنید و مطمئن شوید برنامه‌های شما با شرایط استفاده سروش پلاس مطابقت دارند.

---

<div align="center">

**Made with ❤️ for the Soroush Plus community**

**ساخته شده با ❤️ برای جامعه سروش پلاس**

</div>
