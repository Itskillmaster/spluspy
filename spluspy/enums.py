from enum import Enum


class MessageMediaType(Enum):
    PHOTO = "photo"
    VIDEO = "video"
    VIDEO_NOTE = "video_note"
    DOCUMENT = "document"
    AUDIO = "audio"
    VOICE = "voice"
    STICKER = "sticker"
    ANIMATION = "animation"
    GIF = "gif"
    WEB_PAGE = "web_page"
    GEO = "geo"
    GEO_LIVE = "geo_live"
    CONTACT = "contact"
    GAME = "game"
    POLL = "poll"
    DICE = "dice"
    VENUE = "venue"
    STORY = "story"
    GIVEAWAY = "giveaway"
    INVOICE = "invoice"
    UNSUPPORTED = "unsupported"
    EMPTY = "empty"

    @classmethod
    def from_media(cls, media):
        """
        Detect MessageMediaType from a MessageMedia object.

        Usage:
            from spluspy.enums import MessageMediaType
            media_type = MessageMediaType.from_media(message.media)
        """
        from .tl import types

        if media is None or isinstance(media, types.MessageMediaEmpty):
            return cls.EMPTY

        if isinstance(media, types.MessageMediaPhoto):
            return cls.PHOTO

        if isinstance(media, types.MessageMediaDocument):
            doc = media.document
            if doc is None or isinstance(doc, types.DocumentEmpty):
                return cls.DOCUMENT

            attrs = {type(a): a for a in doc.attributes}

            if types.DocumentAttributeSticker in attrs:
                return cls.STICKER

            if types.DocumentAttributeAnimated in attrs:
                if types.DocumentAttributeVideo in attrs:
                    return cls.ANIMATION
                return cls.GIF

            if types.DocumentAttributeVideo in attrs:
                vid = attrs[types.DocumentAttributeVideo]
                if vid.round_message:
                    return cls.VIDEO_NOTE
                return cls.VIDEO

            if types.DocumentAttributeAudio in attrs:
                aud = attrs[types.DocumentAttributeAudio]
                if aud.voice:
                    return cls.VOICE
                return cls.AUDIO

            return cls.DOCUMENT

        if isinstance(media, types.MessageMediaWebPage):
            return cls.WEB_PAGE

        if isinstance(media, types.MessageMediaGeo):
            return cls.GEO

        if isinstance(media, types.MessageMediaGeoLive):
            return cls.GEO_LIVE

        if isinstance(media, types.MessageMediaContact):
            return cls.CONTACT

        if isinstance(media, types.MessageMediaGame):
            return cls.GAME

        if isinstance(media, types.MessageMediaPoll):
            return cls.POLL

        if isinstance(media, types.MessageMediaDice):
            return cls.DICE

        if isinstance(media, types.MessageMediaVenue):
            return cls.VENUE

        if isinstance(media, types.MessageMediaStory):
            return cls.STORY

        if isinstance(media, types.MessageMediaGiveaway):
            return cls.GIVEAWAY

        if isinstance(media, types.MessageMediaInvoice):
            return cls.INVOICE

        if isinstance(media, types.MessageMediaUnsupported):
            return cls.UNSUPPORTED

        return cls.EMPTY

    @classmethod
    def from_message(cls, message):
        """
        Detect MessageMediaType from a Message object.

        Usage:
            from spluspy.enums import MessageMediaType
            media_type = MessageMediaType.from_message(event.message)
        """
        if hasattr(message, 'media'):
            return cls.from_media(message.media)
        return cls.EMPTY

    def is_image(self):
        return self == self.PHOTO

    def is_video(self):
        return self in (self.VIDEO, self.VIDEO_NOTE, self.ANIMATION)

    def is_audio(self):
        return self in (self.AUDIO, self.VOICE)

    def is_document(self):
        return self == self.DOCUMENT

    def is_sticker(self):
        return self == self.STICKER

    def is_animation(self):
        return self in (self.ANIMATION, self.GIF)

    def is_media(self):
        return self not in (self.EMPTY, self.UNSUPPORTED)
