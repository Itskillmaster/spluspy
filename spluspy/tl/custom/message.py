import logging
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from .chatgetter import ChatGetter
from .sendergetter import SenderGetter
from .forward import Forward
from .file import File
from .. import TLObject, types, functions
from ... import utils, errors
from ...enums import MessageMediaType

_log = logging.getLogger(__name__)

class Message(ChatGetter, SenderGetter, TLObject):
    def __init__(
        self,
        id: int,
        peer_id: types.TypePeer,
        date: Optional[datetime] = None,
        message: Optional[str] = None,
        out: Optional[bool] = None,
        mentioned: Optional[bool] = None,
        media_unread: Optional[bool] = None,
        silent: Optional[bool] = None,
        post: Optional[bool] = None,
        from_scheduled: Optional[bool] = None,
        legacy: Optional[bool] = None,
        edit_hide: Optional[bool] = None,
        pinned: Optional[bool] = None,
        noforwards: Optional[bool] = None,
        invert_media: Optional[bool] = None,
        from_id: Optional[types.TypePeer] = None,
        fwd_from: Optional[types.TypeMessageFwdHeader] = None,
        via_bot_id: Optional[int] = None,
        reply_to: Optional[types.TypeMessageReplyHeader] = None,
        media: Optional[types.TypeMessageMedia] = None,
        reply_markup: Optional[types.TypeReplyMarkup] = None,
        entities: Optional[List[types.TypeMessageEntity]] = None,
        views: Optional[int] = None,
        forwards: Optional[int] = None,
        replies: Optional['types.TypeMessageReplies'] = None,
        edit_date: Optional[datetime] = None,
        post_author: Optional[str] = None,
        grouped_id: Optional[int] = None,
        reactions: Optional['types.TypeMessageReactions'] = None,
        restriction_reason: Optional[List] = None,
        ttl_period: Optional[int] = None,
        action: Optional[types.TypeMessageAction] = None,
        **kwargs,
    ):
        self.id = id
        self.peer_id = peer_id
        self.date = date
        self.message = message
        self.out = bool(out)
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.silent = silent
        self.post = post
        self.from_scheduled = from_scheduled
        self.legacy = legacy
        self.edit_hide = edit_hide
        self.pinned = pinned
        self.noforwards = noforwards
        self.invert_media = invert_media
        self.from_id = from_id
        self.fwd_from = fwd_from
        self.via_bot_id = via_bot_id
        self.reply_to = reply_to
        self.media = None if isinstance(media, types.MessageMediaEmpty) else media
        self.reply_markup = reply_markup
        self.entities = entities
        self.views = views
        self.forwards = forwards
        self.replies = replies
        self.edit_date = edit_date
        self.post_author = post_author
        self.grouped_id = grouped_id
        self.reactions = reactions
        self.restriction_reason = restriction_reason
        self.ttl_period = ttl_period
        self.action = action

        self._client = None
        self._text = None
        self._file = None
        self._reply_message = None
        self._forward = None

        sender_id = None
        if from_id is not None:
            sender_id = utils.get_peer_id(from_id)
        elif peer_id:
            if post or (not out and isinstance(peer_id, types.PeerUser)):
                sender_id = utils.get_peer_id(peer_id)

        ChatGetter.__init__(self, peer_id, broadcast=post)
        SenderGetter.__init__(self, sender_id)

    def _finish_init(self, client, entities, input_chat):
        self._client = client
        if self.peer_id == types.PeerUser(client._self_id) and not self.fwd_from:
            self.out = True

        cache = client._mb_entity_cache
        self._sender, self._input_sender = utils._get_entity_pair(self.sender_id, entities, cache)
        self._chat, self._input_chat = utils._get_entity_pair(self.chat_id, entities, cache)
        if input_chat:
            self._input_chat = input_chat
        if self.fwd_from:
            self._forward = Forward(self._client, self.fwd_from, entities)

    @property
    def client(self):
        return self._client

    @property
    def text(self):
        if self._text is None and self._client:
            if not self._client.parse_mode:
                self._text = self.message
            else:
                self._text = self._client.parse_mode.unparse(self.message, self.entities)
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        if self._client and self._client.parse_mode:
            self.message, self.entities = self._client.parse_mode.parse(value)
        else:
            self.message, self.entities = value, []

    @property
    def raw_text(self):
        return self.message

    @property
    def is_reply(self):
        return self.reply_to is not None

    @property
    def forward(self):
        return self._forward

    @property
    def file(self):
        if not self._file:
            media = self.photo or self.document
            if media:
                self._file = File(media)
        return self._file

    @property
    def media_type(self):
        """
        Returns the MessageMediaType of this message.

        Usage:
            from spluspy.enums import MessageMediaType

            @client.on_message()
            async def handler(client, event):
                media_type = event.message.media_type

                if media_type == MessageMediaType.PHOTO:
                    await event.reply("عکس دریافت شد!")
                elif media_type == MessageMediaType.VIDEO:
                    await event.reply("ویدیو دریافت شد!")
                elif media_type == MessageMediaType.STICKER:
                    await event.reply("استیکر دریافت شد!")
        """
        return MessageMediaType.from_media(self.media)

    @property
    def photo(self):
        if isinstance(self.media, types.MessageMediaPhoto):
            return self.media.photo
        return None

    @property
    def document(self):
        if isinstance(self.media, types.MessageMediaDocument):
            return self.media.document
        return None

    @property
    def audio(self):
        return self._document_by_attribute(types.DocumentAttributeAudio, lambda attr: not attr.voice)

    @property
    def voice(self):
        return self._document_by_attribute(types.DocumentAttributeAudio, lambda attr: attr.voice)

    @property
    def video(self):
        return self._document_by_attribute(types.DocumentAttributeVideo)

    @property
    def gif(self):
        return self._document_by_attribute(types.DocumentAttributeAnimated)

    @property
    def sticker(self):
        return self._document_by_attribute(types.DocumentAttributeSticker)

    def _document_by_attribute(self, kind, condition=None):
        doc = self.document
        if doc:
            for attr in doc.attributes:
                if isinstance(attr, kind):
                    if not condition or condition(attr):
                        return doc
        return None

    async def get_reply_message(self):
        if self._reply_message is None and self._client:
            if not isinstance(self.reply_to, types.MessageReplyHeader):
                return None
            self._reply_message = await self._client.get_messages(
                await self.get_input_chat() if self.is_channel else None,
                ids=self.reply_to.reply_to_msg_id
            )
        return self._reply_message

    async def respond(self, *args, **kwargs):
        if self._client:
            return await self._client.send_message(await self.get_input_chat(), *args, **kwargs)

    async def reply(self, *args, **kwargs):
        if self._client:
            kwargs['reply_to'] = self.id
            return await self._client.send_message(await self.get_input_chat(), *args, **kwargs)

    async def edit(self, *args, **kwargs):
        if self._client:
            return await self._client.edit_message(await self.get_input_chat(), self.id, *args, **kwargs)

    async def delete(self, *args, **kwargs):
        if self._client:
            return await self._client.delete_messages(await self.get_input_chat(), [self.id], *args, **kwargs)

    async def tag_member(self, user, text: str = None):
        if not self._client:
            return
        user_id = await self._client.get_peer_id(user)
        display_text = text or str(user_id)
        # Using markdown style mention for self-bot
        mention = f"[{display_text}](tg://user?id={user_id})"
        return await self.reply(mention)

    async def download_media(self, *args, **kwargs):
        if self._client:
            return await self._client.download_media(self, *args, **kwargs)

    # region Convenience reply methods

    async def reply_text(self, text, **kwargs):
        """
        Replies to this message with a text message.

        Args:
            text: The text to send.
            **kwargs: Additional arguments passed to send_message.

        Returns:
            The sent Message object.
        """
        if self._client:
            kwargs.setdefault('reply_to', self.id)
            return await self._client.send_message(
                await self.get_input_chat(), text, **kwargs)

    async def reply_photo(self, photo, caption=None, **kwargs):
        """
        Replies to this message with a photo.

        Args:
            photo: The photo to send (file path, bytes, or InputMedia).
            caption: Optional caption for the photo.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        if self._client:
            kwargs.setdefault('reply_to', self.id)
            return await self._client.send_file(
                await self.get_input_chat(), photo, caption=caption, **kwargs)

    async def reply_video(self, video, caption=None, **kwargs):
        """
        Replies to this message with a video.

        Args:
            video: The video to send (file path, bytes, or InputMedia).
            caption: Optional caption for the video.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        if self._client:
            kwargs.setdefault('reply_to', self.id)
            return await self._client.send_file(
                await self.get_input_chat(), video, caption=caption, **kwargs)

    async def reply_audio(self, audio, caption=None, **kwargs):
        """
        Replies to this message with an audio file.

        Args:
            audio: The audio to send (file path, bytes, or InputMedia).
            caption: Optional caption for the audio.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        if self._client:
            kwargs.setdefault('reply_to', self.id)
            return await self._client.send_file(
                await self.get_input_chat(), audio, caption=caption, **kwargs)

    async def reply_voice(self, voice, caption=None, **kwargs):
        """
        Replies to this message with a voice note.

        Args:
            voice: The voice note to send (file path, bytes, or InputMedia).
            caption: Optional caption for the voice note.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        if self._client:
            kwargs.setdefault('reply_to', self.id)
            kwargs.setdefault('voice_note', True)
            return await self._client.send_file(
                await self.get_input_chat(), voice, caption=caption, **kwargs)

    async def reply_document(self, document, caption=None, **kwargs):
        """
        Replies to this message with a document.

        Args:
            document: The document to send (file path, bytes, or InputMedia).
            caption: Optional caption for the document.
            **kwargs: Additional arguments passed to send_file.

        Returns:
            The sent Message object.
        """
        if self._client:
            kwargs.setdefault('reply_to', self.id)
            return await self._client.send_file(
                await self.get_input_chat(), document, caption=caption, **kwargs)

    # endregion

    # region Convenience action methods

    async def forward(self, to_chat_id, **kwargs):
        """
        Forwards this message to another chat.

        Args:
            to_chat_id: The destination chat ID or entity.
            **kwargs: Additional arguments passed to forward_messages.

        Returns:
            The forwarded Message object.
        """
        if self._client:
            return await self._client.forward_messages(
                to_chat_id, self, from_peer=self.chat_id, **kwargs)

    async def copy(self, to_chat_id, **kwargs):
        """
        Copies this message to another chat without the "Forwarded from" tag.

        Args:
            to_chat_id: The destination chat ID or entity.
            **kwargs: Additional arguments passed to forward_messages.

        Returns:
            The copied Message object.
        """
        if self._client:
            return await self._client.forward_messages(
                to_chat_id, self, from_peer=self.chat_id,
                drop_author=True, **kwargs)

    async def pin(self, **kwargs):
        """
        Pins this message in the chat.

        Args:
            **kwargs: Additional arguments passed to pin_message
                (notify, pm_oneside).

        Returns:
            The result of pin_message.
        """
        if self._client:
            return await self._client.pin_message(
                self.chat_id, self.id, **kwargs)

    async def unpin(self, **kwargs):
        """
        Unpins this message from the chat.

        Args:
            **kwargs: Additional arguments passed to unpin_message.

        Returns:
            The result of unpin_message.
        """
        if self._client:
            return await self._client.unpin_message(
                self.chat_id, self.id, **kwargs)

    async def react(self, emoji, **kwargs):
        """
        Adds a reaction (emoji) to this message.

        Args:
            emoji: The emoji reaction to add.
            **kwargs: Additional arguments passed to send_reaction.

        Returns:
            The result of send_reaction.
        """
        if self._client:
            return await self._client.send_reaction(
                self.chat_id, self.id, emoji, **kwargs)

    async def download(self, file_name=None, **kwargs):
        """
        Downloads the media attached to this message.

        Args:
            file_name: Optional output file name/path.
            **kwargs: Additional arguments passed to download_media.

        Returns:
            The file path or bytes of the downloaded media.
        """
        if self._client:
            return await self._client.download_media(
                self, file=file_name, **kwargs)

    async def mark_read(self, **kwargs):
        """
        Marks this message as read (sends read acknowledge).

        Args:
            **kwargs: Additional arguments passed to send_read_acknowledge.

        Returns:
            The result of send_read_acknowledge.
        """
        if self._client:
            return await self._client.send_read_acknowledge(
                self.chat_id, self.id, **kwargs)

    # endregion
