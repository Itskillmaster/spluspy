"""Example 11: Message Actions

Demonstrates various message actions like edit, delete, forward, pin.
"""

from spluspy import Client
from spluspy import filters

bot = Client("actions_session")


@bot.on_message(filters.command("edit"))
async def edit_example(m):
    """Demonstrate message editing."""
    sent = await m.reply("This message will be edited...")
    await sent.edit("Message edited successfully!")


@bot.on_message(filters.command("pin"))
async def pin_example(m):
    """Demonstrate message pinning."""
    sent = await m.reply("This message will be pinned!")
    await sent.pin(notify=True)


@bot.on_message(filters.command("forward"))
async def forward_example(m):
    """Demonstrate message forwarding."""
    await m.reply("Forwarding this message...")
    # await m.forward(target_chat_id)


@bot.on_message(filters.command("react"))
async def react_example(m):
    """Demonstrate reactions."""
    await m.react("❤️")
    await m.reply("Reaction added!")


if __name__ == "__main__":
    bot.run()
