"""Tests for session backends."""

from __future__ import annotations

import pytest
from spluspy.session.memory import MemorySession
from spluspy.session.string import StringSession
from spluspy.session.sqlite import SQLiteSession


@pytest.mark.asyncio
class TestMemorySession:
    """Tests for the in-memory session."""

    async def test_lifecycle(self) -> None:
        session = MemorySession()
        await session.start()
        assert session.get_user_id() is None
        session.set_user_id(123)
        assert session.get_user_id() == 123
        await session.close()

    async def test_auth_key(self) -> None:
        session = MemorySession()
        await session.start()
        key = b"test_auth_key_bytes"
        session.set_auth_key(key)
        assert session.get_auth_key() == key

    async def test_dc(self) -> None:
        session = MemorySession()
        await session.start()
        session.set_dc(2, "1.2.3.4", 443)
        assert session.get_dc() == 2

    async def test_context_manager(self) -> None:
        async with MemorySession() as session:
            session.set_user_id(456)
            assert session.get_user_id() == 456


@pytest.mark.asyncio
class TestStringSession:
    """Tests for the string session."""

    async def test_export_import(self) -> None:
        session = StringSession()
        session.set_user_id(123)
        session.set_dc(2, "1.2.3.4", 443)
        exported = session.export()

        restored = StringSession.import_string(exported)
        assert restored.get_user_id() == 123
        assert restored.get_dc() == 2

    async def test_invalid_string(self) -> None:
        with pytest.raises(ValueError):
            StringSession("not_valid_base64!")


@pytest.mark.asyncio
class TestSQLiteSession:
    """Tests for the SQLite session (single unified database)."""

    async def test_lifecycle(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.session"
        session = SQLiteSession("bot1", db_path=db_path)
        await session.start()
        session.set_user_id(123)
        assert session.get_user_id() == 123
        await session.close()

    async def test_persistence(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.session"
        session = SQLiteSession("bot1", db_path=db_path)
        await session.start()
        session.set_user_id(123)
        await session.save()
        await session.close()

        session2 = SQLiteSession("bot1", db_path=db_path)
        await session2.start()
        assert session2.get_user_id() == 123
        await session2.close()

    async def test_multi_session_single_db(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.session"
        s1 = SQLiteSession("bot_a", db_path=db_path)
        await s1.start()
        s1.set_user_id(111)
        s1.set_dc(2, "1.2.3.4", 443)
        await s1.save()

        s2 = SQLiteSession("bot_b", db_path=db_path)
        await s2.start()
        s2.set_user_id(222)
        await s2.save()

        assert s1.get_user_id() == 111
        assert s2.get_user_id() == 222

        await s1.close()
        await s2.close()

        # Re-open and verify both survive
        s3 = SQLiteSession("bot_a", db_path=db_path)
        await s3.start()
        assert s3.get_user_id() == 111
        s4 = SQLiteSession("bot_b", db_path=db_path)
        await s4.start()
        assert s4.get_user_id() == 222
        await s3.close()
        await s4.close()

    async def test_save_get_session(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.session"
        s = SQLiteSession("mgr", db_path=db_path)
        await s.start()

        await s.save_session("acct_x", {"user_id": 555, "dc_id": 3})
        result = await s.get_session("acct_x")
        assert result is not None
        assert result["user_id"] == 555
        assert result["dc_id"] == 3

        assert await s.get_session("nonexistent") is None
        await s.close()

    async def test_delete_session(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.session"
        s = SQLiteSession("mgr", db_path=db_path)
        await s.start()

        await s.save_session("del_me", {"user_id": 999})
        assert await s.delete_session("del_me") is True
        assert await s.get_session("del_me") is None
        assert await s.delete_session("del_me") is False
        await s.close()

    async def test_list_sessions(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.session"
        s = SQLiteSession("mgr", db_path=db_path)
        await s.start()

        await s.save_session("alpha", {"user_id": 1})
        await s.save_session("beta", {"user_id": 2})
        names = await s.list_sessions()
        assert "alpha" in names
        assert "beta" in names
        await s.close()

    async def test_auth_key_roundtrip(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.session"
        s = SQLiteSession("bk", db_path=db_path)
        await s.start()
        key = b"\x00\x01\x02\x03"
        s.set_auth_key(key)
        await s.save()
        await s.close()

        s2 = SQLiteSession("bk", db_path=db_path)
        await s2.start()
        assert s2.get_auth_key() == key
        await s2.close()

    async def test_dc_full_state(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.session"
        s = SQLiteSession("dc_test", db_path=db_path)
        await s.start()
        s.set_dc(2, "149.154.167.50", 443)
        await s.save()
        await s.close()

        s2 = SQLiteSession("dc_test", db_path=db_path)
        await s2.start()
        assert s2.get_dc() == 2
        state = s2.load()
        assert state["server_address"] == "149.154.167.50"
        assert state["port"] == 443
        await s2.close()
