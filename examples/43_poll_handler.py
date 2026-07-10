"""Example 43: Poll Handler

Handles incoming polls.
"""

from spluspy import Client

bot = Client("poll_handler_session")


@bot.on_poll()
async def poll_handler(m):
    """Handle incoming polls."""
    if m.media and hasattr(m.media, "question"):
        await m.reply(f"Poll: {m.media.question}")


if __name__ == "__main__":
    bot.run()
