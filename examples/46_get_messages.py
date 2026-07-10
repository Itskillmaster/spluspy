"""Example 46: Get Messages

Demonstrates fetching message history.
"""

from spluspy import Client
from spluspy import filters

bot = Client("get_messages_session")


@bot.on_message(filters.command("history"))
async def history_handler(m):
    """Get recent message history."""
    messages = await m._client.get_messages(m.chat_id, limit=5)
    for msg in messages:
        await m.reply(f"ID: {msg.id}, Text: {msg.text}")


@bot.on_message(filters.command("search"))
async def search_handler(m):
    """Search messages."""
    query = m.text.replace("/search ", "")
    messages = await m._client.search_messages(m.chat_id, query, limit=5)
    for msg in messages:
        await m.reply(f"Found: {msg.text}")


if __name__ == "__main__":
    bot.run()
