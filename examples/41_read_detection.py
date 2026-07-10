"""Example 41: Read Detection

Detects when messages are read.
"""

from spluspy import Client

bot = Client("read_detection_session")


@bot.on_message_read()
async def read_handler(update):
    """Handle read receipts."""
    print(f"Messages read in chat {update.chat_id}")
    print(f"Max read ID: {update.max_id}")


if __name__ == "__main__":
    bot.run()
