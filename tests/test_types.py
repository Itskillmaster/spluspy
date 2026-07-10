"""Tests for type definitions."""

from __future__ import annotations

import pytest

from spluspy.types.message import Message
from spluspy.types.user import User
from spluspy.types.chat import Chat, Channel, Group
from spluspy.types.enums import ChatType, MessageMediaType, UserStatus
from spluspy.types.bot import Button, CallbackQuery
from spluspy.types.objects import MessageEntity, InlineKeyboardButton


class TestMessage:
    """Tests for the Message type."""

    def test_basic_properties(self) -> None:
        msg = Message(id=1, text="Hello", chat_id=123)
        assert msg.id == 1
        assert msg.text == "Hello"
        assert msg.chat_id == 123
        assert msg.message_id == 1

    def test_is_media(self) -> None:
        msg = Message(media_type=MessageMediaType.PHOTO)
        assert msg.is_media is True
        msg2 = Message(media_type=MessageMediaType.NONE)
        assert msg2.is_media is False

    def test_is_reply(self) -> None:
        msg = Message(reply_to=100)
        assert msg.is_reply is True
        msg2 = Message(reply_to=None)
        assert msg2.is_reply is False

    def test_is_forwarded(self) -> None:
        msg = Message(forward_origin={"type": "user"})
        assert msg.is_forwarded is True
        msg2 = Message(forward_origin=None)
        assert msg2.is_forwarded is False

    def test_str(self) -> None:
        msg = Message(id=1, text="Hello World")
        assert str(msg) == "Hello World"

    def test_hash(self) -> None:
        msg1 = Message(id=1, chat_id=100)
        msg2 = Message(id=1, chat_id=100)
        msg3 = Message(id=2, chat_id=100)
        assert hash(msg1) == hash(msg2)
        assert hash(msg1) != hash(msg3)

    def test_equality(self) -> None:
        msg1 = Message(id=1, chat_id=100)
        msg2 = Message(id=1, chat_id=100)
        msg3 = Message(id=2, chat_id=100)
        assert msg1 == msg2
        assert msg1 != msg3


class TestUser:
    """Tests for the User type."""

    def test_basic_properties(self) -> None:
        user = User(id=1, first_name="Ali", last_name="Mirshekari")
        assert user.id == 1
        assert user.full_name == "Ali Mirshekari"
        assert user.first_name == "Ali"
        assert user.last_name == "Mirshekari"

    def test_mention(self) -> None:
        user = User(id=1, username="ali")
        assert user.mention == "@ali"

    def test_mention_no_username(self) -> None:
        user = User(id=1, first_name="Ali")
        assert user.mention == "Ali"

    def test_link(self) -> None:
        user = User(id=1, username="ali")
        assert user.link == "https://t.me/ali"

    def test_link_no_username(self) -> None:
        user = User(id=1, first_name="Ali")
        assert user.link is None

    def test_hash(self) -> None:
        user1 = User(id=1)
        user2 = User(id=1)
        user3 = User(id=2)
        assert hash(user1) == hash(user2)
        assert hash(user1) != hash(user3)

    def test_equality(self) -> None:
        user1 = User(id=1)
        user2 = User(id=1)
        user3 = User(id=2)
        assert user1 == user2
        assert user1 != user3


class TestChat:
    """Tests for the Chat type."""

    def test_basic_properties(self) -> None:
        chat = Chat(id=100, title="My Chat")
        assert chat.id == 100
        assert chat.title == "My Chat"

    def test_chat_types(self) -> None:
        private = Chat(id=1, type=ChatType.PRIVATE)
        assert private.is_private is True
        assert private.is_group is False

        group = Chat(id=2, type=ChatType.GROUP)
        assert group.is_group is True

        channel = Chat(id=3, type=ChatType.CHANNEL)
        assert channel.is_channel is True

    def test_channel_subclass(self) -> None:
        ch = Channel(id=100, title="My Channel")
        assert ch.is_channel is True
        assert ch.type == ChatType.CHANNEL

    def test_group_subclass(self) -> None:
        g = Group(id=200, title="My Group")
        assert g.is_group is True


class TestButton:
    """Tests for the Button factory."""

    def test_inline_button(self) -> None:
        btn = Button.inline("Click", b"data")
        assert isinstance(btn, InlineKeyboardButton)
        assert btn.text == "Click"
        assert btn.callback_data == b"data"

    def test_url_button(self) -> None:
        btn = Button.url("Visit", "https://example.com")
        assert btn.url == "https://example.com"

    def test_build_inline(self) -> None:
        markup = Button.build_inline(
            [Button.inline("A", b"a"), Button.inline("B", b"b")]
        )
        assert markup.inline_keyboard is not None
        assert len(markup.inline_keyboard) == 1
        assert len(markup.inline_keyboard[0]) == 2

    def test_clear(self) -> None:
        markup = Button.clear()
        assert markup.keyboard == []


class TestCallbackQuery:
    """Tests for the CallbackQuery type."""

    def test_text_decode(self) -> None:
        cq = CallbackQuery(id="1", data=b"hello")
        assert cq.text == "hello"

    def test_text_none(self) -> None:
        cq = CallbackQuery(id="1", data=None)
        assert cq.text is None

    def test_text_invalid_utf8(self) -> None:
        cq = CallbackQuery(id="1", data=b"\xff\xfe")
        assert cq.text is None
