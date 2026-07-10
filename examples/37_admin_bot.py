"""Example 37: Admin Bot

Demonstrates admin management operations.
"""

from spluspy import Client
from spluspy import filters

bot = Client("admin_session")


@bot.on_message(filters.command("ban"))
async def ban_handler(m):
    """Ban a user."""
    if m.reply_to and m.reply_to_message:
        await m._client.ban_user(m.chat_id, m.reply_to_message.sender_id)
        await m.reply("User banned!")
    else:
        await m.reply("Reply to a user's message to ban them.")


@bot.on_message(filters.command("unban"))
async def unban_handler(m):
    """Unban a user."""
    if m.reply_to and m.reply_to_message:
        await m._client.unban_user(m.chat_id, m.reply_to_message.sender_id)
        await m.reply("User unbanned!")
    else:
        await m.reply("Reply to a user's message to unban them.")


@bot.on_message(filters.command("mute"))
async def mute_handler(m):
    """Mute a user."""
    if m.reply_to and m.reply_to_message:
        await m._client.mute_user(m.chat_id, m.reply_to_message.sender_id)
        await m.reply("User muted!")
    else:
        await m.reply("Reply to a user's message to mute them.")


@bot.on_message(filters.command("unmute"))
async def unmute_handler(m):
    """Unmute a user."""
    if m.reply_to and m.reply_to_message:
        await m._client.unmute_user(m.chat_id, m.reply_to_message.sender_id)
        await m.reply("User unmuted!")
    else:
        await m.reply("Reply to a user's message to unmute them.")


if __name__ == "__main__":
    bot.run()
