"""Example 3: Command Bot

A bot that responds to commands like /start, /help, etc.
"""

from spluspy import Client, filters

bot = Client(session_name="command_session")


@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    """Handle /start command."""
    await message.reply("Welcome! I'm your SplusPy bot.")


@bot.on_message(filters.command("help"))
async def help_handler(client, message):
    """Handle /help command."""
    await message.reply(
        "Available commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help\n"
        "/ping - Check if bot is alive"
    )


@bot.on_message(filters.command("ping"))
async def ping_handler(client, message):
    """Handle /ping command."""
    await message.reply("Pong!")


# Command with custom prefixes
@bot.on_message(filters.command("hello", prefixes_list=["!", "/"]))
async def hello_handler(client, message):
    """Handle !hello or /hello."""
    await message.reply("Hello there!")


if __name__ == "__main__":
    bot.run()
