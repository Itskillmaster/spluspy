"""Example 5: Group Chat Only

Only responds to messages in group chats.
"""

from spluspy import Client
from spluspy import filters

bot = Client("group_session")


@bot.on_message(filters.group)
async def group_handler(m):
    """Handle messages in group chats only."""
    await m.reply("This is a group chat!")


if __name__ == "__main__":
    bot.run()
