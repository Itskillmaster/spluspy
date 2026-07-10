"""Example 31: Reaction Bot

Automatically reacts to messages.
"""

from spluspy import Client
from spluspy import filters

bot = Client("reaction_session")


@bot.on_message(filters.command("love"))
async def love_handler(m):
    await m.react("❤️")
    await m.reply("Reacted with love!")


@bot.on_message(filters.command("thumbsup"))
async def thumbsup_handler(m):
    await m.react("👍")
    await m.reply("Thumbs up!")


@bot.on_message(filters.command("fire"))
async def fire_handler(m):
    await m.react("🔥")
    await m.reply("Fire!")


if __name__ == "__main__":
    bot.run()
