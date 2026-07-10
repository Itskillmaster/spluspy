"""Example 17: Conversation Bot

Demonstrates the conversation API for interactive flows.
"""

from spluspy import Client
from spluspy.client.conversation import Conversation

bot = Client("conversation_session")


@bot.on_message(filters.command("quiz"))
async def quiz_handler(m):
    """Start a quiz conversation."""
    async with bot.client.conversation(m.chat_id, timeout=30) as conv:
        conv.send_message("What is 2 + 2?")
        response = await conv.get_response()

        if response.text == "4":
            conv.send_message("Correct!")
        else:
            conv.send_message(f"Wrong! The answer is 4.")


if __name__ == "__main__":
    bot.run()
