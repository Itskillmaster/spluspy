"""Example 2: Echo Bot

Echoes back any text message it receives.
"""

from spluspy import Client, filters

bot = Client(session_name="echo_session")


@bot.on_message(filters.text)
async def echo_handler(client, message):
    """Echo the received message."""
    await message.reply(f"You said: {message.text}")


if __name__ == "__main__":
    bot.run()
