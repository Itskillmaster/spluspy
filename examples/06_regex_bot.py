"""Example 6: Regex Bot

Matches messages using regex patterns.
"""

from spluspy import Client
from spluspy import filters

bot = Client("regex_session")


@bot.on_message(filters.regex(r"\d+"))
async def number_handler(m):
    """Handle messages containing numbers."""
    numbers = m.pattern_match.group()
    await m.reply(f"I found a number: {numbers}")


@bot.on_message(filters.regex(r"(?i)hello|hi|hey"))
async def greeting_handler(m):
    """Handle greeting messages."""
    await m.reply("Hey there!")


if __name__ == "__main__":
    bot.run()
