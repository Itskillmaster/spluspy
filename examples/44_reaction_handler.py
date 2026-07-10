"""Example 44: Reaction Handler

Handles reactions on messages.
"""

from spluspy import Client

bot = Client("reaction_handler_session")


@bot.on_reaction()
async def reaction_handler(m):
    """Handle reactions."""
    print(f"Reaction received on message {m.id}")


if __name__ == "__main__":
    bot.run()
