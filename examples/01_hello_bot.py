"""Example 1: Hello World Bot

The simplest possible SplusPy bot that replies "Hello!" to any message.
"""

from spluspy import Client

# Use session_name for clarity
bot = Client(session_name="hello_session")


@bot.on_message()
async def hello_handler(client, message):
    """Reply to every message with 'Hello!'."""
    await message.reply("Hello!")


if __name__ == "__main__":
    bot.run()
