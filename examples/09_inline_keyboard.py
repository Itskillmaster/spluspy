"""Example 9: Inline Keyboard Bot

Demonstrates inline keyboard buttons and callback queries.
"""

from spluspy import Client
from spluspy import Button, filters

bot = Client("keyboard_session")


@bot.on_message(filters.command("menu"))
async def menu_handler(m):
    """Show an inline keyboard menu."""
    keyboard = Button.build_inline(
        [
            [Button.inline("Option 1", b"opt1"), Button.inline("Option 2", b"opt2")],
            [Button.inline("Option 3", b"opt3")],
        ]
    )
    await m.reply("Choose an option:", buttons=keyboard)


@bot.on_callback_query()
async def callback_handler(cb):
    """Handle inline button clicks."""
    data = cb.text
    if data == "opt1":
        await cb.answer("You chose Option 1!")
    elif data == "opt2":
        await cb.answer("You chose Option 2!")
    elif data == "opt3":
        await cb.answer("You chose Option 3!")


if __name__ == "__main__":
    bot.run()
