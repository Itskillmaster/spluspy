"""Tests for the scheduler."""

from __future__ import annotations

import asyncio
import pytest
from spluspy.scheduler.scheduler import Scheduler


@pytest.mark.asyncio
class TestScheduler:
    """Tests for the Scheduler."""

    async def test_add_task(self) -> None:
        scheduler = Scheduler()
        called = []

        async def task() -> None:
            called.append(True)

        scheduler.add("test", task, interval=10)
        assert "test" in scheduler._tasks

    async def test_remove_task(self) -> None:
        scheduler = Scheduler()
        async def task() -> None:
            pass

        scheduler.add("test", task)
        assert scheduler.remove("test") is True
        assert scheduler.remove("test") is False

    async def test_start_stop(self) -> None:
        scheduler = Scheduler()
        async def task() -> None:
            pass

        scheduler.add("test", task, interval=10)
        await scheduler.start()
        assert scheduler.running is True
        await scheduler.stop()
        assert scheduler.running is False

    async def test_single_shot(self) -> None:
        scheduler = Scheduler()
        called = []

        async def task() -> None:
            called.append(True)

        scheduler.add("test", task, delay=0.01)
        await scheduler.start()
        await asyncio.sleep(0.1)
        await scheduler.stop()
        assert len(called) == 1

    async def test_max_runs(self) -> None:
        scheduler = Scheduler()
        called = []

        async def task() -> None:
            called.append(True)

        scheduler.add("test", task, interval=0.01, max_runs=3)
        await scheduler.start()
        await asyncio.sleep(0.2)
        await scheduler.stop()
        assert len(called) == 3
