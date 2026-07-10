"""Example 4: Private Chat Only

Only responds to messages in private chats.
"""

from spluspy import Client
from spluspy import filters

bot = Client("private_session")


@bot.on_message(filters.private)
async def private_handler(m):
    """Handle messages in private chats only."""
    await m.reply("This is a private chat!")


if __name__ == "__main__":
    bot.run()
