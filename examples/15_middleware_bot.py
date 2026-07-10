"""Example 15: Middleware Bot

Demonstrates the middleware system for pre/post processing.
"""

import time
from spluspy import Client
from spluspy.middleware import Middleware


class TimingMiddleware(Middleware):
    """Logs how long each update takes to process."""

    async def on_update(self, update, handler):
        start = time.monotonic()
        result = await handler(update)
        elapsed = time.monotonic() - start
        print(f"Update processed in {elapsed:.3f}s")
        return result


class LoggingMiddleware(Middleware):
    """Logs every incoming update."""

    async def on_update(self, update, handler):
        print(f"Received update: {type(update).__name__}")
        return await handler(update)


bot = Client("middleware_session")
bot.middleware.add(TimingMiddleware())
bot.middleware.add(LoggingMiddleware())


@bot.on_message()
async def handler(m):
    await m.reply("Hello!")


if __name__ == "__main__":
    bot.run()
