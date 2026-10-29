"""Minimal official-bot example. Set SPLUS_BOT_TOKEN before running."""
import asyncio
import os

from spluspy.bot import Bot, filters

TOKEN = os.environ.get("SPLUS_BOT_TOKEN")
if not TOKEN:
    raise SystemExit("Set the SPLUS_BOT_TOKEN environment variable first.")

bot = Bot(TOKEN)


@bot.on_message(filters.text("/start"))
async def start_handler(client, event):
    chat_id = getattr(event, "chat_id", None)
    if chat_id is not None:
        await client.sendMessage(chat_id, "Hello from SPlusPy!")


async def main():
    await bot.start()


if __name__ == "__main__":
    asyncio.run(main())
