"""Example 38: Media Filters

Demonstrates filtering by media type.
"""

from spluspy import Client
from spluspy import filters

bot = Client("media_filter_session")


@bot.on_message(filters.photo)
async def photo_handler(m):
    await m.reply("Nice photo!")


@bot.on_message(filters.video)
async def video_handler(m):
    await m.reply("Nice video!")


@bot.on_message(filters.audio)
async def audio_handler(m):
    await m.reply("Nice audio!")


@bot.on_message(filters.voice)
async def voice_handler(m):
    await m.reply("Nice voice message!")


@bot.on_message(filters.media)
async def any_media_handler(m):
    await m.reply("Got some media!")


if __name__ == "__main__":
    bot.run()
