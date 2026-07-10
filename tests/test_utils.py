"""Tests for utility modules."""

from __future__ import annotations

import pytest
from spluspy.utils.cache import LRUCache
from spluspy.utils.helpers import (
    sanitize_filename,
    truncate,
    chunk_list,
    generate_random_id,
)


class TestLRUCache:
    """Tests for the LRU cache."""

    @pytest.mark.asyncio
    async def test_set_get(self) -> None:
        cache = LRUCache[int, str](max_size=3)
        await cache.set(1, "a")
        await cache.set(2, "b")
        assert await cache.get(1) == "a"
        assert await cache.get(2) == "b"

    @pytest.mark.asyncio
    async def test_eviction(self) -> None:
        cache = LRUCache[int, str](max_size=2)
        await cache.set(1, "a")
        await cache.set(2, "b")
        await cache.set(3, "c")  # Should evict key 1
        assert await cache.get(1) is None
        assert await cache.get(2) == "b"
        assert await cache.get(3) == "c"

    @pytest.mark.asyncio
    async def test_lru_order(self) -> None:
        cache = LRUCache[int, str](max_size=2)
        await cache.set(1, "a")
        await cache.set(2, "b")
        await cache.get(1)  # Access key 1 to refresh it
        await cache.set(3, "c")  # Should evict key 2
        assert await cache.get(1) == "a"
        assert await cache.get(2) is None
        assert await cache.get(3) == "c"

    @pytest.mark.asyncio
    async def test_delete(self) -> None:
        cache = LRUCache[int, str](max_size=3)
        await cache.set(1, "a")
        assert await cache.delete(1) is True
        assert await cache.delete(1) is False
        assert await cache.get(1) is None

    @pytest.mark.asyncio
    async def test_clear(self) -> None:
        cache = LRUCache[int, str](max_size=3)
        await cache.set(1, "a")
        await cache.set(2, "b")
        await cache.clear()
        assert await cache.size() == 0

    @pytest.mark.asyncio
    async def test_stats(self) -> None:
        cache = LRUCache[int, str](max_size=3)
        await cache.set(1, "a")
        await cache.get(1)
        await cache.get(2)
        stats = cache.get_stats()
        assert stats["size"] == 1
        assert stats["hits"] == 1
        assert stats["misses"] == 1


class TestHelpers:
    """Tests for helper functions."""

    def test_sanitize_filename(self) -> None:
        # Input: test<>:"/\|?*file.txt (9 special chars → 9 underscores)
        assert sanitize_filename('test<>:"/\\|?*file.txt') == "test_________file.txt"
        assert sanitize_filename("normal.txt") == "normal.txt"

    def test_truncate(self) -> None:
        # truncate("hello", max_length=3) → "he" + "…" = "he…"
        assert truncate("hello", max_length=3) == "he\u2026"
        assert truncate("hi", max_length=5) == "hi"

    def test_chunk_list(self) -> None:
        assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
        assert chunk_list([], 3) == []

    def test_generate_random_id(self) -> None:
        id1 = generate_random_id()
        id2 = generate_random_id()
        assert id1 != id2
        assert isinstance(id1, int)
