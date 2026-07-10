"""Example 10: Reply Keyboard Bot

Demonstrates reply keyboards (replacing the user's keyboard).
"""

from spluspy import Client
from spluspy import Button, filters

bot = Client("reply_keyboard_session")


@bot.on_message(filters.command("menu"))
async def menu_handler(m):
    """Show a reply keyboard."""
    keyboard = Button.build_reply(
        [Button.text("Settings"), Button.text("Profile")],
        [Button.text("Help")],
    )
    await m.reply("Choose:", buttons=keyboard)


@bot.on_message(filters.command("clear"))
async def clear_handler(m):
    """Clear the keyboard."""
    await m.reply("Keyboard cleared!", buttons=Button.clear())


@bot.on_message(filters.text)
async def text_handler(m):
    """Handle text messages."""
    await m.reply(f"You pressed: {m.text}")


if __name__ == "__main__":
    bot.run()
