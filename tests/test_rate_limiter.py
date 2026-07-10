"""Tests for rate limiter."""

import asyncio
import time
import pytest
from spluspy.utils.rate_limiter import RateLimiter, TokenBucket, FloodWaitError


class TestTokenBucket:
    @pytest.mark.asyncio
    async def test_acquire(self):
        bucket = TokenBucket(rate=10, capacity=10)
        assert await bucket.acquire() is True

    @pytest.mark.asyncio
    async def test_acquire_nonblocking(self):
        bucket = TokenBucket(rate=0.1, capacity=1)
        await bucket.acquire()
        result = await bucket.acquire(blocking=False)
        assert result is False

    @pytest.mark.asyncio
    async def test_refill(self):
        bucket = TokenBucket(rate=100, capacity=10)
        for _ in range(10):
            await bucket.acquire()
        await asyncio.sleep(0.1)
        assert await bucket.acquire() is True


class TestRateLimiter:
    @pytest.mark.asyncio
    async def test_acquire(self):
        limiter = RateLimiter(default_rate=10, default_capacity=10)
        await limiter.acquire("test_method")

    @pytest.mark.asyncio
    async def test_flood_wait(self):
        limiter = RateLimiter(default_rate=10, default_capacity=10, flood_sleep_threshold=1)
        limiter.register_flood_wait("test_method", 60)
        with pytest.raises(FloodWaitError):
            await limiter.acquire("test_method")

    @pytest.mark.asyncio
    async def test_flood_wait_short(self):
        limiter = RateLimiter(default_rate=10, default_capacity=10, flood_sleep_threshold=60)
        limiter.register_flood_wait("test_method", 1)
        await limiter.acquire("test_method")

    def test_decorator(self):
        limiter = RateLimiter(default_rate=10, default_capacity=10)

        @limiter.limit("test")
        async def my_func():
            return 42

        assert asyncio.iscoroutinefunction(my_func)

    def test_clear_flood_wait(self):
        limiter = RateLimiter()
        limiter.register_flood_wait("test", 60)
        limiter.clear_flood_wait("test")
        assert limiter.get_wait_time("test") == 0.0
