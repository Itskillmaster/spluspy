"""Example 13: FSM Bot

Demonstrates the Finite State Machine for conversational flows.
"""

from spluspy import Client
from spluspy import filters
from spluspy.fsm import State, StateMachine
from spluspy.storage import MemoryStorage

bot = Client("fsm_session")
storage = MemoryStorage()
fsm = StateMachine(storage)


class RegistrationForm:
    """Form states."""

    name = State()
    age = State()
    city = State()


@bot.on_message(filters.command("register"))
async def start_registration(m):
    """Start the registration flow."""
    ctx = fsm.context(m.sender_id)
    await ctx.set_state(RegistrationForm.name)
    await m.reply("What is your name?")


@bot.on_message(filters.private)
async def process_form(m):
    """Process form responses based on current state."""
    ctx = fsm.context(m.sender_id)
    state = await ctx.get_state()

    if state is None:
        return

    if state == RegistrationForm.name:
        await ctx.set_data(name=m.text)
        await ctx.set_state(RegistrationForm.age)
        await m.reply("How old are you?")

    elif state == RegistrationForm.age:
        await ctx.set_data(age=m.text)
        await ctx.set_state(RegistrationForm.city)
        await m.reply("Which city are you from?")

    elif state == RegistrationForm.city:
        data = await ctx.get_data()
        await ctx.reset()
        await m.reply(
            f"Registration complete!\n"
            f"Name: {data.get('name')}\n"
            f"Age: {data.get('age')}\n"
            f"City: {m.text}"
        )


if __name__ == "__main__":
    bot.run()
