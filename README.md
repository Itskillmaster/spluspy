# SplusPy v2.2.11


**A fast, minimal, and fully-featured framework for Soroush Plus — self-bots and official bots**

---

## About

SplusPy is a Python library designed specifically for building **Soroush Plus self-bots** (userbots) and **official bots**. It provides a clean, intuitive API for automating your personal Soroush Plus account or building bots via the official HTTP Bot API.

> ⚠️ **Note:** This framework supports both **self-bot** (personal account) and **official bot** (Bot API) modes. Please adhere to Soroush's Terms of Service.

---

## Installation

```bash
pip install SplusPy
```

To upgrade to the latest version:

```bash
pip install --upgrade Spluspy
```

---

## Quick Start

Here is a minimal example to get your self-bot up and running:

```python
import spluspy
from spluspy import events

client = spluspy.Client("my_session")

@client.on_message()
async def handler(client, event):
    if event.message.message.lower() == "hello":
        await event.reply("Hi there!")

client.start()
client.run_until_disconnected()
```

### How it works

1. **Create a `Client`** — pass a session name (or path) to store your login.
2. **Register handlers** — use `@client.on_message()` to react to messages.
3. **Start the client** — call `client.start()` to connect and log in.
4. **Run forever** — `client.run_until_disconnected()` keeps the bot alive.

---

## Official Bot (Robot)

You can also build official bots using the HTTP Bot API:

```python
from spluspy import Robot, filters

bot = Robot("YOUR_BOT_TOKEN")

@bot.on_message(filters.text("hello"))
async def hello_handler(client, event):
    await event.reply("Hi there!")

bot.run()
```

### How it works

1. **Create a `Robot`** — pass your bot token.
2. **Register handlers** — use `@bot.on_message()` just like the self-bot.
3. **Run** — call `bot.run()` to start long-polling.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
