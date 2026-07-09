# SPlusPy

**SPlusPy** is an asynchronous Python 3 library for interacting with the [Soroush Plus](https://web.splus.ir) platform — as a user account or a bot account.

Built as a fork of [Telethon](https://github.com/LonamiWebs/Telethon), SPlusPy is adapted specifically for the Soroush Plus ecosystem with native MTProto, WebSocket transport, and Layer 182 support.

> **Note:** SPlusPy is an unofficial third-party library. Use it responsibly and comply with Soroush Plus's Terms of Service.

## Features

- Fully asynchronous (`asyncio`) + sync support
- User and bot account support
- Native MTProto + WebSocket transport
- Built-in API credentials (no registration needed)
- Event-driven handler system
- Inline & reply keyboard buttons
- Conversation API for interactive flows
- QR code & phone login
- Rate limiting & auto-retry
- File upload/download with progress

## Installation

```bash
pip install -U splusthon
```

## Quick Start

### Bot (simplest)

```python
import asyncio
from spluspy import SoroushClient

bot = SoroushClient('my_bot')

@bot.on_message(incoming=True)
async def handler(event):
    if event.is_private and event.raw_text == 'سلام':
        await event.reply('خوبی!')

async def main():
    await bot.start()
    print('Bot is running!')
    await bot.run_until_disconnected()

asyncio.run(main())
```

### User Account

```python
import asyncio
from spluspy import SoroushClient

client = SoroushClient('session_name')

@client.on_message(incoming=True, pattern='(?i)hello')
async def handler(event):
    await event.reply('Hey there!')

async def main():
    await client.start(phone='+98XXXXXXXXXX')
    print('Logged in!')
    await client.run_until_disconnected()

asyncio.run(main())
```

### Sync Mode

```python
from spluspy import SoroushClient
from spluspy.sync import synchronous

client = SoroushClient('session')
client.start()

# All methods work synchronously
dialogs = client.get_dialogs()
```

---

## Event Types

Import from `spluspy.events`:

```python
from spluspy import events
```

| Event | Description |
|---|---|
| `events.NewMessage` | New message received |
| `events.MessageEdited` | Message was edited |
| `events.CallbackQuery` | Inline button clicked |
| `events.ChatAction` | Join/leave/pin/title change |
| `events.InlineQuery` | Bot inline query |
| `events.UserUpdate` | User online/offline/typing |
| `events.MessageDeleted` | Message was deleted |
| `events.MessageRead` | Read receipt received |
| `events.Album` | Grouped media (album) received |

### Filtering Events

```python
# Only incoming messages
@client.on(events.NewMessage(incoming=True))

# Only from specific users
@client.on(events.NewMessage(from_users='username'))

# Only matching a regex pattern
@client.on(events.NewMessage(pattern='(?i)help'))

# Only in specific chats
@client.on(events.NewMessage(chats=['chat_username']))
```

---

## Handler Decorators

SPlusPy provides shorthand decorators on the client:

| Decorator | Equivalent |
|---|---|
| `@client.on_message(...)` | `@client.on(events.NewMessage(...))` |
| `@client.on_edited(...)` | `@client.on(events.MessageEdited(...))` |
| `@client.on_callback_query(...)` | `@client.on(events.CallbackQuery(...))` |
| `@client.on_chat_action(...)` | `@client.on(events.ChatAction(...))` |
| `@client.on_inline_query(...)` | `@client.on(events.InlineQuery(...))` |
| `@client.on_user_update(...)` | `@client.on(events.UserUpdate(...))` |
| `@client.on_message_deleted(...)` | `@client.on(events.MessageDeleted(...))` |
| `@client.on_message_read(...)` | `@client.on(events.MessageRead(...))` |

### Parameters

All shorthand decorators accept:

| Parameter | Type | Description |
|---|---|---|
| `chats` | `str | list` | Filter by chat(s) |
| `blacklist_chats` | `bool` | Treat chats as blacklist |
| `incoming` | `bool` | Only incoming messages |
| `outgoing` | `bool` | Only outgoing messages |
| `from_users` | `str | list` | Filter by sender(s) |
| `forwards` | `bool` | Only forwarded messages |
| `pattern` | `str | regex` | Regex pattern to match |
| `func` | `callable` | Custom filter function |

---

## Client Methods

### Messages

```python
# Send a message
await client.send_message('username', 'Hello!')

# Send with buttons
from spluspy import Button
await client.send_message('username', 'Pick:', buttons=[
    [Button.inline('Option 1', b'opt1'), Button.inline('Option 2', b'opt2')]
])

# Get messages
messages = await client.get_messages('username', limit=10)

# Edit a message
await client.edit_message(msg, 'New text')

# Delete messages
await client.delete_messages(msg)

# Forward messages
await client.forward_messages('destination', msg)

# Mark as read
await client.send_read_acknowledge(msg)
```

### Dialogs

```python
# Get all dialogs
async for dialog in client.iter_dialogs():
    print(dialog.name, dialog.unread_count)

# Get specific dialog
dialog = await client.get_dialogs(limit=5)
```

### Users & Entities

```python
# Get current user
me = await client.get_me()

# Resolve entity
user = await client.get_entity('username')

# Get participants
async for user in client.iter_participants('chat_username'):
    print(user.first_name)
```

### Media

```python
# Download media
await client.download_media(message, file='downloads/')

# Send a file
await client.send_file('username', '/path/to/photo.jpg')

# Upload a file
file = await client.upload_file('/path/to/file.pdf')
```

### Profile Photos

```python
photos = await client.get_profile_photos('username')
await client.download_profile_photo('username', file='photo.jpg')
```

### Chat Management

```python
# Get chat info
await client.get_permissions('chat_username')

# Edit admin
await client.edit_admin('chat_username', user, is_admin=True)

# Kick user
await client.kick_participant('chat_username', 'username')
```

---

## Buttons & Keyboards

### Inline Buttons (under message)

```python
from spluspy import Button

# Callback button
Button.inline('Click me', b'callback_data')

# URL button
Button.url('Visit', 'https://example.com')

# Switch inline
Button.switch_inline('Search', 'query')

# Game button
Button.game('Play')
```

### Reply Keyboard (replaces user keyboard)

```python
# Text button
Button.text('Menu', resize=True)

# Request location
Button.request_location('Share Location')

# Request phone
Button.request_phone('Share Phone')

# Request poll
Button.request_poll('Create Poll')

# Clear keyboard
Button.clear()

# Force reply
Button.force_reply()
```

### Example with Buttons

```python
@bot.on_message(pattern='menu')
async def menu(event):
    await event.reply('Choose:', buttons=[
        [Button.inline('Profile', b'profile'), Button.inline('Settings', b'settings')],
        [Button.url('Help', 'https://help.example.com')]
    ])

@bot.on_callback_query(pattern='profile')
async def profile_handler(event):
    await event.answer('Your profile', alert=True)
```

---

## Sessions

| Session | Description |
|---|---|
| `MemorySession` | In-memory only (lost on restart) |
| `SQLiteSession` | Default. Saved as `.session` file |
| `StringSession` | Serialized as base64 string |

```python
from spluspy import SoroushClient
from spluspy.sessions import StringSession

# String session (useful for env variables)
client = SoroushClient(StringSession(), api_id=..., api_hash=...)
```

---

## Authentication

```python
# Phone login (interactive)
await client.start(phone='+98XXXXXXXXXX')

# Bot token login
await client.start(bot_token='123456:ABC-DEF')

# QR code login
qr = await client.qr_login()
print(qr.url)  # Show this URL or scan QR
await qr.wait()  # Block until scanned

# 2FA
await client.edit_2fa(new_password='my_password', hint='hint')
```

---

## Conversation API

Interactive conversations for bot flows:

```python
async with client.conversation('user', timeout=60) as conv:
    conv.send_message('What is your name?')
    response = await conv.get_response()
    conv.send_message(f'Hello {response.text}!')
```

---

## Rate Limiting

```python
from spluspy import SoroushClient, RateLimiter, RetryConfig

client = SoroushClient('session')
client._request_loop_rate_limiter = RateLimiter(rate=1.0, burst=10)
```

---

## Connection Types

| Type | Description |
|---|---|
| `ConnectionWebSocket` | Default. WebSocket transport |
| `ConnectionTcpFull` | Full TCP |
| `ConnectionTcpAbridged` | Compact TCP |
| `ConnectionTcpObfuscated` | Anti-censorship |

```python
from spluspy.network import ConnectionTcpAbridged

client = SoroushClient('session', connection=ConnectionTcpAbridged)
```

---

## Utilities

```python
from spluspy import utils

# Display name
utils.get_display_name(user)

# Parse phone
utils.parse_phone('+98 912 123 4567')

# Parse username
utils.parse_username('https://t.me/username')

# Peer ID
utils.get_peer_id(chat)
```

---

## Error Handling

```python
from spluspy import errors

try:
    await client.send_message('user', 'hello')
except errors.FloodWaitError as e:
    print(f'Wait {e.seconds} seconds')
except errors.PeerIdInvalidError:
    print('Invalid peer')
```

---

## Examples

See the [`examples/`](examples/) directory for complete working examples:

- `salam_bot.py` — Simple auto-reply bot
- `replier.py` — Trigger-based replies
- `assistant.py` — Plugin-based bot framework

---

## License

SPlusPy is open-source software distributed under its respective license.
