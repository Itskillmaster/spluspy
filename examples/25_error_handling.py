"""Example 25: Error Handling

Demonstrates proper error handling with the exception hierarchy.
"""

import asyncio
from spluspy import Client, filters
from spluspy.errors import (
    SoroushPlusAPIError,
    SessionExpiredError,
    FloodWait,
    Unauthorized,
    RPCError,
)

bot = Client(session_name="error_session")


@bot.on_message(filters.text & filters.private)
async def safe_handler(client, message):
    """Handle messages with error handling."""
    try:
        await message.reply("Hello!")
    except FloodWait as e:
        print(f"Flood wait: {e.seconds} seconds")
        await asyncio.sleep(e.seconds)
    except Unauthorized:
        print("Not authorized! Please re-login.")
    except SessionExpiredError:
        print("Session expired! Please re-authenticate.")
    except RPCError as e:
        print(f"RPC error (code {e.code}): {e}")
    except SoroushPlusAPIError as e:
        print(f"API error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


@bot.on_error(FloodWait, Unauthorized, SessionExpiredError)
async def global_error_handler(event):
    """Global error handler for specific exceptions."""
    exc = event.exception
    if isinstance(exc, FloodWait):
        print(f"Global: Flood wait {exc.seconds}s")
    elif isinstance(exc, SessionExpiredError):
        print("Global: Session expired, reconnecting...")
    else:
        print(f"Global error: {exc}")


@bot.on_error()
async def catch_all_handler(event):
    """Catch-all error handler."""
    print(f"Unhandled: {event.exception}")


if __name__ == "__main__":
    bot.run()
