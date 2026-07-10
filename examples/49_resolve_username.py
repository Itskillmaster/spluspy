"""Example 49: Resolve Username

Demonstrates resolving usernames to IDs.
"""

from spluspy import Client
from spluspy import filters

bot = Client("resolve_session")


@bot.on_message(filters.command("resolve"))
async def resolve_handler(m):
    """Resolve a username to an ID."""
    username = m.text.replace("/resolve ", "").strip().lstrip("@")
    if not username:
        await m.reply("Usage: /resolve @username")
        return
    user_id = await m._client.resolve_username(username)
    await m.reply(f"User ID: {user_id}")


if __name__ == "__main__":
    bot.run()
