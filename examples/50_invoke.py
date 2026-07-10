"""Example 50: Raw Invoke

Demonstrates raw API calls.
"""

from spluspy import Client
from spluspy import filters

bot = Client("invoke_session")


@bot.on_message(filters.command("raw"))
async def raw_handler(m):
    """Make a raw API call."""
    result = await m._client.invoke("some_method", key="value")
    await m.reply(f"Result: {result}")


if __name__ == "__main__":
    bot.run()
