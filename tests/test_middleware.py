"""Tests for the middleware system."""

from __future__ import annotations

import pytest
from spluspy.middleware.base import Middleware, MiddlewareManager


class CountingMiddleware(Middleware):
    """Test middleware that counts invocations."""

    def __init__(self) -> None:
        self.call_count = 0

    async def on_update(self, update: object, handler: object) -> object:
        self.call_count += 1
        return await handler(update)  # type: ignore[misc]


class TestMiddlewareManager:
    """Tests for the MiddlewareManager."""

    @pytest.mark.asyncio
    async def test_execute_single(self) -> None:
        manager = MiddlewareManager()
        mw = CountingMiddleware()
        manager.add(mw)

        async def final(update: object) -> str:
            return "done"

        result = await manager.execute("test", final)
        assert result == "done"
        assert mw.call_count == 1

    @pytest.mark.asyncio
    async def test_execute_chain(self) -> None:
        manager = MiddlewareManager()
        mw1 = CountingMiddleware()
        mw2 = CountingMiddleware()
        manager.add(mw1)
        manager.add(mw2)

        async def final(update: object) -> str:
            return "done"

        result = await manager.execute("test", final)
        assert result == "done"
        assert mw1.call_count == 1
        assert mw2.call_count == 1

    @pytest.mark.asyncio
    async def test_startup_shutdown(self) -> None:
        manager = MiddlewareManager()
        mw = CountingMiddleware()
        manager.add(mw)

        await manager.startup()
        await manager.shutdown()
        # No error should occur

    def test_remove(self) -> None:
        manager = MiddlewareManager()
        mw = CountingMiddleware()
        manager.add(mw)
        manager.remove(mw)
        assert len(manager._middleware) == 0
