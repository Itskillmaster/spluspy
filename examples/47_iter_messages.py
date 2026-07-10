"""Example 47: Iter Messages

Demonstrates iterating over messages.
"""

from spluspy import Client
from spluspy import filters

bot = Client("iter_messages_session")


@bot.on_message(filters.command("iterate"))
async def iterate_handler(m):
    """Iterate over messages."""
    count = 0
    async for msg in m._client.iter_messages(m.chat_id, limit=10):
        count += 1
    await m.reply(f"Iterated over {count} messages!")


if __name__ == "__main__":
    bot.run()
