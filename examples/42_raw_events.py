"""Example 42: Raw Events

Demonstrates handling raw updates.
"""

from spluspy import Client

bot = Client("raw_session")


@bot.on_raw()
async def raw_handler(update):
    """Handle raw updates."""
    print(f"Raw update: {update}")


if __name__ == "__main__":
    bot.run()
