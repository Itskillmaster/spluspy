"""Example 22: Download Bot

Downloads media sent to the bot.
"""

from spluspy import Client
from spluspy import filters

bot = Client("download_session")


@bot.on_message(filters.command("save"))
async def save_handler(m):
    """Save the replied-to message's media."""
    if m.reply_to_message and m.reply_to_message.is_media:
        file_path = await m.reply_to_message.download()
        if file_path:
            await m.reply(f"Saved to: {file_path}")
        else:
            await m.reply("Failed to download.")
    else:
        await m.reply("Reply to a media message to save it.")


if __name__ == "__main__":
    bot.run()
