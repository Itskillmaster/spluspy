"""Example 34: User Info Bot

Shows user information.
"""

from spluspy import Client
from spluspy import filters

bot = Client("userinfo_session")


@bot.on_message(filters.command("whoami"))
async def whoami_handler(m):
    """Show current user info."""
    await m.reply(
        f"Your ID: {m.sender_id}\n"
        f"Name: {m.sender.full_name if m.sender else 'Unknown'}\n"
        f"Username: @{m.sender.username if m.sender and m.sender.username else 'None'}"
    )


if __name__ == "__main__":
    bot.run()
