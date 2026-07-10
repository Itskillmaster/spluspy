"""Tests for storage backends."""

import pytest
from spluspy.storage.memory import MemoryStorage


@pytest.fixture
def memory_storage():
    return MemoryStorage()


class TestMemoryStorage:
    @pytest.mark.asyncio
    async def test_set_get(self, memory_storage):
        await memory_storage.set("key", "value")
        assert await memory_storage.get("key") == "value"

    @pytest.mark.asyncio
    async def test_get_nonexistent(self, memory_storage):
        assert await memory_storage.get("missing") is None

    @pytest.mark.asyncio
    async def test_delete(self, memory_storage):
        await memory_storage.set("key", "value")
        assert await memory_storage.delete("key") is True
        assert await memory_storage.get("key") is None

    @pytest.mark.asyncio
    async def test_delete_nonexistent(self, memory_storage):
        assert await memory_storage.delete("missing") is False

    @pytest.mark.asyncio
    async def test_exists(self, memory_storage):
        await memory_storage.set("key", "value")
        assert await memory_storage.exists("key") is True
        assert await memory_storage.exists("missing") is False

    @pytest.mark.asyncio
    async def test_clear(self, memory_storage):
        await memory_storage.set("a", 1)
        await memory_storage.set("b", 2)
        await memory_storage.clear()
        assert await memory_storage.get("a") is None
        assert await memory_storage.get("b") is None

    @pytest.mark.asyncio
    async def test_ttl(self, memory_storage):
        await memory_storage.set("key", "value", ttl=0)
        # With ttl=0, the item expires at current time, so sleep briefly
        import asyncio
        await asyncio.sleep(0.05)
        assert await memory_storage.get("key") is None
