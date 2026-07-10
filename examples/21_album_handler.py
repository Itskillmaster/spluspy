"""Example 21: Album Handler

Handles grouped media (albums).
"""

from spluspy import Client

bot = Client("album_session")


@bot.on_album()
async def album_handler(album):
    """Handle album messages."""
    count = album.total
    await album.messages[0].reply(f"Received album with {count} items!")


if __name__ == "__main__":
    bot.run()
