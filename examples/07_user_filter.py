"""Example 7: User Filter

Responds only to specific users.
"""

from spluspy import Client
from spluspy import filters

bot = Client("user_filter_session")

# Replace with actual user IDs
ALLOWED_USERS = [123456, 789012]


@bot.on_message(filters.user(*ALLOWED_USERS))
async def allowed_handler(m):
    """Handle messages from allowed users only."""
    await m.reply("Hello authorized user!")


@bot.on_message()
async def unauthorized_handler(m):
    """Handle messages from unauthorized users."""
    await m.reply("Sorry, you are not authorized.")


if __name__ == "__main__":
    bot.run()
