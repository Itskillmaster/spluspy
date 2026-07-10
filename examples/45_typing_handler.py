"""Example 45: Typing Handler

Handles typing indicators.
"""

from spluspy import Client

bot = Client("typing_session")


@bot.on_typing()
async def typing_handler(update):
    """Handle typing indicators."""
    print(f"User {update.user_id} is typing...")


if __name__ == "__main__":
    bot.run()
