"""Example 33: Context Manager

Demonstrates using the client as a context manager.
"""

from spluspy import Client
from spluspy import filters


async def main():
    async with Client("context_session") as bot:
        @bot.on_message(filters.command("ping"))
        async def handler(m):
            await m.reply("Pong!")

        await bot.start()
        await bot.run_until_disconnected()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
