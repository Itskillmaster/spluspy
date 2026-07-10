"""Example 8: Combined Filters

Using filter composition with & and | operators.
"""

from spluspy import Client, filters

# Clean API with session_name
bot = Client(session_name="combined_session")


# Text messages in private chats
@bot.on_message(filters.text & filters.private)
async def private_text_handler(client, message):
    await message.reply("You sent text in a private chat!")


# Photo or video messages
@bot.on_message(filters.photo | filters.video)
async def media_handler(client, message):
    await message.reply("Nice media!")


# Text in groups, not from bots
@bot.on_message(filters.text & filters.group & ~filters.bot)
async def group_text_handler(client, message):
    await message.reply("Group message from a human!")


# Using text_contains filter
@bot.on_message(filters.text_contains("hello", case_sensitive=False))
async def hello_mention_handler(client, message):
    await message.reply("You mentioned 'hello'!")


# Using length filter
@bot.on_message(filters.length(min=10, max=100))
async def medium_length_handler(client, message):
    await message.reply("Nice message length!")


# Using from_callable for custom logic
@bot.on_message(filters.from_callable(lambda m: m.text and m.text.isupper()))
async def all_caps_handler(client, message):
    await message.reply("WHY ARE YOU SHOUTING?!")


if __name__ == "__main__":
    bot.run()
