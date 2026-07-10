"""Example 29: Dice Bot

Demonstrates sending dice animations.
"""

from spluspy import Client
from spluspy import filters

bot = Client("dice_session")


@bot.on_message(filters.command("dice"))
async def dice_handler(m):
    """Send a dice."""
    await m._client.send_dice(m.chat_id, emoji="🎲")


@bot.on_message(filters.command("darts"))
async def darts_handler(m):
    """Send darts."""
    await m._client.send_dice(m.chat_id, emoji="🎯")


@bot.on_message(filters.command("basketball"))
async def basketball_handler(m):
    """Send basketball."""
    await m._client.send_dice(m.chat_id, emoji="🏀")


if __name__ == "__main__":
    bot.run()
