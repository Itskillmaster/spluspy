"""Example 36: Forward and Copy

Demonstrates forwarding and copying messages.
"""

from spluspy import Client
from spluspy import filters

bot = Client("forward_session")


@bot.on_message(filters.command("copy"))
async def copy_handler(m):
    """Copy the replied message."""
    if m.reply_to_message:
        await m.reply_to_message.copy(m.chat_id)
        await m.reply("Message copied!")
    else:
        await m.reply("Reply to a message to copy it.")


@bot.on_message(filters.command("forward"))
async def forward_handler(m):
    """Forward the replied message."""
    if m.reply_to_message:
        await m.reply_to_message.forward(m.chat_id)
        await m.reply("Message forwarded!")
    else:
        await m.reply("Reply to a message to forward it.")


if __name__ == "__main__":
    bot.run()
