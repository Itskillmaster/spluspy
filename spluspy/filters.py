import re
import typing

class Filter:
    async def __call__(self, client, message) -> bool:
        raise NotImplementedError

    def __and__(self, other):
        return AndFilter(self, other)

    def __or__(self, other):
        return OrFilter(self, other)

    def __invert__(self):
        return NotFilter(self)

class AndFilter(Filter):
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2

    async def __call__(self, client, message) -> bool:
        res1 = await self.f1(client, message)
        if not res1:
            return False
        return await self.f2(client, message)

class OrFilter(Filter):
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2

    async def __call__(self, client, message) -> bool:
        res1 = await self.f1(client, message)
        if res1:
            return True
        return await self.f2(client, message)

class NotFilter(Filter):
    def __init__(self, f1):
        self.f1 = f1

    async def __call__(self, client, message) -> bool:
        return not await self.f1(client, message)

class PrivateFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return getattr(message, 'is_private', False)

class GroupFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return getattr(message, 'is_group', False)

class ChannelFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return getattr(message, 'is_channel', False)

class MeFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return getattr(message, 'out', False)

class TextFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return bool(getattr(message, 'text', None))

class LinkFilter(Filter):
    async def __call__(self, client, message) -> bool:
        text = getattr(message, 'text', '') or ''
        return bool(re.search(r'(https?://[^\s]+)', text))

class MediaFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return bool(getattr(message, 'media', None))

class PhotoFilter(Filter):
    async def __call__(self, client, message) -> bool:
        from .tl import types
        return isinstance(getattr(message, 'media', None), types.MessageMediaPhoto)

class VideoFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return bool(getattr(message, 'video', None))

class DocumentFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return bool(getattr(message, 'document', None))

class AudioFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return bool(getattr(message, 'audio', None))

class VoiceFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return bool(getattr(message, 'voice', None))

class StickerFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return bool(getattr(message, 'sticker', None))

class AnimationFilter(Filter):
    async def __call__(self, client, message) -> bool:
        return bool(getattr(message, 'gif', None))

class CommandFilter(Filter):
    def __init__(self, commands, prefixes="/"):
        self.commands = [commands] if isinstance(commands, str) else commands
        self.prefixes = prefixes

    async def __call__(self, client, message) -> bool:
        text = getattr(message, 'text', None)
        if not text:
            return False
        for prefix in self.prefixes:
            for command in self.commands:
                if text.startswith(f"{prefix}{command}"):
                    return True
        return False

class RegexFilter(Filter):
    def __init__(self, pattern):
        self.pattern = re.compile(pattern)

    async def __call__(self, client, message) -> bool:
        text = getattr(message, 'text', None)
        if not text:
            return False
        return bool(self.pattern.search(text))

class WordFilter(Filter):
    def __init__(self, words):
        self.words = [words] if isinstance(words, str) else words

    async def __call__(self, client, message) -> bool:
        text = getattr(message, 'text', None)
        if not text:
            return False
        text = text.lower()
        for word in self.words:
            if word.lower() in text:
                return True
        return False

class NewChatMembersFilter(Filter):
    async def __call__(self, client, message) -> bool:
        from .tl import types
        return isinstance(getattr(message, 'action', None), types.MessageActionChatAddUser)

class LeftChatMemberFilter(Filter):
    async def __call__(self, client, message) -> bool:
        from .tl import types
        return isinstance(getattr(message, 'action', None), types.MessageActionChatDeleteUser)

class FilterModule:
    def __init__(self):
        self.private = PrivateFilter()
        self.group = GroupFilter()
        self.channel = ChannelFilter()
        self.me = MeFilter()
        self.text = TextFilter()
        self.link = LinkFilter()
        self.media = MediaFilter()
        self.photo = PhotoFilter()
        self.video = VideoFilter()
        self.document = DocumentFilter()
        self.audio = AudioFilter()
        self.voice = VoiceFilter()
        self.sticker = StickerFilter()
        self.animation = AnimationFilter()
        self.new_chat_members = NewChatMembersFilter()
        self.left_chat_member = LeftChatMemberFilter()

    def command(self, commands, prefixes="/"):
        return CommandFilter(commands, prefixes)

    def regex(self, pattern):
        return RegexFilter(pattern)

    def word(self, words):
        return WordFilter(words)

filters = FilterModule()
