"""Example 35: Chat Info Bot

Shows chat information.
"""

from spluspy import Client
from spluspy import filters

bot = Client("chatinfo_session")


@bot.on_message(filters.command("chatinfo"))
async def chatinfo_handler(m):
    """Show chat info."""
    await m.reply(
        f"Chat ID: {m.chat_id}\n"
        f"Is Group: {m.is_group}\n"
        f"Is Channel: {m.is_channel}\n"
        f"Is Private: {m.is_private}"
    )


if __name__ == "__main__":
    bot.run()
