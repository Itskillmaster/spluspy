"""Example 25: Working Bot with Soroush Plus

This example shows how to connect to Soroush Plus using spluspy.

Requirements:
    pip install spluspy

Usage:
    1. Run this script
    2. Enter your phone number when prompted
    3. Enter the verification code sent to your phone
    4. The bot will start listening for messages
"""

import asyncio
from spluspy import Client

# Create client with a session file (persists across restarts)
bot = Client("my_soroush_bot")


@bot.on_message()
async def handler(m):
    """Reply to every message."""
    await m.reply("Hello from SplusPy!")


@bot.on_message(filters.command("start"))
async def start_handler(m):
    """Handle /start command."""
    await m.reply("Welcome! I am your Soroush Plus bot.")


# Import filters
from spluspy import filters


@bot.on_message(filters.command("help"))
async def help_handler(m):
    """Handle /help command."""
    await m.reply("Available commands:\n/start - Start bot\n/help - Show help")


async def main():
    """Main function."""
    print("Connecting to Soroush Plus...")
    print("You will be prompted for your phone number.")
    print()

    await bot.start()

    print()
    print("Bot is running! Press Ctrl+C to stop.")
    print()

    await bot.run_until_disconnected()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped.")
