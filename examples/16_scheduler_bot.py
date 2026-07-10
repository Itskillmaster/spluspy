"""Example 16: Scheduler Bot

Demonstrates the built-in task scheduler.
"""

from spluspy import Client

bot = Client("scheduler_session")

# Scheduled tasks
async def heartbeat():
    print("Heartbeat!")
    # Could send a message, check something, etc.

async def daily_report():
    print("Daily report generated!")


@bot.on_message(filters.command("start_scheduler"))
async def start_scheduler(m):
    bot.scheduler.add("heartbeat", heartbeat, interval=60)
    bot.scheduler.add("daily", daily_report, interval=86400)
    await m.reply("Scheduler started!")


@bot.on_message(filters.command("stop_scheduler"))
async def stop_scheduler(m):
    bot.scheduler.remove("heartbeat")
    bot.scheduler.remove("daily")
    await m.reply("Scheduler stopped!")


if __name__ == "__main__":
    bot.run()
