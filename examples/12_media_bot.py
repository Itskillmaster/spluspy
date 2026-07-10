"""Example 12: Media Bot

Demonstrates sending different types of media.
"""

from spluspy import Client
from spluspy import filters

bot = Client("media_session")


@bot.on_message(filters.command("photo"))
async def photo_example(m):
    """Send a photo."""
    await m.reply_photo("https://example.com/photo.jpg", caption="Here is a photo!")


@bot.on_message(filters.command("video"))
async def video_example(m):
    """Send a video."""
    await m.reply_video("https://example.com/video.mp4", caption="Here is a video!")


@bot.on_message(filters.command("document"))
async def document_example(m):
    """Send a document."""
    await m.reply_document("https://example.com/file.pdf", caption="Here is a document!")


@bot.on_message(filters.command("location"))
async def location_example(m):
    """Send a location."""
    await m.reply("Sending location...")
    # await m._client.send_location(m.chat_id, 35.6892, 51.3890)


if __name__ == "__main__":
    bot.run()
