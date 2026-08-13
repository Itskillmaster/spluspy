import typing
from ..tl import functions, types
from .. import helpers, utils, hints

if typing.TYPE_CHECKING:
    from .soroushclient import SoroushClient


class ExtraMethods:

    # =====================================================================
    # region Messaging & Media Methods
    # =====================================================================

    async def send_photo(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        photo: 'hints.FileLike',
        caption: str = None,
        reply_to_message_id: int = None,
        **kwargs
    ) -> 'types.Message':
        """
        Sends a photo to the specified chat.

        Args:
            chat_id: Target chat ID or entity.
            photo: The photo file (path, bytes, IO, or URL).
            caption: Optional caption for the photo.
            reply_to_message_id: Optional message ID to reply to.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        return await self.send_file(
            chat_id, photo, caption=caption,
            reply_to=reply_to_message_id, **kwargs)

    async def send_video(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        video: 'hints.FileLike',
        caption: str = None,
        reply_to_message_id: int = None,
        **kwargs
    ) -> 'types.Message':
        """
        Sends a video to the specified chat.

        Args:
            chat_id: Target chat ID or entity.
            video: The video file (path, bytes, IO, or URL).
            caption: Optional caption for the video.
            reply_to_message_id: Optional message ID to reply to.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        return await self.send_file(
            chat_id, video, caption=caption,
            reply_to=reply_to_message_id, **kwargs)

    async def send_audio(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        audio: 'hints.FileLike',
        caption: str = None,
        reply_to_message_id: int = None,
        **kwargs
    ) -> 'types.Message':
        """
        Sends an audio file to the specified chat.

        Args:
            chat_id: Target chat ID or entity.
            audio: The audio file (path, bytes, IO, or URL).
            caption: Optional caption for the audio.
            reply_to_message_id: Optional message ID to reply to.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        return await self.send_file(
            chat_id, audio, caption=caption,
            reply_to=reply_to_message_id, **kwargs)

    async def send_voice(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        voice: 'hints.FileLike',
        caption: str = None,
        reply_to_message_id: int = None,
        **kwargs
    ) -> 'types.Message':
        """
        Sends a voice note to the specified chat.

        Args:
            chat_id: Target chat ID or entity.
            voice: The voice file (path, bytes, IO, or URL).
            caption: Optional caption for the voice note.
            reply_to_message_id: Optional message ID to reply to.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        kwargs.setdefault('voice_note', True)
        return await self.send_file(
            chat_id, voice, caption=caption,
            reply_to=reply_to_message_id, **kwargs)

    async def send_document(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        document: 'hints.FileLike',
        caption: str = None,
        reply_to_message_id: int = None,
        **kwargs
    ) -> 'types.Message':
        """
        Sends a document to the specified chat.

        Args:
            chat_id: Target chat ID or entity.
            document: The document file (path, bytes, IO, or URL).
            caption: Optional caption for the document.
            reply_to_message_id: Optional message ID to reply to.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        return await self.send_file(
            chat_id, document, caption=caption,
            reply_to=reply_to_message_id, **kwargs)

    async def copy_message(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        from_chat_id: 'hints.EntityLike',
        message_id: int,
        **kwargs
    ) -> 'types.Message':
        """
        Sends a copy of a message to another chat without the
        "Forwarded from" tag.

        Args:
            chat_id: Destination chat ID or entity.
            from_chat_id: Source chat ID or entity.
            message_id: The message ID to copy.
            **kwargs: Additional arguments passed to forward_messages.

        Returns:
            The sent Message object.
        """
        return await self.forward_messages(
            chat_id, message_id, from_chat_id,
            drop_author=True, **kwargs)

    async def send_reaction(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        message_id: int,
        emoji: str,
        **kwargs
    ):
        """
        Adds a reaction (emoji) to a message.

        Args:
            chat_id: The chat ID or entity where the message is.
            message_id: The message ID to react to.
            emoji: The emoji to react with.
            **kwargs: Additional arguments.

        Returns:
            The result of the API call.
        """
        entity = await self.get_input_entity(chat_id)
        return await self(functions.messages.SendReactionRequest(
            peer=entity,
            msg_id=message_id,
            reaction=[types.ReactionEmoji(emoticon=emoji)],
            **kwargs
        ))

    async def read_chat_history(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike'
    ) -> bool:
        """
        Sends a read acknowledge for the chat (marks all messages as seen).

        Args:
            chat_id: The chat ID or entity.

        Returns:
            True on success.
        """
        return await self.send_read_acknowledge(chat_id)

    # endregion

    # =====================================================================
    # region Chats, Dialogs & Admin Methods
    # =====================================================================

    async def get_chat(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike'
    ):
        """
        Fetches full chat/group/channel information.

        Args:
            chat_id: The chat ID, username, or entity.

        Returns:
            The full chat info (FullChannel or FullChat).
        """
        entity = await self.get_input_entity(chat_id)
        if helpers._entity_type(entity) == helpers._EntityType.CHANNEL:
            return await self(functions.channels.GetFullChannelRequest(entity))
        else:
            return await self(functions.messages.GetFullChatRequest(entity.chat_id))

    async def get_chat_info(self: 'SoroushClient', chat_id):
        """Alias for get_chat. Returns the entity for the given chat."""
        return await self.get_entity(chat_id)

    async def get_user(self: 'SoroushClient', user_id):
        """Alias for get_entity. Returns the entity for the given user."""
        return await self.get_entity(user_id)

    async def get_full_chat(self: 'SoroushClient', chat_id):
        """Alias for get_chat. Returns full chat/channel info."""
        return await self.get_chat(chat_id)

    async def get_dialogs(
        self: 'SoroushClient',
        limit: int = 0,
        **kwargs
    ):
        """
        Fetches the user's active dialogs (chats).

        Args:
            limit: Maximum number of dialogs to return. 0 for all.
            **kwargs: Additional arguments passed to iter_dialogs.

        Returns:
            A TotalList of Dialog objects.
        """
        return await self.iter_dialogs(limit=limit or None, **kwargs).collect()

    async def get_chat_history(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        limit: int = 20,
        offset_id: int = 0,
        **kwargs
    ):
        """
        Fetches message history for a chat.

        Args:
            chat_id: The chat ID or entity.
            limit: Maximum number of messages to return.
            offset_id: Start fetching from this message ID (exclusive).
            **kwargs: Additional arguments passed to get_messages.

        Returns:
            A TotalList of Message objects.
        """
        return await self.get_messages(
            chat_id, limit=limit, offset_id=offset_id, **kwargs)

    async def search_messages(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike' = None,
        query: str = '',
        limit: int = 20,
        filter_type: 'typing.Union[types.TypeMessagesFilter, typing.Type[types.TypeMessagesFilter]]' = None,
        **kwargs
    ):
        """
        Searches for messages in a chat or globally.

        Args:
            chat_id: The chat ID or entity. None for global search.
            query: The search query string.
            limit: Maximum number of results.
            filter_type: Optional filter (e.g. InputMessagesFilterPhotos).
            **kwargs: Additional arguments passed to get_messages.

        Returns:
            A TotalList of matching Message objects.
        """
        return await self.get_messages(
            chat_id, limit=limit, search=query,
            filter=filter_type, **kwargs)

    async def create_group(
        self: 'SoroushClient',
        title: str,
        users: 'typing.Sequence[hints.EntityLike]'
    ):
        """
        Creates a new group chat.

        Args:
            title: The group title.
            users: A list of users to add to the group.

        Returns:
            The result of the API call (Chat object).
        """
        input_users = []
        for user in users:
            input_users.append(await self.get_input_entity(user))
        return await self(functions.messages.CreateChatRequest(
            users=input_users, title=title))

    async def create_channel(
        self: 'SoroushClient',
        title: str,
        about: str = '',
        megagroup: bool = False
    ):
        """
        Creates a new channel or megagroup.

        Args:
            title: The channel title.
            about: The channel description.
            megagroup: If True, creates a megagroup (supergroup) instead
                of a broadcast channel.

        Returns:
            The result of the API call (Updates with Channel).
        """
        return await self(functions.channels.CreateChannelRequest(
            title=title, about=about, megagroup=megagroup))

    async def archive_chat(self: 'SoroushClient', chat_id: 'hints.EntityLike'):
        """
        Archives a chat.

        Args:
            chat_id: The chat ID or entity to archive.
        """
        entity = await self.get_input_entity(chat_id)
        return await self(functions.folders.EditFolderRequest(
            folder=types.InputFolderPeer(
                peer=entity, folder_id=1),
            on_behalf_of_peer_id=types.InputPeerEmpty()
        ))

    async def unarchive_chat(self: 'SoroushClient', chat_id: 'hints.EntityLike'):
        """
        Unarchives a chat.

        Args:
            chat_id: The chat ID or entity to unarchive.
        """
        entity = await self.get_input_entity(chat_id)
        return await self(functions.folders.EditFolderRequest(
            folder=types.InputFolderPeer(
                peer=entity, folder_id=0),
            on_behalf_of_peer_id=types.InputPeerEmpty()
        ))

    async def ban_chat_member(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        user_id: 'hints.EntityLike'
    ):
        """
        Bans a user from a chat (removes and prevents re-joining).

        Args:
            chat_id: The chat ID or entity.
            user_id: The user to ban.
        """
        entity = await self.get_input_entity(chat_id)
        user = await self.get_input_entity(user_id)
        ty = helpers._entity_type(entity)
        if ty == helpers._EntityType.CHANNEL:
            return await self(functions.channels.EditBannedRequest(
                channel=entity,
                participant=user,
                banned_rights=types.ChatBannedRights(
                    until_date=None, view_messages=True)))
        else:
            return await self(functions.messages.DeleteChatUserRequest(
                entity.chat_id, user))

    async def unban_chat_member(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        user_id: 'hints.EntityLike'
    ):
        """
        Unbans a user from a chat (allows re-joining).

        Args:
            chat_id: The chat ID or entity.
            user_id: The user to unban.
        """
        entity = await self.get_input_entity(chat_id)
        user = await self.get_input_entity(user_id)
        ty = helpers._entity_type(entity)
        if ty == helpers._EntityType.CHANNEL:
            return await self(functions.channels.EditBannedRequest(
                channel=entity,
                participant=user,
                banned_rights=types.ChatBannedRights(until_date=None)))
        else:
            raise ValueError('Unbanning is only supported in channels/supergroups')

    async def restrict_chat_member(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        user_id: 'hints.EntityLike',
        permissions: 'types.ChatBannedRights' = None,
        **kwargs
    ):
        """
        Restricts a user's permissions in a chat.

        Args:
            chat_id: The chat ID or entity.
            user_id: The user to restrict.
            permissions: A ChatBannedRights object specifying restrictions.
                If None, uses **kwargs to build one.
            **kwargs: Permission flags passed to ChatBannedRights constructor.
                Set to False to restrict (True = allowed by default).
                e.g. send_messages=False, send_media=False.
        """
        entity = await self.get_input_entity(chat_id)
        user = await self.get_input_entity(user_id)
        if permissions is None:
            permissions = types.ChatBannedRights(**kwargs)
        return await self(functions.channels.EditBannedRequest(
            channel=entity,
            participant=user,
            banned_rights=permissions))

    async def promote_chat_member(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        user_id: 'hints.EntityLike',
        privileges: 'types.ChatAdminRights' = None,
        title: str = '',
        **kwargs
    ):
        """
        Promotes a user to admin in a chat.

        Args:
            chat_id: The chat ID or entity.
            user_id: The user to promote.
            privileges: A ChatAdminRights object specifying admin privileges.
                If None, uses **kwargs to build one.
            title: Custom admin title (rank).
            **kwargs: Privilege flags passed to ChatAdminRights constructor.
                e.g. delete_messages=True, ban_users=True, pin_messages=True.
        """
        entity = await self.get_input_entity(chat_id)
        user = await self.get_input_entity(user_id)
        if privileges is None:
            privileges = types.ChatAdminRights(**kwargs)
        return await self(functions.channels.EditAdminRequest(
            channel=entity,
            user_id=user,
            admin_rights=privileges,
            rank=title))

    async def set_chat_title(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        title: str
    ):
        """
        Sets the title of a chat.

        Args:
            chat_id: The chat ID or entity.
            title: The new title.
        """
        return await self._extra_set_chat_title(chat_id, title)

    async def _extra_set_chat_title(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        title: str
    ):
        entity = await self.get_input_entity(chat_id)
        if helpers._entity_type(entity) == helpers._EntityType.CHANNEL:
            return await self(functions.channels.EditTitleRequest(entity, title))
        else:
            return await self(functions.messages.EditChatTitleRequest(
                entity.chat_id, title))

    async def set_chat_description(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        description: str = ''
    ):
        """
        Sets the description/about of a chat.

        Args:
            chat_id: The chat ID or entity.
            description: The new description.
        """
        entity = await self.get_input_entity(chat_id)
        if helpers._entity_type(entity) == helpers._EntityType.CHANNEL:
            return await self(functions.channels.EditAboutRequest(
                entity, description))
        else:
            return await self(functions.messages.EditChatAboutRequest(
                entity, description))

    async def set_chat_photo(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        photo: 'hints.FileLike'
    ):
        """
        Sets the photo of a chat.

        Args:
            chat_id: The chat ID or entity.
            photo: The photo file (path, bytes, IO, or InputChatPhoto).
        """
        entity = await self.get_input_entity(chat_id)
        if isinstance(photo, (str, bytes)) or hasattr(photo, 'read'):
            photo = await self.upload_file(photo)
        if isinstance(photo, types.InputFile):
            photo = types.InputChatUploadedPhoto(photo=photo)
        if helpers._entity_type(entity) == helpers._EntityType.CHANNEL:
            return await self(functions.channels.EditPhotoRequest(
                entity, photo))
        else:
            return await self(functions.messages.EditChatPhotoRequest(
                entity, photo))

    async def pin_chat_message(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        message_id: int,
        notify: bool = False
    ):
        """
        Pins a message in a chat.

        Args:
            chat_id: The chat ID or entity.
            message_id: The message ID to pin.
            notify: Whether to notify members.
        """
        return await self.pin_message(chat_id, message_id, notify=notify)

    async def unpin_chat_message(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        message_id: int = None
    ):
        """
        Unpins a message from a chat, or all messages if message_id is None.

        Args:
            chat_id: The chat ID or entity.
            message_id: The message ID to unpin. None to unpin all.
        """
        if message_id is None:
            return await self.unpin_all_messages(chat_id)
        return await self.unpin_message(chat_id, message_id)

    async def unpin_all_chat_messages(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike'
    ):
        """
        Unpins all messages in a chat.

        Args:
            chat_id: The chat ID or entity.
        """
        return await self.unpin_all_messages(chat_id)

    # endregion

    # =====================================================================
    # region Users, Profile & Security Methods
    # =====================================================================

    async def get_users(
        self: 'SoroushClient',
        user_ids: 'typing.Union[hints.EntityLike, typing.Sequence[hints.EntityLike]]'
    ):
        """
        Resolves one or more user IDs/usernames to User objects.

        Args:
            user_ids: A single user ID/username or a list of them.

        Returns:
            A single User or list of Users.
        """
        return await self.get_entity(user_ids)

    async def get_chat_members(
        self: 'SoroushClient',
        chat_id: 'hints.EntityLike',
        limit: int = 0,
        **kwargs
    ):
        """
        Fetches members of a group/channel.

        Args:
            chat_id: The chat ID or entity.
            limit: Maximum number of members. 0 for all.
            **kwargs: Additional arguments passed to get_participants.

        Returns:
            A TotalList of User objects with .participant attribute.
        """
        return await self.get_participants(
            chat_id, limit=limit or None, **kwargs)

    async def update_profile(
        self: 'SoroushClient',
        first_name: str = None,
        last_name: str = None,
        about: str = None
    ):
        """
        Updates the current user's profile information.

        Args:
            first_name: New first name.
            last_name: New last name.
            about: New bio/about text.
        """
        return await self(functions.account.UpdateProfileRequest(
            first_name=first_name or '',
            last_name=last_name or '',
            about=about
        ))

    async def update_username(
        self: 'SoroushClient',
        username: str
    ):
        """
        Updates the current user's username.

        Args:
            username: The new username.
        """
        return await self(functions.account.UpdateUsernameRequest(
            username=username))

    async def update_profile_photo(
        self: 'SoroushClient',
        photo: 'hints.FileLike'
    ):
        """
        Updates the current user's profile photo.

        Args:
            photo: The photo file (path, bytes, IO, or InputPhoto.
        """
        if isinstance(photo, (str, bytes)) or hasattr(photo, 'read'):
            photo = await self.upload_file(photo)
        if isinstance(photo, types.InputFile):
            photo = types.InputUploadedPhoto(file=photo)
        return await self(functions.photos.UpdateProfilePhotoRequest(
            file=photo))

    async def get_contacts(self: 'SoroushClient'):
        """
        Fetches the user's contact list.

        Returns:
            A list of User objects from the contact list.
        """
        result = await self(functions.contacts.GetContactsRequest(
            hash=0))
        return result.users

    async def add_contact(
        self: 'SoroushClient',
        phone: str,
        first_name: str,
        last_name: str = ''
    ):
        """
        Adds a phone number to the user's contact list.

        Args:
            phone: The phone number (with country code).
            first_name: Contact's first name.
            last_name: Contact's last name.
        """
        return await self(functions.contacts.AddContactRequest(
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            phone_hash='',
            add_phone_privacy_exception=True
        ))

    async def delete_contacts(
        self: 'SoroushClient',
        user_ids: 'typing.Union[hints.EntityLike, typing.Sequence[hints.EntityLike]]'
    ):
        """
        Deletes users from the contact list.

        Args:
            user_ids: A single user ID or a list of user IDs.
        """
        if not utils.is_list_like(user_ids):
            user_ids = (user_ids,)
        input_users = []
        for uid in user_ids:
            input_users.append(await self.get_input_entity(uid))
        return await self(functions.contacts.DeleteContactsRequest(
            id=input_users))

    async def block_user(
        self: 'SoroushClient',
        user_id: 'hints.EntityLike'
    ):
        """
        Blocks a user.

        Args:
            user_id: The user to block.
        """
        user = await self.get_input_entity(user_id)
        return await self(functions.contacts.BlockRequest(id=[user]))

    async def unblock_user(
        self: 'SoroushClient',
        user_id: 'hints.EntityLike'
    ):
        """
        Unblocks a user.

        Args:
            user_id: The user to unblock.
        """
        user = await self.get_input_entity(user_id)
        return await self(functions.contacts.UnblockRequest(id=[user]))

    async def get_active_sessions(self: 'SoroushClient'):
        """
        Lists all connected devices/sessions.

        Returns:
            A list of Authorizations (sessions).
        """
        result = await self(functions.account.GetAuthorizationsRequest())
        return result.authorizations

    async def terminate_session(
        self: 'SoroushClient',
        session_hash: bytes
    ):
        """
        Terminates (revokes) a specific session.

        Args:
            session_hash: The hash of the session to terminate.
        """
        return await self(functions.account.ResetAuthorizationRequest(
            hash=session_hash))

    async def join_chat(
        self: 'SoroushClient',
        chat: 'hints.EntityLike'
    ):
        """
        Joins a chat by invite link or username.

        Args:
            chat: The invite link, username, or hash to join.

        Returns:
            The joined Chat object.
        """
        if isinstance(chat, str) and 'splus.ir/joingroup/' in chat:
            import re
            match = re.search(r'splus\.ir/joingroup/([a-zA-Z0-9_-]+)', chat)
            if match:
                invite_hash = match.group(1)
            else:
                invite_hash = chat
        elif isinstance(chat, str):
            invite_hash = chat
        else:
            return await self.get_entity(chat)

        result = await self(
            functions.messages.ImportChatInviteRequest(invite_hash))

        if hasattr(result, 'chats') and result.chats:
            return result.chats[0]
        elif hasattr(result, 'chat'):
            return result.chat
        return result

    # endregion
