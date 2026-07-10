"""Example 23: URL Button

Demonstrates URL buttons in inline keyboards.
"""

from spluspy import Client
from spluspy import Button

bot = Client("url_button_session")


@bot.on_message(filters.command("links"))
async def links_handler(m):
    """Show a keyboard with URL buttons."""
    keyboard = Button.build_inline(
        [
            [Button.url("GitHub", "https://github.com")],
            [Button.url("Soroush Plus", "https://web.splus.ir")],
        ]
    )
    await m.reply("Useful links:", buttons=keyboard)


if __name__ == "__main__":
    bot.run()
