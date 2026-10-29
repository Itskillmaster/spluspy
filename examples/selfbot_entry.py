"""Self-bot entry-point example; adapt authentication to your environment."""
from spluspy.selfbot import Client, events

# A session name/path, not an official bot token.
app = Client("spluspy-session")


@app.on(events.NewMessage)
async def on_message(event):
    if getattr(event, "raw_text", None) == "سلام":
        await event.respond("سلام! 👋")


if __name__ == "__main__":
    app.run()
