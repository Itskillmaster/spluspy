"""Example 40: Delete Detection

Detects when messages are deleted.
"""

from spluspy import Client

bot = Client("delete_session")


@bot.on_message_deleted()
async def deleted_handler(update):
    """Handle deleted messages."""
    print(f"Messages deleted: {update.deleted_ids}")
    print(f"Chat: {update.chat_id}")


if __name__ == "__main__":
    bot.run()
