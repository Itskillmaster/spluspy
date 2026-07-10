"""Tests for the filter system."""

from __future__ import annotations

import pytest

from spluspy.filters.filters import (
    Text,
    Media,
    Photo,
    Video,
    Audio,
    Voice,
    Command,
    Regex,
    User,
    Chat,
    Group,
    Private,
    Channel,
    Reply,
    Forwarded,
    Me,
    Bot,
    Incoming,
    Outgoing,
)
from spluspy.types.enums import MessageMediaType, ChatType
from spluspy.types.message import Message
from spluspy.types.user import User as UserType


def _make_message(
    text: str = "",
    media_type: MessageMediaType = MessageMediaType.NONE,
    chat_type: ChatType = ChatType.PRIVATE,
    sender_id: int = 1,
    is_reply: bool = False,
    is_forwarded: bool = False,
) -> Message:
    """Helper to create test messages."""
    msg = Message(
        text=text,
        media_type=media_type,
        is_private=chat_type == ChatType.PRIVATE,
        is_group=chat_type in (ChatType.GROUP, ChatType.SUPERGROUP),
        is_channel=chat_type == ChatType.CHANNEL,
        sender_id=sender_id,
        reply_to=1 if is_reply else None,
        forward_origin={"from_id": 1} if is_forwarded else None,
    )
    msg.sender = UserType(id=sender_id, is_bot=False)
    return msg


class TestBasicFilters:
    """Tests for basic filters."""

    def test_text_filter(self) -> None:
        f = Text()
        assert f(_make_message(text="hello")) is True
        assert f(_make_message(text="")) is False
        assert f(_make_message(media_type=MessageMediaType.PHOTO)) is False

    def test_media_filter(self) -> None:
        f = Media()
        assert f(_make_message(media_type=MessageMediaType.PHOTO)) is True
        assert f(_make_message(media_type=MessageMediaType.NONE)) is False

    def test_photo_filter(self) -> None:
        f = Photo()
        assert f(_make_message(media_type=MessageMediaType.PHOTO)) is True
        assert f(_make_message(media_type=MessageMediaType.VIDEO)) is False

    def test_video_filter(self) -> None:
        f = Video()
        assert f(_make_message(media_type=MessageMediaType.VIDEO)) is True
        assert f(_make_message(media_type=MessageMediaType.AUDIO)) is False

    def test_audio_filter(self) -> None:
        f = Audio()
        assert f(_make_message(media_type=MessageMediaType.AUDIO)) is True

    def test_voice_filter(self) -> None:
        f = Voice()
        assert f(_make_message(media_type=MessageMediaType.VOICE)) is True


class TestChatFilters:
    """Tests for chat type filters."""

    def test_private_filter(self) -> None:
        f = Private()
        assert f(_make_message(chat_type=ChatType.PRIVATE)) is True
        assert f(_make_message(chat_type=ChatType.GROUP)) is False

    def test_group_filter(self) -> None:
        f = Group()
        assert f(_make_message(chat_type=ChatType.GROUP)) is True
        assert f(_make_message(chat_type=ChatType.PRIVATE)) is False

    def test_channel_filter(self) -> None:
        f = Channel()
        assert f(_make_message(chat_type=ChatType.CHANNEL)) is True
        assert f(_make_message(chat_type=ChatType.PRIVATE)) is False

    def test_reply_filter(self) -> None:
        f = Reply()
        assert f(_make_message(is_reply=True)) is True
        assert f(_make_message(is_reply=False)) is False

    def test_forwarded_filter(self) -> None:
        f = Forwarded()
        assert f(_make_message(is_forwarded=True)) is True
        assert f(_make_message(is_forwarded=False)) is False


class TestCommandFilter:
    """Tests for the command filter."""

    def test_default_prefix(self) -> None:
        f = Command("start")
        assert f(_make_message(text="/start")) is True
        assert f(_make_message(text="!start")) is True
        assert f(_make_message(text="start")) is False

    def test_multiple_commands(self) -> None:
        f = Command("start", "help")
        assert f(_make_message(text="/start")) is True
        assert f(_make_message(text="/help")) is True
        assert f(_make_message(text="/other")) is False

    def test_custom_prefixes(self) -> None:
        f = Command("go", prefixes=["."])
        assert f(_make_message(text=".go")) is True
        assert f(_make_message(text="/go")) is False


class TestRegexFilter:
    """Tests for the regex filter."""

    def test_basic_regex(self) -> None:
        f = Regex(r"\d+")
        assert f(_make_message(text="hello 123")) is True
        assert f(_make_message(text="no numbers")) is False

    def test_case_insensitive_pattern(self) -> None:
        f = Regex(r"(?i)hello")
        assert f(_make_message(text="Hello World")) is True
        assert f(_make_message(text="HELLO")) is True


class TestUserFilter:
    """Tests for the user filter."""

    def test_user_filter(self) -> None:
        f = User(1, 2, 3)
        assert f(_make_message(sender_id=1)) is True
        assert f(_make_message(sender_id=4)) is False


class TestChatFilter:
    """Tests for the chat filter."""

    def test_chat_filter(self) -> None:
        f = Chat(100, 200)
        msg = _make_message()
        msg.chat_id = 100
        assert f(msg) is True
        msg.chat_id = 300
        assert f(msg) is False


class TestFilterComposition:
    """Tests for filter composition with &, |, ~."""

    def test_and_filter(self) -> None:
        f = Text() & Private()
        assert f(_make_message(text="hi", chat_type=ChatType.PRIVATE)) is True
        assert f(_make_message(text="hi", chat_type=ChatType.GROUP)) is False

    def test_or_filter(self) -> None:
        f = Photo() | Video()
        assert f(_make_message(media_type=MessageMediaType.PHOTO)) is True
        assert f(_make_message(media_type=MessageMediaType.VIDEO)) is True
        assert f(_make_message(media_type=MessageMediaType.AUDIO)) is False

    def test_not_filter(self) -> None:
        f = ~Bot()
        msg = _make_message()
        msg.sender = UserType(id=1, is_bot=False)
        assert f(msg) is True
        msg.sender = UserType(id=1, is_bot=True)
        assert f(msg) is False
