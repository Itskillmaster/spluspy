"""Example 28: Poll Bot

Demonstrates creating polls.
"""

from spluspy import Client
from spluspy import filters

bot = Client("poll_session")


@bot.on_message(filters.command("poll"))
async def poll_handler(m):
    """Create a poll."""
    await m._client.send_poll(
        m.chat_id,
        question="What is your favorite programming language?",
        options=["Python", "JavaScript", "Rust", "Go"],
        is_anonymous=True,
    )


if __name__ == "__main__":
    bot.run()
