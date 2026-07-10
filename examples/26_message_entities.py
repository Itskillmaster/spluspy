"""Example 26: Message Entities

Demonstrates working with message entities (formatting).
"""

from spluspy import Client
from spluspy import filters

bot = Client("entities_session")


@bot.on_message(filters.command("format"))
async def format_handler(m):
    """Show formatted text."""
    # Using HTML
    await m.reply(
        "<b>Bold</b>, <i>Italic</i>, <code>Code</code>",
        parse_mode="html",
    )


@bot.on_message(filters.command("entities"))
async def entities_handler(m):
    """Show message entities."""
    if m.entities:
        for entity in m.entities:
            await m.reply(f"Entity: {entity.type} at {entity.offset}")
    else:
        await m.reply("No entities in this message.")


if __name__ == "__main__":
    bot.run()
