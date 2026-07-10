"""Example 14: Plugin Bot

Demonstrates the plugin loading system.
"""

# plugins/greetings.py
"""Greeting plugin."""

GREETINGS = {
    "hello": "Hello there!",
    "hi": "Hey!",
    "salam": "Salam! How are you?",
    "bye": "Goodbye! Have a great day!",
}


def register(client):
    """Register plugin handlers with the client."""

    @client.on_message(filters.command("greet"))
    async def greet_handler(m):
        await m.reply("Available greetings: hello, hi, salam, bye")

    @client.on_message(filters.text)
    async def auto_greet(m):
        text = m.text.lower().strip()
        if text in GREETINGS:
            await m.reply(GREETINGS[text])


# main.py
from spluspy import Client

bot = Client("plugin_session")
bot.plugins.load("plugins")
bot.run()
