"""Example 20: Sync Bot

Demonstrates the synchronous client (no async/await needed).
"""

from spluspy.sync import Client
from spluspy import filters

bot = Client("sync_session")


@bot.on_message()
def handler(m):
    """Handle messages synchronously."""
    m.reply("Hello from sync bot!")


@bot.on_message(filters.command("ping"))
def ping_handler(m):
    """Respond to /ping."""
    m.reply("Pong!")


if __name__ == "__main__":
    bot.run()
