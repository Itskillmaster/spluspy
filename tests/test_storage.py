"""Tests for storage backends."""

from __future__ import annotations

import pytest
from spluspy.storage.memory import MemoryStorage
from spluspy.storage.sqlite import SQLiteStorage


@pytest.mark.asyncio
class TestMemoryStorage:
    """Tests for the in-memory storage backend."""

    async def test_set_get(self) -> None:
        storage = MemoryStorage()
        await storage.set("key", "value")
        assert await storage.get("key") == "value"

    async def test_get_missing(self) -> None:
        storage = MemoryStorage()
        assert await storage.get("missing") is None

    async def test_delete(self) -> None:
        storage = MemoryStorage()
        await storage.set("key", "value")
        assert await storage.delete("key") is True
        assert await storage.delete("key") is False

    async def test_exists(self) -> None:
        storage = MemoryStorage()
        assert await storage.exists("key") is False
        await storage.set("key", "value")
        assert await storage.exists("key") is True

    async def test_clear(self) -> None:
        storage = MemoryStorage()
        await storage.set("a", 1)
        await storage.set("b", 2)
        await storage.clear()
        assert await storage.get("a") is None
        assert await storage.get("b") is None


@pytest.mark.asyncio
class TestSQLiteStorage:
    """Tests for the SQLite storage backend."""

    async def test_set_get(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.db"  # type: ignore[operator]
        async with SQLiteStorage(db_path) as storage:
            await storage.set("key", "value")
            assert await storage.get("key") == "value"

    async def test_persistence(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.db"  # type: ignore[operator]
        async with SQLiteStorage(db_path) as storage:
            await storage.set("key", "value")
        async with SQLiteStorage(db_path) as storage:
            assert await storage.get("key") == "value"

    async def test_delete(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.db"  # type: ignore[operator]
        async with SQLiteStorage(db_path) as storage:
            await storage.set("key", "value")
            assert await storage.delete("key") is True
            assert await storage.delete("key") is False

    async def test_exists(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.db"  # type: ignore[operator]
        async with SQLiteStorage(db_path) as storage:
            assert await storage.exists("key") is False
            await storage.set("key", "value")
            assert await storage.exists("key") is True

    async def test_clear(self, tmp_path: object) -> None:
        db_path = str(tmp_path) + "/test.db"  # type: ignore[operator]
        async with SQLiteStorage(db_path) as storage:
            await storage.set("a", 1)
            await storage.set("b", 2)
            await storage.clear()
            assert await storage.get("a") is None
            assert await storage.get("b") is None
