"""Example 27: Search Messages

Demonstrates searching for messages.
"""

from spluspy import Client
from spluspy import filters

bot = Client("search_session")


@bot.on_message(filters.command("search"))
async def search_handler(m):
    """Search for messages containing a keyword."""
    query = m.text.replace("/search ", "").strip()
    if not query:
        await m.reply("Usage: /search <keyword>")
        return

    messages = await m._client.search_messages(m.chat_id, query, limit=5)
    if messages:
        for msg in messages:
            await m.reply(f"Found: {msg.text}")
    else:
        await m.reply("No messages found.")


if __name__ == "__main__":
    bot.run()
