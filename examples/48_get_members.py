"""Example 48: Get Members

Demonstrates fetching chat members.
"""

from spluspy import Client
from spluspy import filters

bot = Client("get_members_session")


@bot.on_message(filters.command("members"))
async def members_handler(m):
    """Get chat members."""
    members = await m._client.get_members(m.chat_id, limit=10)
    for member in members:
        await m.reply(f"Member: {member}")


if __name__ == "__main__":
    bot.run()
