"""Example 32: Mark Read Bot

Demonstrates marking messages as read.
"""

from spluspy import Client
from spluspy import filters

bot = Client("read_session")


@bot.on_message(filters.command("read"))
async def read_handler(m):
    """Mark the current message as read."""
    await m.mark_read()
    await m.reply("Marked as read!")


@bot.on_message(filters.command("readall"))
async def readall_handler(m):
    """Mark all messages in chat as read."""
    await m._client.mark_read(m.chat_id)
    await m.reply("All messages marked as read!")


if __name__ == "__main__":
    bot.run()
