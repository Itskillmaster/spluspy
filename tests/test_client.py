"""Tests for the Client class — comprehensive coverage."""

from __future__ import annotations

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from spluspy.client.client import Client
from spluspy.events.message import NewMessage, NewMessageEventBuilder
from spluspy.types.message import Message


@pytest.fixture
def client() -> Client:
    """Create a test client with an in-memory session."""
    return Client(":memory:", api_id=12345, api_hash="test_hash", log_level=10)


def _make_mock_client(**methods: MagicMock | AsyncMock) -> MagicMock:
    """Build a mock underlying client with given method stubs."""
    mock = MagicMock()
    for name, fn in methods.items():
        setattr(mock, name, fn)
    return mock


# ───────────────────────────────────────────────────────────────────
# Init / Lifecycle
# ───────────────────────────────────────────────────────────────────


class TestClientInit:
    """Tests for Client initialization."""

    def test_default_session(self) -> None:
        c = Client(":memory:", api_id=12345, api_hash="test_hash")
        assert c is not None
        assert c._connected is False

    def test_custom_session_name(self) -> None:
        c = Client(":memory:", api_id=12345, api_hash="test_hash")
        assert c.session is not None

    def test_properties(self) -> None:
        c = Client(":memory:", api_id=12345, api_hash="test_hash")
        assert c._middleware is not None
        assert c._plugins is not None
        assert c._scheduler is not None


class TestClientLifecycle:
    """Tests for Client connect/disconnect lifecycle."""

    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires network access to Soroush Plus server")
    async def test_connect_disconnect(self) -> None:
        c = Client(":memory:", api_id=12345, api_hash="test_hash")
        await c.connect()
        assert c._connected is True
        await c.disconnect()
        assert c._connected is False

    @pytest.mark.asyncio
    @pytest.mark.skip(reason="Requires network access to Soroush Plus server")
    async def test_double_connect(self) -> None:
        c = Client(":memory:", api_id=12345, api_hash="test_hash")
        await c.connect()
        await c.connect()
        assert c._connected is True
        await c.disconnect()


# ───────────────────────────────────────────────────────────────────
# Event Registration
# ───────────────────────────────────────────────────────────────────


class TestEventRegistration:
    """Tests for event handler registration."""

    def test_on_message(self, client: Client) -> None:
        @client.on_message()
        async def handler(m: Message) -> None:
            pass
        assert len(client._handlers) > 0

    def test_on_edited(self, client: Client) -> None:
        @client.on_edited()
        async def handler(m: Message) -> None:
            pass
        assert len(client._handlers) > 0

    def test_on_callback_query(self, client: Client) -> None:
        @client.on_callback_query()
        async def handler(m: Message) -> None:
            pass
        assert len(client._handlers) > 0


# ───────────────────────────────────────────────────────────────────
# Message Sending
# ───────────────────────────────────────────────────────────────────


class TestMessageSending:
    """Tests for message sending methods."""

    @pytest.mark.asyncio
    async def test_send_message(self, client: Client) -> None:
        msg = await client.send_message(123, "Hello")
        assert isinstance(msg, Message)
        assert msg.text == "Hello"
        assert msg.chat_id == 123

    @pytest.mark.asyncio
    async def test_edit_message(self, client: Client) -> None:
        original = Message(id=1, chat_id=123, text="Old")
        edited = await client.edit_message(original, text="New")
        assert edited.text == "New"

    @pytest.mark.asyncio
    async def test_delete_messages(self, client: Client) -> None:
        result = await client.delete_messages(Message(id=1, chat_id=123))
        assert result is True

    @pytest.mark.asyncio
    async def test_send_photo(self, client: Client) -> None:
        msg = await client.send_photo(123, "photo.jpg", caption="Photo")
        assert isinstance(msg, Message)

    @pytest.mark.asyncio
    async def test_send_video(self, client: Client) -> None:
        msg = await client.send_video(123, "video.mp4")
        assert isinstance(msg, Message)

    @pytest.mark.asyncio
    async def test_send_document(self, client: Client) -> None:
        msg = await client.send_document(123, "file.pdf")
        assert isinstance(msg, Message)


# ───────────────────────────────────────────────────────────────────
# Chat ID Resolution
# ───────────────────────────────────────────────────────────────────


class TestResolveChatId:
    """Tests for _resolve_chat_id static helper."""

    def test_int_passthrough(self) -> None:
        assert Client._resolve_chat_id(123) == 123

    def test_tgme_link(self) -> None:
        assert Client._resolve_chat_id("https://t.me/my_channel") == "my_channel"

    def test_tgme_short_link(self) -> None:
        assert Client._resolve_chat_id("t.me/my_group") == "my_group"

    def test_at_username(self) -> None:
        assert Client._resolve_chat_id("@username") == "username"

    def test_bare_username(self) -> None:
        assert Client._resolve_chat_id("some_group") == "some_group"

    def test_whitespace_stripped(self) -> None:
        assert Client._resolve_chat_id("  my_group  ") == "my_group"


# ───────────────────────────────────────────────────────────────────
# join_chat — the main focus
# ───────────────────────────────────────────────────────────────────


class TestJoinChat:
    """Tests for join_chat — success, failure, input types."""

    @pytest.mark.asyncio
    async def test_join_by_int_id(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        entity = MagicMock(title="Test Chat")
        mock = _make_mock_client(join_chat=AsyncMock(return_value=entity))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        result = await c.join_chat(123)
        assert result is entity
        mock.join_chat.assert_awaited_once_with(123)

    @pytest.mark.asyncio
    async def test_join_by_username(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        entity = MagicMock(title="My Group")
        mock = _make_mock_client(join_chat=AsyncMock(return_value=entity))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        result = await c.join_chat("my_group")
        assert result is entity
        mock.join_chat.assert_awaited_once_with("my_group")

    @pytest.mark.asyncio
    async def test_join_by_tgme_link(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        entity = MagicMock(title="Channel")
        mock = _make_mock_client(join_chat=AsyncMock(return_value=entity))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        result = await c.join_chat("https://t.me/my_channel")
        assert result is entity
        mock.join_chat.assert_awaited_once_with("my_channel")

    @pytest.mark.asyncio
    async def test_join_by_at_username(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        entity = MagicMock(title="Group")
        mock = _make_mock_client(join_chat=AsyncMock(return_value=entity))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        result = await c.join_chat("@group")
        assert result is entity
        mock.join_chat.assert_awaited_once_with("group")

    @pytest.mark.asyncio
    async def test_join_failure_returns_none(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(
            join_chat=AsyncMock(side_effect=Exception("chat not found"))
        )
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        result = await c.join_chat(999)
        assert result is None

    @pytest.mark.asyncio
    async def test_join_no_connection_returns_none(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        # _get_client returns None
        result = await c.join_chat(123)
        assert result is None


# ───────────────────────────────────────────────────────────────────
# leave_chat
# ───────────────────────────────────────────────────────────────────


class TestLeaveChat:
    """Tests for leave_chat."""

    @pytest.mark.asyncio
    async def test_leave_success(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(leave_chat=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.leave_chat(123) is True

    @pytest.mark.asyncio
    async def test_leave_by_username(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(leave_chat=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.leave_chat("my_channel") is True
        mock.leave_chat.assert_awaited_once_with("my_channel")

    @pytest.mark.asyncio
    async def test_leave_failure_returns_false(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(
            leave_chat=AsyncMock(side_effect=Exception("not in chat"))
        )
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.leave_chat(999) is False

    @pytest.mark.asyncio
    async def test_leave_no_connection_returns_false(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        assert await c.leave_chat(123) is False


# ───────────────────────────────────────────────────────────────────
# ban / unban / mute / unmute
# ───────────────────────────────────────────────────────────────────


class TestBanUnbanMute:
    """Tests for ban_user, unban_user, mute_user, unmute_user."""

    @pytest.mark.asyncio
    async def test_ban_success(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(edit_permissions=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.ban_user(100, 200) is True
        mock.edit_permissions.assert_awaited_once_with(100, 200, view_messages=False)

    @pytest.mark.asyncio
    async def test_ban_failure(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(edit_permissions=AsyncMock(side_effect=Exception("fail")))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.ban_user(100, 200) is False

    @pytest.mark.asyncio
    async def test_ban_no_connection(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        assert await c.ban_user(100, 200) is False

    @pytest.mark.asyncio
    async def test_unban_success(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(edit_permissions=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.unban_user(100, 200) is True
        mock.edit_permissions.assert_awaited_once_with(100, 200)

    @pytest.mark.asyncio
    async def test_unban_failure(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(edit_permissions=AsyncMock(side_effect=Exception("fail")))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.unban_user(100, 200) is False

    @pytest.mark.asyncio
    async def test_mute_success(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(edit_permissions=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.mute_user(100, 200) is True
        mock.edit_permissions.assert_awaited_once_with(100, 200, send_messages=False)

    @pytest.mark.asyncio
    async def test_mute_failure(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(edit_permissions=AsyncMock(side_effect=Exception("fail")))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.mute_user(100, 200) is False

    @pytest.mark.asyncio
    async def test_unmute_delegates_to_unban(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(edit_permissions=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.unmute_user(100, 200) is True
        mock.edit_permissions.assert_awaited_once_with(100, 200)


# ───────────────────────────────────────────────────────────────────
# pin / unpin / unpin_all
# ───────────────────────────────────────────────────────────────────


class TestPinUnpin:
    """Tests for pin_message, unpin_message, unpin_all_messages."""

    @pytest.mark.asyncio
    async def test_pin_success(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(pin_message=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.pin_message(100, Message(id=5)) is True
        mock.pin_message.assert_awaited_once_with(100, 5, notify=False)

    @pytest.mark.asyncio
    async def test_pin_with_notify(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(pin_message=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.pin_message(100, 5, notify=True) is True
        mock.pin_message.assert_awaited_once_with(100, 5, notify=True)

    @pytest.mark.asyncio
    async def test_pin_failure(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(pin_message=AsyncMock(side_effect=Exception("fail")))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.pin_message(100, Message(id=5)) is False

    @pytest.mark.asyncio
    async def test_unpin_success(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(unpin_message=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.unpin_message(100, Message(id=5)) is True
        mock.unpin_message.assert_awaited_once_with(100, 5)

    @pytest.mark.asyncio
    async def test_unpin_failure(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(unpin_message=AsyncMock(side_effect=Exception("fail")))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.unpin_message(100, Message(id=5)) is False

    @pytest.mark.asyncio
    async def test_unpin_all_success(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(unpin_messages=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.unpin_all_messages(100) is True

    @pytest.mark.asyncio
    async def test_unpin_all_failure(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(unpin_messages=AsyncMock(side_effect=Exception("fail")))
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.unpin_all_messages(100) is False

    @pytest.mark.asyncio
    async def test_unpin_all_no_connection(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        assert await c.unpin_all_messages(100) is False


# ───────────────────────────────────────────────────────────────────
# mark_read
# ───────────────────────────────────────────────────────────────────


class TestMarkRead:
    """Tests for mark_read."""

    @pytest.mark.asyncio
    async def test_mark_read_all(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(send_read_acknowledge=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.mark_read(100) is True
        mock.send_read_acknowledge.assert_awaited_once_with(100)

    @pytest.mark.asyncio
    async def test_mark_read_specific_message(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(send_read_acknowledge=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.mark_read(100, Message(id=42)) is True
        mock.send_read_acknowledge.assert_awaited_once_with(100, 42)

    @pytest.mark.asyncio
    async def test_mark_read_int_message(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(send_read_acknowledge=AsyncMock())
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.mark_read(100, 42) is True
        mock.send_read_acknowledge.assert_awaited_once_with(100, 42)

    @pytest.mark.asyncio
    async def test_mark_read_failure(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        mock = _make_mock_client(
            send_read_acknowledge=AsyncMock(side_effect=Exception("fail"))
        )
        c._mtproto = MagicMock()
        c._mtproto.client = mock
        assert await c.mark_read(100) is False

    @pytest.mark.asyncio
    async def test_mark_read_no_connection(self) -> None:
        c = Client(":memory:", api_id=1, api_hash="h")
        assert await c.mark_read(100) is False
