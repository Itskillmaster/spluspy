"""Example 39: Status Bot

Shows user online/offline status changes.
"""

from spluspy import Client

bot = Client("status_session")


@bot.on_user_update()
async def status_handler(update):
    """Handle user status changes."""
    if update.is_online:
        print(f"User {update.user_id} is now online")
    elif update.is_offline:
        print(f"User {update.user_id} is now offline")


if __name__ == "__main__":
    bot.run()
