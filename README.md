<div align="center">

# 🚀 SPlusPy 
**The Powerful, Fast, and Asynchronous Python Library for SoroushPlus API** **کتابخانه قدرتمند، سریع و ناهمگام پایتون برای ساخت ربات و یوزربات در سروش‌پلاس**

[![PyPI - Version](https://img.shields.io/pypi/v/spluspy?style=for-the-badge&logo=pypi&logoColor=white&color=blue)](https://pypi.org/project/spluspy/)
[![Python - Version](https://img.shields.io/badge/Python-3.7+-yellow?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub - License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://github.com/itskillmaster/SPlusthon)
[![Asyncio - Supported](https://img.shields.io/badge/Asyncio-Supported-red?style=for-the-badge&logo=python)](https://docs.python.org/3/library/asyncio.html)

[English Documentation](#-english-documentation) • [مستندات فارسی](#-مستندات-فارسی) • [Report Bug](https://github.com/itskillmaster/SPlusthon/issues)

<hr>
</div>

---

# 🇮🇷 مستندات فارسی

<div dir="rtl">

## 🌟 چرا SPlusPy؟
کتابخانه **SPlusPy** یک کتابخانه پایتون مبتنی بر `asyncio` است که برای تعامل ساده، سریع و بهینه با API سروش‌پلاس طراحی شده است. این کتابخانه به شما امکان می‌دهد با استفاده از حساب کاربری یا توکن ربات خود، اسکریپت‌ها و ربات‌های پیشرفته بسازید.

* ⚡ **کارایی و سرعت بالا:** پشتیبانی کامل از `asyncio` برای انجام عملیات همزمان بدون افت سرعت.
* 🛠 **سادگی در استفاده:** طراحی ساده و خوانا با الهام از معماری Telethon.
* 📡 **سیستم رویدادها (Events):** پاسخ‌گویی خودکار به پیام‌ها، ویرایش‌ها، کلیک روی دکمه‌ها و آپدیت‌های مخاطبین.
* 🔐 **امنیت:** ذخیره‌سازی امن نشست‌ها (Sessions) به صورت فایل‌های SQLite یا رشته‌ای (StringSession).
* 📦 **امکانات گسترده:** ارسال و ویرایش پیام، مدیریت مکالمات، دانلود/آپلود فایل‌های حجیم و مدیا.

---

## ⚙️ نصب و راه‌اندازی

برای نصب آخرین نسخه از PyPI، دستور زیر را اجرا کنید:
```bash
pip install --upgrade spluspy
```

## نمونه ربات 


```
import asyncio
from spluspy import SoroushClient

bot = SoroushClient('salam_bot')


@bot.on_message(incoming=True)
async def handler(event):
    if not event.is_private:
        return

    text = event.raw_text.strip()

    if text == 'سلام':
        await event.reply('خوبی')
    elif text in ('خوبی', 'خوبی؟', 'خوبی!'):
        await event.reply('ممنون، خوبم!')


async def main():
    await bot.start()
    print('ربات فعال شد!')
    await bot.run_until_disconnected()


asyncio.run(main())

```

## توضیحات 





Now I have all the information needed. Here is my comprehensive report on the spluspy library:

---

# Comprehensive Analysis of the spluspy Library

## Overview

**spluspy** (version 1.0.1) is a Soroush Plus client library for Python, forked from Telethon. The main entry point is `SoroushClient` (aliased as `Client`). It provides both synchronous and asynchronous APIs for interacting with the Soroush Plus messaging platform.

---

## 1. Client Methods (via `SoroushClient`)

The `SoroushClient` class at `D:\SPlusthon-main\spluspy\client\soroushclient.py` inherits from 12 method mixin classes, each providing a group of related methods:

### Message Methods (`client/messages.py` -- `MessageMethods`)
| Method | Description |
|---|---|
| `iter_messages()` | Iterator over messages for a given chat with extensive filtering (date, search, filter, from_user, reply_to, scheduled, reverse, ids) |
| `get_messages()` | Returns a list/single message (wrapper around iter_messages) |
| `send_message()` | Sends text, media, or buttons to an entity. Supports parse_mode, scheduling, silent, background, send_as, message_effect_id |
| `forward_messages()` | Forwards messages with drop_author and drop_media_captions options |
| `edit_message()` | Edits text, media, buttons, or scheduled messages |
| `delete_messages()` | Deletes one or more messages (with revoke option) |
| `send_read_acknowledge()` | Marks messages as read |
| `pin_message()` / `unpin_message()` | Pins/unpins a message in a chat |

### Chat Methods (`client/chats.py` -- `ChatMethods`)
| Method | Description |
|---|---|
| `iter_participants()` / `get_participants()` | Iterate/list chat participants with search and filter |
| `iter_admin_log()` / `get_admin_log()` | Iterate/list admin log events for channels |
| `iter_profile_photos()` / `get_profile_photos()` | Iterate/list profile photos |
| `action()` | Context manager for chat actions (typing, recording, uploading, etc.) |
| `edit_admin()` | Edit admin permissions for users |
| `edit_permissions()` | Edit user restrictions (ban, mute, etc.) |
| `kick_participant()` | Kick/leave a chat |
| `get_permissions()` | Fetch user permissions in a chat/channel |
| `get_stats()` | Retrieve channel/megagroup statistics |

### Dialog Methods (`client/dialogs.py` -- `DialogMethods`)
| Method | Description |
|---|---|
| `iter_dialogs()` / `get_dialogs()` | Iterate/list dialogs with folder/archive support |
| `iter_drafts()` / `get_drafts()` | Iterate/list draft messages |
| `edit_folder()` | Archive/unarchive dialogs |
| `delete_dialog()` | Leave/delete a dialog |
| `conversation()` | Create a Conversation context manager for interactive dialogs |

### User Methods (`client/users.py` -- `UserMethods`)
| Method | Description |
|---|---|
| `get_me()` | Get the currently logged-in user |
| `is_bot()` | Check if logged in as bot |
| `is_user_authorized()` | Check if user is authorized/logged in |
| `get_entity()` | Resolve entities (users, chats, channels) by username, ID, etc. |
| `get_input_entity()` | Get input peer version of an entity |
| `get_peer_id()` | Get the marked ID for an entity |

### Download Methods (`client/downloads.py` -- `DownloadMethods`)
| Method | Description |
|---|---|
| `download_profile_photo()` | Download a user/chat/channel profile photo |
| `download_media()` | Download media from a message (photos, documents, contacts, web pages) |
| `download_file()` | Low-level file download from any input location |
| `iter_download()` | Stream file downloads in chunks |

### Upload Methods (`client/uploads.py` -- `UploadMethods`)
| Method | Description |
|---|---|
| `send_file()` | Send files (photos, documents, audio, video, etc.) with resize support |
| `upload_file()` | Upload a file without sending it |
| `upload_profile_photo()` | Upload/set a new profile photo |

### Authentication Methods (`client/auth.py` -- `AuthMethods`)
| Method | Description |
|---|---|
| `start()` | High-level connect + login (supports phone, bot_token, 2FA) |
| `sign_in()` | Sign in with phone/code, password, or bot_token |
| `send_code_request()` | Send authentication code |
| `qr_login()` | Initiate QR code login (returns `QRLogin` object) |
| `log_out()` | Log out and delete session file |
| `edit_2fa()` | Change 2FA settings (set, change, or remove password) |

### Bot Methods (`client/bots.py` -- `BotMethods`)
| Method | Description |
|---|---|
| `inline_query()` | Make an inline query to a bot |

### Account Methods (`client/account.py` -- `AccountMethods`)
| Method | Description |
|---|---|
| `takeout()` | Create a takeout session (proxy client for data export) |

### Update Methods (`client/updates.py` -- `UpdateMethods`)
| Method | Description |
|---|---|
| `on()` | Decorator for event handling |
| `add_event_handler()` | Register an event handler |
| `remove_event_handler()` | Unregister an event handler |
| `list_event_handlers()` | List registered handlers |
| `run_until_disconnected()` | Run the event loop until disconnected |
| `set_receive_updates()` | Enable/disable receiving updates |

### Message Parse Methods (`client/messageparse.py` -- `MessageParseMethods`)
| Property/Method | Description |
|---|---|
| `parse_mode` | Property to get/set default parse mode (markdown, html, None) |

### Button Methods (`client/buttons.py` -- `ButtonMethods`)
| Method | Description |
|---|---|
| `build_reply_markup()` | Build `ReplyInlineMarkup` or `ReplyKeyboardMarkup` from button definitions |

---

## 2. Event Types (`events/`)

All events are in `D:\SPlusthon-main\spluspy\events\__init__.py`:

| Event | File | Description |
|---|---|---|
| `events.NewMessage` | `newmessage.py` | Fires on new messages. Supports `incoming`, `outgoing`, `from_users`, `forwards`, `pattern` filters |
| `events.MessageEdited` | `messageedited.py` | Fires when a message is edited. Inherits NewMessage filtering |
| `events.CallbackQuery` | `callbackquery.py` | Fires on inline button clicks (bot). Supports `data` and `pattern` matching |
| `events.ChatAction` | `chataction.py` | Fires on chat actions: joins, leaves, kicks, title/photo changes, pins, game scores, channel participant updates |
| `events.InlineQuery` | `inlinequery.py` | Fires on bot inline queries. Supports `users`, `pattern` filters |
| `events.UserUpdate` | `userupdate.py` | Fires on user status changes (online/offline, typing, uploading, recording, etc.) |
| `events.MessageDeleted` | `messagedeleted.py` | Fires on message deletions. Note: unreliable for private chats |
| `events.MessageRead` | `messageread.py` | Fires on read receipts (inbox/outbox). Supports `inbox` filter |
| `events.Album` | `album.py` | Fires when an album (grouped media) is received. Aggregates multiple messages |
| `events.Raw` | `raw.py` | Raw update handler. Pass any `Update` type through. Can filter by specific types |

### Event Flow Control
- `events.StopPropagation` -- exception to stop other handlers from running
- `events.register()` -- client-less handler registration
- `events.unregister()` -- client-less handler removal
- `events.is_handler()` -- check if a callback is registered
- `events.list()` -- list registered event builders on a callback

---

## 3. Handler Decorators

### Convenience Decorators (on `SoroushClient`, defined in `soroushclient.py`)

| Decorator | Parameters | Description |
|---|---|---|
| `@client.on_message(...)` | `chats`, `blacklist_chats`, `incoming`, `outgoing`, `from_users`, `forwards`, `pattern`, `func` | Shorthand for `@client.on(events.NewMessage(...))` |
| `@client.on_edited(...)` | `chats`, `blacklist_chats`, `incoming`, `outgoing`, `from_users`, `forwards`, `pattern`, `func` | Shorthand for `@client.on(events.MessageEdited(...))` |
| `@client.on_callback_query(...)` | `chats`, `blacklist_chats`, `data`, `pattern`, `func` | Shorthand for `@client.on(events.CallbackQuery(...))` |
| `@client.on_chat_action(...)` | `chats`, `blacklist_chats`, `func` | Shorthand for `@client.on(events.ChatAction(...))` |
| `@client.on_inline_query(...)` | `chats`, `blacklist_chats`, `pattern`, `func` | Shorthand for `@client.on(events.InlineQuery(...))` |
| `@client.on_user_update(...)` | `chats`, `blacklist_chats`, `func` | Shorthand for `@client.on(events.UserUpdate(...))` |
| `@client.on_message_deleted(...)` | `chats`, `blacklist_chats`, `func` | Shorthand for `@client.on(events.MessageDeleted(...))` |
| `@client.on_message_read(...)` | `chats`, `blacklist_chats`, `incoming`, `outgoing`, `func` | Shorthand for `@client.on(events.MessageRead(...))` |

### Classic Decorator
- `@client.on(events.NewMessage)` -- the classic `client.on()` decorator (defined in `UpdateMethods`)

---

## 4. Session Types (`sessions/`)

| Session | File | Description |
|---|---|---|
| `Session` | `abstract.py` | Abstract base class defining the session interface (set_dc, dc_id, auth_key, file reference management, entity caching) |
| `MemorySession` | `memory.py` | In-memory session storing all data in RAM (entities, sent files, etc.) |
| `SQLiteSession` | `sqlite.py` | File-based session using SQLite (saves as `.session` file). Current DB version: 8. Default session type |
| `StringSession` | `string.py` | Session that can be serialized/deserialized as a base64 string. Useful for environments without file system access |

---

## 5. Button/Keyboard Support (`tl/custom/button.py`)

### Inline Buttons (under message)
| Method | Description |
|---|---|
| `Button.inline(text, data)` | Creates an inline callback button (max 64 bytes data) |
| `Button.switch_inline(text, query, same_peer)` | Creates a switch-to-inline button |
| `Button.url(text, url)` | Creates a URL button |
| `Button.auth(text, url, bot, write_access, fwd_text)` | Creates a Telegram Login button |
| `Button.buy(text)` | Creates a payment/buy button |
| `Button.game(text)` | Creates a game button |

### Reply Keyboard Buttons (replaces user keyboard)
| Method | Description |
|---|---|
| `Button.text(text, resize, single_use, selective, persistent, placeholder)` | Creates a text button |
| `Button.request_location(text, ...)` | Creates a location request button |
| `Button.request_phone(text, ...)` | Creates a phone request button |
| `Button.request_poll(text, force_quiz, ...)` | Creates a poll creation button |

### Special Markup
| Method | Description |
|---|---|
| `Button.clear(selective)` | Clears/hides the keyboard |
| `Button.force_reply(single_use, selective, placeholder)` | Forces the user to reply |

### MessageButton (`tl/custom/messagebutton.py`)
- Returned by `message.buttons` -- wraps buttons from received messages with `.click()` method

---

## 6. Utility Functions (`utils.py`)

Key utilities in `D:\SPlusthon-main\spluspy\utils.py` (1593 lines):

| Function | Description |
|---|---|
| `get_display_name(entity)` | Get display name for User, Chat, or Channel |
| `get_extension(media)` | Get file extension for Telegram media |
| `get_input_peer(entity)` | Convert entity to InputPeer |
| `get_input_user(entity)` / `get_input_channel(entity)` / `get_input_chat(entity)` | Convert to specific input types |
| `get_peer_id(peer, add_mark)` | Get the marked/signed ID for a peer |
| `parse_phone(phone)` | Parse and normalize phone numbers |
| `parse_username(string)` | Parse usernames and invite links |
| `resolve_id(peer_id)` | Resolve a marked peer ID to (id, PeerClass) |
| `get_peer(peer)` | Convert input peer or entity to Peer type |
| `is_list_like(obj)` | Check if object is list-like |
| `get_appropriated_part_size(file_size)` | Determine optimal download chunk size |
| `get_inner_text(text, entities)` | Extract inner text for message entities |
| `sanitize_parse_mode(mode)` | Normalize parse mode string to parser object |
| `resolve_bot_file_id(file_id)` | Resolve bot API file IDs |
| `stripped_photo_to_jpg(data)` | Convert stripped photo bytes to JPEG |
| `maybe_async(func)` | Call sync or async function appropriately |
| `_get_entity_pair(...)` | Get (entity, input_entity) pair from cache |
| `get_file_info(file)` | Get file location info for downloads |

---

## 7. Sync Module (`sync.py`)

`D:\SPlusthon-main\spluspy\sync.py` provides automatic sync wrappers:

- **How it works**: All public async methods on `SoroushClient`, `_TakeoutClient`, `Draft`, `Dialog`, `MessageButton`, `ChatGetter`, `SenderGetter`, `Forward`, `Message`, `InlineResult`, and `Conversation` are wrapped to be synchronous.
- **Behavior**: If the event loop is not running, the coroutine runs via `loop.run_until_complete()`. If the loop is already running, the raw coroutine is returned (so you can await it yourself).
- **Import**: Simply `import spluspy.sync` to enable all sync wrappers.

---

## 8. Custom Types (`tl/custom/`)

| Type | File | Description |
|---|---|---|
| `Message` | `message.py` | Unified message class wrapping both `Message` and `MessageService`. Properties: `text`, `raw_text`, `photo`, `document`, `audio`, `voice`, `video`, `video_note`, `gif`, `sticker`, `contact`, `game`, `geo`, `invoice`, `poll`, `venue`, `dice`, `web_preview`, `buttons`, `button_count`, `file`, `forward`, `is_reply`, `reply_to_msg_id`. Methods: `respond()`, `reply()`, `forward_to()`, `edit()`, `delete()`, `download_media()`, `click()`, `mark_read()`, `pin()`, `unpin()`, `get_reply_message()`, `get_entities_text()` |
| `Conversation` | `conversation.py` | Interactive conversation context manager. Methods: `send_message()`, `send_file()`, `mark_read()`, `get_response()`, `get_reply()`, `get_edit()`, `wait_read()`, `wait_event()`, `cancel()`, `cancel_all()` |
| `Dialog` | `dialog.py` | Dialog wrapper with properties: `entity`, `input_entity`, `id`, `name`, `title`, `unread_count`, `unread_mentions_count`, `draft`, `is_user`, `is_group`, `is_channel`, `pinned`, `archived`, `message`, `date`. Methods: `send_message()`, `delete()`, `archive()` |
| `Draft` | `draft.py` | Draft message wrapper. Properties: `text`, `raw_text`, `is_empty`, `date`, `link_preview`, `reply_to_msg_id`, `entity`. Methods: `set_message()`, `send()`, `delete()` |
| `Forward` | `forward.py` | Message forward header wrapper. Implements ChatGetter and SenderGetter |
| `Button` | `button.py` | Helper for defining reply markups (see section 5) |
| `MessageButton` | `messagebutton.py` | Button wrapper for received messages with `click()` method |
| `InlineBuilder` | `inlinebuilder.py` | Build inline query results (articles, photos, etc.) |
| `InlineResult` | `inlineresult.py` | Individual inline query result with `click()` |
| `InlineResults` | `inlineresults.py` | List of inline results with iteration |
| `QRLogin` | `qrlogin.py` | QR code login support with `url`, `token`, `expires`, `wait()`, `recreate()` |
| `AdminLogEvent` | `adminlogevent.py` | Admin log event wrapper |
| `ParticipantPermissions` | `participantpermissions.py` | User permission wrapper for chats/channels |
| `InputSizedFile` | `inputsizedfile.py` | File input with known size |
| `File` | `file.py` | File info wrapper (id, name, size, mime_type, etc.) |

### Sender/Chat Getter Mixins
- `SenderGetter` (`sendergetter.py`) -- provides `sender`, `sender_id`, `input_sender`, `get_sender()` methods
- `ChatGetter` (`chatgetter.py`) -- provides `chat`, `chat_id`, `input_chat`, `is_private`, `is_group`, `is_channel`, `get_chat()` methods

### Soroush-Specific Types (`tl/custom/types.py`)
- `FactCheck` -- stub type for Soroush fact-checking feature
- `SuggestedPost` -- stub type for Soroush suggested posts

---

## 9. Connection Types (`network/connection/`)

| Connection | File | Description |
|---|---|---|
| `Connection` | `connection.py` | Abstract base connection class |
| `ConnectionTcpFull` | `tcpfull.py` | Full TCP connection (original Telegram transport) |
| `ConnectionTcpIntermediate` | `tcpintermediate.py` | Intermediate TCP (lighter protocol) |
| `ConnectionTcpAbridged` | `tcpabridged.py` | Abridged TCP (most compact, recommended) |
| `ConnectionTcpObfuscated` | `tcpobfuscated.py` | Obfuscated TCP (anti-censorship, looks like random data) |
| `ConnectionWebSocket` | `websocket.py` | WebSocket connection |
| `ConnectionHttp` | `http.py` | HTTP connection |
| `ConnectionTcpMTProxyAbridged` | `tcpmtproxy.py` | MTProto Proxy (abridged) |
| `ConnectionTcpMTProxyIntermediate` | `tcpmtproxy.py` | MTProto Proxy (intermediate) |
| `ConnectionTcpMTProxyRandomizedIntermediate` | `tcpmtproxy.py` | MTProto Proxy (randomized intermediate) |
| `TcpMTProxy` | `tcpmtproxy.py` | MTProto Proxy helper |

---

## 10. Special Features

### QR Code Login (`tl/custom/qrlogin.py` + `client/auth.py`)
- `client.qr_login()` -- initiates QR login flow
- Returns `QRLogin` object with `.url`, `.token`, `.expires` properties
- Call `await qr_login.wait()` to block until scanned
- Supports token regeneration via `qr_login.recreate()`

### Two-Factor Authentication (2FA) (`client/auth.py`)
- `client.edit_2fa(current_password, new_password, hint, email, email_code_callback)` -- full 2FA management
- Automatic 2FA detection during `start()` -- prompts for password if enabled

### Rate Limiter (`client/ratelimiter.py`)
- `RateLimiter(rate, burst, enabled)` -- token bucket rate limiter
- `RetryConfig(max_retries, base_delay, max_delay, exponential_base, retry_on, flood_sleep_threshold)` -- retry configuration
- Integrated into the request pipeline to proactively prevent FloodWait errors
- Tracks per-request-type flood waits

### Takeout Sessions (`client/account.py`)
- `client.takeout(...)` -- returns a `_TakeoutClient` proxy that wraps requests in `InvokeWithTakeoutRequest`
- Supports context manager protocol for automatic session finalization

### Conversation API (`tl/custom/conversation.py`)
- `client.conversation(entity, timeout, total_timeout, max_messages, exclusive, replies_are_responses)` -- creates interactive conversations
- Supports `async with` / `with` blocks
- Methods: `send_message()`, `send_file()`, `get_response()`, `get_reply()`, `get_edit()`, `wait_read()`, `wait_event()`, `cancel()`

### Parse Mode Support (`client/messageparse.py`)
- Default: Markdown (Telegram-style with `**bold**`, `` `code` ``, `__italic__`)
- Also supports HTML (`<b>bold</b>`, `<i>italic</i>`, etc.)
- Configurable per-client: `client.parse_mode = 'html'` or `client.parse_mode = None`

### File Streaming / Download
- `iter_download()` -- async generator for streaming file downloads
- Supports CDN redirects, file reference refresh, DC migration
- Progress callbacks for upload/download

### Context Manager Support
- `SoroushClient` supports `async with` / `with` (calls `start()` / `disconnect()`)
- `Conversation` supports `async with` / `with`
- `_ChatAction` supports `async with` for typing indicators

### Album Handling (`events/album.py`)
- Automatically groups album messages via `grouped_id`
- Provides `AlbumHack` for cross-datacenter album delivery
- Album events support: `respond()`, `reply()`, `forward_to()`, `edit()`, `delete()`, `mark_read()`, `pin()`

---

## Public API (`__init__.py`)

```python
from spluspy import (
    SoroushClient, Client,         # Main client
    Button,                         # Button builder
    Session, MemorySession,         # Session types
    SQLiteSession, StringSession,
    Conversation, Message,          # Custom types
    Dialog, Forward, Draft,
    RateLimiter, RetryConfig,       # Rate limiting
    types, functions,               # Raw TL types/functions
    custom,                         # Custom module
    errors,                         # Error types
    events,                         # Event system
    utils,                          # Utilities
    connection                      # Connection types
)
```

**Version**: 1.0.1
