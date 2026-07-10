"""Example 18: Chat Management Bot

Demonstrates chat management operations.
"""

from spluspy import Client
from spluspy import filters

bot = Client("chat_mgmt_session")


@bot.on_message(filters.command("ban"))
async def ban_handler(m):
    """Ban a user (reply to their message)."""
    if m.reply_to:
        await m._client.ban_user(m.chat_id, m.reply_to)
        await m.reply("User banned!")
    else:
        await m.reply("Reply to a user's message to ban them.")


@bot.on_message(filters.command("unban"))
async def unban_handler(m):
    """Unban a user."""
    if m.reply_to:
        await m._client.unban_user(m.chat_id, m.reply_to)
        await m.reply("User unbanned!")
    else:
        await m.reply("Reply to a user's message to unban them.")


@bot.on_message(filters.command("pin"))
async def pin_handler(m):
    """Pin a message."""
    if m.reply_to:
        await m._client.pin_message(m.chat_id, m.reply_to, notify=True)
        await m.reply("Message pinned!")
    else:
        await m.reply("Reply to a message to pin it.")


@bot.on_message(filters.command("info"))
async def info_handler(m):
    """Get chat info."""
    await m.reply(f"Chat ID: {m.chat_id}\nYour ID: {m.sender_id}")


if __name__ == "__main__":
    bot.run()
