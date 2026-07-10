"""Example 19: Event Types

Demonstrates all available event types.
"""

from spluspy import Client
from spluspy import filters

bot = Client("events_session")


@bot.on_message()
async def on_message(m):
    """Handle new messages."""
    print(f"New message from {m.sender_id}: {m.text}")


@bot.on_edited()
async def on_edited(m):
    """Handle edited messages."""
    print(f"Message edited: {m.text}")


@bot.on_callback_query()
async def on_callback(cb):
    """Handle callback queries."""
    print(f"Callback: {cb.data}")


@bot.on_inline_query()
async def on_inline(iq):
    """Handle inline queries."""
    print(f"Inline query: {iq.query}")


@bot.on_chat_action()
async def on_action(action):
    """Handle chat actions."""
    print(f"Chat action: {action.action_type}")


@bot.on_user_update()
async def on_user_update(update):
    """Handle user status changes."""
    print(f"User {update.user_id} status: {update.status}")


@bot.on_message_deleted()
async def on_deleted(update):
    """Handle deleted messages."""
    print(f"Messages deleted: {update.deleted_ids}")


@bot.on_message_read()
async def on_read(update):
    """Handle read receipts."""
    print(f"Messages read in chat {update.chat_id}")


if __name__ == "__main__":
    bot.run()
