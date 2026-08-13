# SplusPy v2.2.6

**A fast, minimal, and fully-featured self-bot framework**

---

## About

SplusPy is a Python library designed specifically for building **Soroush Plus self-bots** (userbots). It provides a clean, intuitive API for automating your personal Soroush Plus account with ease.

> ⚠️ **Note:** This is a **self-bot framework** — it operates on your personal account, not a bot account. Please adhere to Telegram's Terms of Service.

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

## License

MIT License. See [LICENSE](LICENSE) for details.
