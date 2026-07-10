"""Tests for enhanced FSM."""

import pytest
from spluspy.fsm import State, StateMachine, FSMContext
from spluspy.storage.memory import MemoryStorage


class Form:
    name = State()
    age = State()


@pytest.fixture
def fsm():
    storage = MemoryStorage()
    return StateMachine(storage)


class TestStateMachine:
    @pytest.mark.asyncio
    async def test_context_creation(self, fsm):
        ctx = fsm.context(user_id=123)
        assert isinstance(ctx, FSMContext)
        assert ctx.user_id == 123

    @pytest.mark.asyncio
    async def test_set_get_state(self, fsm):
        ctx = fsm.context(user_id=123)
        await ctx.set_state(Form.name)
        state = await ctx.get_state()
        assert state == Form.name

    @pytest.mark.asyncio
    async def test_state_data(self, fsm):
        ctx = fsm.context(user_id=123)
        await ctx.set_data(name="Ali", age=25)
        data = await ctx.get_data()
        assert data["name"] == "Ali"
        assert data["age"] == 25

    @pytest.mark.asyncio
    async def test_state_get_set_single(self, fsm):
        ctx = fsm.context(user_id=123)
        await ctx.set("name", "Ali")
        assert await ctx.get("name") == "Ali"
        assert await ctx.get("missing", "default") == "default"

    @pytest.mark.asyncio
    async def test_reset(self, fsm):
        ctx = fsm.context(user_id=123)
        await ctx.set_state(Form.name)
        await ctx.set_data(name="Ali")
        await ctx.reset()
        assert await ctx.get_state() is None
        assert await ctx.get_data() == {}

    @pytest.mark.asyncio
    async def test_finish(self, fsm):
        ctx = fsm.context(user_id=123)
        await ctx.set_state(Form.name)
        await ctx.finish()
        assert await ctx.get_state() is None

    @pytest.mark.asyncio
    async def test_handler_registration(self, fsm):
        @fsm.state(Form.name)
        async def handle_name(m):
            pass

        assert Form.name.name in fsm._handlers

    @pytest.mark.asyncio
    async def test_handler_routing(self, fsm):
        results = []

        @fsm.state(Form.name)
        async def handle_name(m):
            results.append("name")

        @fsm.state(Form.age)
        async def handle_age(m):
            results.append("age")

        ctx = fsm.context(user_id=123)
        await ctx.set_state(Form.name)

        handled = await fsm.handle("update", user_id=123)
        assert handled is True
        assert results == ["name"]

    @pytest.mark.asyncio
    async def test_fallback_handler(self, fsm):
        results = []

        # Create a state with no handler registered
        orphan_state = State("orphan")

        @fsm.fallback()
        async def handle_fallback(m):
            results.append("fallback")

        ctx = fsm.context(user_id=123)
        await ctx.set_state(orphan_state)

        await fsm.handle("update", user_id=123)
        assert results == ["fallback"]
