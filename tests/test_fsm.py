"""Tests for the FSM module."""

from __future__ import annotations

import pytest
from spluspy.fsm.state import State, StateMachine, FSMContext
from spluspy.storage.memory import MemoryStorage


class TestState:
    """Tests for the State class."""

    def test_state_creation(self) -> None:
        state = State("name")
        assert state.name == "name"

    def test_state_equality(self) -> None:
        s1 = State("same")
        s2 = State("same")
        s3 = State("different")
        assert s1 == s2
        assert s1 != s3

    def test_state_hash(self) -> None:
        s1 = State("test")
        s2 = State("test")
        assert hash(s1) == hash(s2)


class TestFSMContext:
    """Tests for FSMContext."""

    @pytest.mark.asyncio
    async def test_set_get_state(self) -> None:
        storage = MemoryStorage()
        ctx = FSMContext(storage, user_id=1)
        state = State("form.name")
        await ctx.set_state(state)
        current = await ctx.get_state()
        assert current is not None
        assert current.name == "form.name"

    @pytest.mark.asyncio
    async def test_get_state_empty(self) -> None:
        storage = MemoryStorage()
        ctx = FSMContext(storage, user_id=1)
        current = await ctx.get_state()
        assert current is None

    @pytest.mark.asyncio
    async def test_set_get_data(self) -> None:
        storage = MemoryStorage()
        ctx = FSMContext(storage, user_id=1)
        await ctx.set_data(name="Ali", age=25)
        data = await ctx.get_data()
        assert data["name"] == "Ali"
        assert data["age"] == 25

    @pytest.mark.asyncio
    async def test_reset(self) -> None:
        storage = MemoryStorage()
        ctx = FSMContext(storage, user_id=1)
        await ctx.set_state(State("test"))
        await ctx.set_data(name="test")
        await ctx.reset()
        assert await ctx.get_state() is None
        assert await ctx.get_data() == {}


class TestStateMachine:
    """Tests for StateMachine."""

    @pytest.mark.asyncio
    async def test_context_creation(self) -> None:
        storage = MemoryStorage()
        sm = StateMachine(storage)
        ctx = sm.context(user_id=1)
        assert isinstance(ctx, FSMContext)

    @pytest.mark.asyncio
    async def test_isolated_users(self) -> None:
        storage = MemoryStorage()
        sm = StateMachine(storage)
        ctx1 = sm.context(user_id=1)
        ctx2 = sm.context(user_id=2)
        await ctx1.set_state(State("state1"))
        await ctx2.set_state(State("state2"))
        s1 = await ctx1.get_state()
        s2 = await ctx2.get_state()
        assert s1 is not None
        assert s2 is not None
        assert s1.name != s2.name
