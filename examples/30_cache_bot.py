"""Example 30: Cache Bot

Demonstrates using the built-in LRU cache.
"""

from spluspy import Client
from spluspy.utils.cache import LRUCache

bot = Client("cache_session")
user_cache = LRUCache[int, str](max_size=1000, default_ttl=300)


@bot.on_message()
async def handler(m):
    """Cache user names."""
    # Check cache first
    cached_name = user_cache.get(m.sender_id)
    if cached_name:
        await m.reply(f"Welcome back, {cached_name}!")
    else:
        # Cache the name
        user_cache.set(m.sender_id, m.sender.first_name)
        await m.reply(f"Hello, {m.sender.first_name}! (cached for next time)")


if __name__ == "__main__":
    bot.run()
