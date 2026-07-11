<div align="center">

# SplusPy

**A modern async Python library for Soroush Plus**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Itskillmaster/spluspy/blob/main/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/spluspy)](https://pypi.org/project/spluspy/)
[![Python versions](https://img.shields.io/pypi/pyversions/spluspy)](https://pypi.org/project/spluspy/)
[![Downloads](https://img.shields.io/pypi/dm/spluspy)](https://pypi.org/project/spluspy/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](https://mypy-lang.org/)

[English](#-features) | [فارسی](#-ویژگی‌ها)

---

**SplusPy** is a modern, asynchronous Python library for interacting with [Soroush Plus](https://web.splus.ir) — both as a user account and a bot account.

Built from the ground up with clean architecture, it's designed to feel like [Telethon](https://github.com/LonamiWebs/Telethon) or [Pyrogram](https://github.com/pyrogram/pyrogram), but specifically for the Soroush Plus ecosystem.

**SplusPy** یک کتابخانه پایتون مدرن و ناهمگام (Asynchronous) برای تعامل با [سروش پلاس](https://web.splus.ir) است — هم به عنوان حساب کاربری و هم به عنوان حساب ربات.

این کتابخانه از صفر با معماری تمیز طراحی شده و الهام گرفته از [Telethon](https://github.com/LonamiWebs/Telethon) و [Pyrogram](https://github.com/pyrogram/pyrogram) است، اما مخصوص اکوسیستم سروش پلاس می‌باشد.

</div>

---

## English

### Features

| Feature | Description |
|---------|-------------|
| **No API Key Required** | Built-in Soroush Plus credentials |
| **Fully Asynchronous** | Built with Python's `asyncio` |
| **Sync Support** | Use without `async/await` via `spluspy.sync` |
| **Bot & User Support** | Both account types |
| **Event-Driven Handlers** | Powerful event system with decorators |
| **Filter System** | Composable filters (`&`, `\|`, `~`) |
| **Inline & Reply Buttons** | Interactive keyboards |
| **Conversation API** | For interactive bot flows |
| **FSM (Finite State Machine)** | Built-in state management for bots |
| **Plugin System** | Dynamic plugin loading |
| **Middleware** | Pre/post processing of updates |
| **Scheduler** | Built-in task scheduler |
| **Multiple Storage Backends** | Memory, SQLite, Redis, PostgreSQL |
| **Rate Limiting** | Token bucket algorithm with flood wait handling |
| **AFK Auto-Reply** | Smart auto-responder with per-chat rate limiting |
| **Chat Administration** | Ban, mute, pin, purge — high-level admin API |
| **Message Mirroring** | Real-time message cloning between chats |
| **Batch Operations** | Send, delete, forward multiple messages at once |
| **File Transfer with Progress** | Upload/download with progress tracking |
| **Professional Logging** | Structured, namespaced loggers |
| **Type Hints Everywhere** | Full type safety |
| **Clean Architecture** | SOLID principles, modular design |

### Requirements

- Python 3.10+
- No external API keys needed (built-in Soroush Plus credentials)

### Installation

```bash
pip install spluspy
```

For faster encryption:

```bash
pip install spluspy[speed]
```

With Redis backend:

```bash
pip install spluspy[redis]
```

With PostgreSQL backend:

```bash
pip install spluspy[postgres]
```

All optional dependencies:

```bash
pip install spluspy[all]
```

### Quick Start

#### Simplest Bot

```python
from spluspy import Client

bot = Client("my_session")

@bot.on_message()
async def handler(client, message):
    await message.reply("Hello!")

bot.run()
```

#### User Account

```python
from spluspy import Client

client = Client("session_name")

@client.on_message()
async def handler(client, message):
    await message.reply("Hey there!")

async def main():
    await client.start(phone="+98XXXXXXXXXX")
    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
```

#### Sync Usage (No Async/Await)

```python
from spluspy.sync import Client

bot = Client("session")

@bot.on_message()
def handler(client, message):
    message.reply("Hello!")

bot.run()
```

### Events

| Decorator | Event |
|-----------|-------|
| `@bot.on_message()` | New message |
| `@bot.on_edited()` | Message edited |
| `@bot.on_callback_query()` | Inline button clicked |
| `@bot.on_inline_query()` | Inline query |
| `@bot.on_chat_action()` | Join/leave/pin |
| `@bot.on_user_update()` | Status change |
| `@bot.on_message_deleted()` | Message deleted |
| `@bot.on_message_read()` | Read receipt |
| `@bot.on_error()` | Global error handling |

#### Event Priority

```python
from spluspy.events import HandlerPriority

@bot.on_message(priority=HandlerPriority.FIRST)
async def high_priority_handler(client, message):
    # Runs first
    pass

@bot.on_message(priority=HandlerPriority.LOW)
async def low_priority_handler(client, message):
    # Runs last
    pass
```

#### Stop Propagation

```python
@bot.on_message()
async def stopper(client, message):
    if message.text == "/stop":
        message.stop_propagation()
        await message.reply("Stopped!")
```

### Filters

```python
from spluspy import filters

@bot.on_message(filters.text)                    # Text only
@bot.on_message(filters.private)                 # Private chats
@bot.on_message(filters.group)                   # Groups
@bot.on_message(filters.command("start"))        # /start command
@bot.on_message(filters.regex(r"\d+"))           # Regex match
@bot.on_message(filters.user(123))               # Specific user
@bot.on_message(filters.text & filters.private)  # Combined
@bot.on_message(filters.photo | filters.video)   # Photo OR video
```

### Message Methods

```python
await message.reply("Hello")              # Reply
await message.edit("New text")            # Edit
await message.delete()                    # Delete
await message.forward(chat_id)            # Forward
await message.copy(chat_id)               # Copy (no forward header)
await message.pin()                       # Pin
await message.react("❤️")                 # React
await message.mark_read()                 # Mark as read
await message.download()                  # Download media
await message.reply_photo("photo.jpg")    # Reply with photo
await message.reply_video("video.mp4")    # Reply with video
await message.reply_document("file.pdf")  # Reply with document
```

### Buttons

```python
from spluspy import Button

# Inline keyboard
keyboard = Button.build_inline([
    Button.inline("Option 1", b"opt1"),
    Button.inline("Option 2", b"opt2")
])
await bot.send_message(chat_id, "Choose:", buttons=keyboard)

# Reply keyboard
kb = Button.build_reply([
    Button.text("Menu"),
    Button.text("Settings")
])
await bot.send_message(chat_id, "Pick:", buttons=kb)

# Clear keyboard
await bot.send_message(chat_id, "Done", buttons=Button.clear())
```

### FSM (Finite State Machine)

```python
from spluspy.fsm import State, StateMachine
from spluspy.storage import MemoryStorage

storage = MemoryStorage()
fsm = StateMachine(storage)

class Form:
    name = State()
    age = State()

@bot.on_message(filters.command("register"))
async def start_register(client, message):
    ctx = fsm.context(message.sender_id)
    await ctx.set_state(Form.name)
    await message.reply("What is your name?")

@bot.on_message(filters.private)
async def process_form(client, message):
    ctx = fsm.context(message.sender_id)
    state = await ctx.get_state()

    if state == Form.name:
        await ctx.set_data(name=message.text)
        await ctx.set_state(Form.age)
        await message.reply("How old are you?")
    elif state == Form.age:
        data = await ctx.get_data()
        await ctx.reset()
        await message.reply(f"Registered! Name: {data.get('name')}, Age: {message.text}")
```

#### Advanced FSM: State Routing with Decorators

```python
from spluspy.fsm import State, StateMachine, StateTransition
from spluspy.storage import SQLiteStorage

storage = SQLiteStorage("fsm.db")
sm = StateMachine(storage)

class Registration:
    name = State()
    age = State()
    complete = State()

@sm.state(Registration.name)
async def handle_name(ctx, message):
    await ctx.set(name=message.text)
    return StateTransition(to=Registration.age)

@sm.state(Registration.age)
async def handle_age(ctx, message):
    await ctx.set(age=message.text)
    return StateTransition(to=Registration.complete)

@sm.state(Registration.complete)
async def handle_complete(ctx, message):
    data = await ctx.get()
    await message.reply(f"Done: {data}")
    await ctx.finish()
```

### Storage Backends

```python
from spluspy.storage import MemoryStorage, SQLiteStorage, RedisStorage, PostgresStorage, get_storage

# Memory (default)
storage = MemoryStorage()

# SQLite
storage = SQLiteStorage("data.db")

# Redis
storage = RedisStorage(host="localhost", port=6379, db=0)

# PostgreSQL
storage = PostgresStorage(dsn="postgresql://user:pass@localhost/db")

# Factory function
storage = get_storage("redis", host="localhost")
```

### Plugin System

```python
# plugins/hello.py
def register(client):
    @client.on_message(filters.command("hello"))
    async def hello_handler(client, message):
        await message.reply("Hello from plugin!")
```

```python
# main.py
from spluspy import Client

bot = Client("session")
bot.plugins.load("plugins")
bot.run()
```

### Middleware

```python
from spluspy.middleware import Middleware

class LoggingMiddleware(Middleware):
    async def on_update(self, update, handler):
        print(f"Update received: {update}")
        result = await handler(update)
        print(f"Handler completed")
        return result

bot.middleware.add(LoggingMiddleware())
```

#### Rate Limiting Middleware

```python
from spluspy.middleware import RateLimitMiddleware

# 10 messages per minute
rate_limit = RateLimitMiddleware(max_messages=10, window_seconds=60)
bot.middleware.add(rate_limit)
```

### Rate Limiter

```python
from spluspy.utils import RateLimiter

limiter = RateLimiter(max_calls=10, period=60)

@bot.on_message()
async def limited_handler(client, message):
    if not limiter.allow():
        await message.reply("Rate limited! Try again later.")
        return
    await message.reply("OK")
```

### Cache

```python
from spluspy.utils import LRUCache

cache = LRUCache(maxsize=1000, ttl=300)  # 5 min TTL
cache.set("key", "value")
value = cache.get("key")
stats = cache.stats()  # {'hits': 42, 'misses': 3}
```

### AFK Auto-Reply

```python
from spluspy import Client, filters
from spluspy.afk import AfkManager

bot = Client("my_account")
afk = AfkManager(bot, message="I'm currently AFK. Back soon!")

@bot.on_message(filters.command("afk"))
async def set_afk(client, message):
    afk.set_afk(True, reason="Lunch break")
    await message.reply("I'm now AFK!")

@bot.on_message(filters.command("back"))
async def unset_afk(client, message):
    afk.set_afk(False)
    await message.reply(f"Back! Sent {afk.total_replies} auto-replies.")

@bot.on_message(filters.private & filters.incoming)
async def auto_reply(client, message):
    if afk.is_afk:
        await afk.handle(message)
```

### Chat Administration

```python
from spluspy.admin import ChatAdmin

admin = ChatAdmin(bot)

await admin.ban_user(chat_id, user_id)
await admin.unban_user(chat_id, user_id)
await admin.mute_user(chat_id, user_id)
await admin.unmute_user(chat_id, user_id)
await admin.pin_message(chat_id, message)
await admin.unpin_message(chat_id, message)
await admin.unpin_all(chat_id)
await admin.purge_messages(chat_id, limit=100)

# Bulk actions
await admin.bulk_action(chat_id, "ban", [user_id1, user_id2, user_id3])

# Admin log
events = await admin.get_admin_log(chat_id, limit=50)
```

### Message Mirroring

```python
from spluspy.mirror import MessageMirror

mirror = MessageMirror(bot)

# Add a mirroring route
mirror.add_route(
    source=-1001234567890,
    targets=[-1009876543210, -1001112223334],
    strip_forward=True,
    strip_sender=False,
    add_prefix="[Mirror]"
)

# Or build incrementally
mirror.add_source(-1001234567890)
mirror.add_target(-1009876543210)

await mirror.start()
```

### Scheduler

```python
from spluspy.scheduler.scheduler import MessageScheduler

scheduler = MessageScheduler(bot)

# Send a message every hour
scheduler.schedule_interval("hourly_greeting", chat_id, "Hello!", interval=3600)

# Send a message after a delay
scheduler.schedule_once("reminder", chat_id, "Don't forget!", delay=300)

# Cancel a scheduled task
scheduler.cancel("hourly_greeting")
```

### Chat Management

```python
await bot.ban_user(chat_id, user_id)
await bot.unban_user(chat_id, user_id)
await bot.mute_user(chat_id, user_id)
await bot.unmute_user(chat_id, user_id)
await bot.pin_message(chat_id, message)
await bot.unpin_message(chat_id, message)
await bot.join_chat(chat_id)
await bot.leave_chat(chat_id)
```

### Error Handling

```python
from spluspy import filters
from spluspy.errors import FloodWait, Unauthorized, BadRequest

@bot.on_message()
async def safe_handler(client, message):
    try:
        await message.reply("Hello!")
    except FloodWait as e:
        await asyncio.sleep(e.seconds)
    except Unauthorized:
        await message.reply("Not authorized!")
    except BadRequest as e:
        print(f"Bad request: {e}")
```

#### Global Error Handler

```python
from spluspy.events import ErrorHandlerBuilder

error_handler = ErrorHandlerBuilder()
error_handler.on(FloodWait)(lambda e: print(f"Flood wait: {e.seconds}s"))
error_handler.on(Unauthorized)(lambda e: print("Unauthorized"))

bot.on_error(error_handler.build())
```

### Batch Operations

```python
# Send multiple messages
messages = ["Hello 1", "Hello 2", "Hello 3"]
results = await bot.batch_send(chat_id, messages)

# Delete multiple messages
await bot.batch_delete(chat_id, [msg1, msg2, msg3])

# Forward multiple messages
await bot.batch_forward(chat_id, [msg1, msg2])
```

### File Transfer with Progress

```python
from spluspy.utils import ProgressTracker

# Upload with progress
tracker = ProgressTracker(on_progress=lambda p: print(f"{p.percent}%"))
await bot.send_document(chat_id, "large_file.zip", progress=tracker)

# Download with progress
await message.download(progress=tracker)
```

### CLI

```bash
# Run a bot
spluspy run bot.py

# Run with custom session name
spluspy run bot.py --session my_bot

# Get session info
spluspy session-info my_session.session

# Show version
spluspy version

# Validate a bot script for syntax errors
spluspy validate bot.py
```

### Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install spluspy
RUN pip install --no-cache-dir spluspy[all]

# Copy your bot script
COPY bot.py .

# Run the bot
CMD ["python", "bot.py"]
```

Build and run:

```bash
docker build -t my-spluspy-bot .
docker run -v ./sessions:/app/sessions my-spluspy-bot
```

### Project Structure

```
spluspy/
├── __init__.py          # Public API
├── __version__.py       # Version info
├── cli.py               # CLI entry point
├── config.py            # Configuration
├── compat.py            # Compatibility layer
├── afk.py               # AFK auto-responder
├── admin.py             # Chat administration
├── mirror.py            # Message mirroring engine
├── client/              # Client and conversation API
│   ├── client.py        # Main Client class
│   └── conversation.py  # Conversation API
├── models/              # Domain models (Message, User, Chat, Media, etc.)
├── events/              # Event types and builders
├── filters/             # Composable message filters
├── errors/              # Custom exception hierarchy
├── session/             # Session backends (SQLite, Memory, String)
├── network/             # TCP connections and connection pool
├── storage/             # Key-value storage backends
├── plugins/             # Plugin loader
├── middleware/          # Middleware system
├── fsm/                 # Finite state machine
├── scheduler/           # Task scheduler
├── utils/               # Logger, cache, helpers
├── sync/                # Synchronous client wrapper
└── _engine/             # Low-level MTProto engine
```

### Error Hierarchy

```
SplusPyError
├── SoroushPlusAPIError
│   ├── RPCError
│   │   ├── FloodWait
│   │   ├── Unauthorized
│   │   ├── BadRequest
│   │   │   ├── ChatNotFound
│   │   │   ├── UserNotFound
│   │   │   └── MessageNotFound
│   │   └── ...
│   ├── SessionExpiredError
│   └── SessionError
├── AuthError
├── ValidationError
├── JoinChatError
│   ├── InvalidInviteLinkError
│   ├── InviteLinkExpiredError
│   ├── ChatFullError
│   ├── ChatDeactivatedError
│   └── MembershipRequiredError
└── FloodWaitError (rate limiter)
```

---

## فارسی

### ویژگی‌ها

| ویژگی | توضیحات |
|-------|---------|
| **بدون نیاز به API Key** | کلیدهای سروش پلاس به صورت داخلی |
| **ناهمگام کامل** | ساخته شده با `asyncio` پایتون |
| **پشتیبانی از حالت همگام** | استفاده بدون `async/await` از طریق `spluspy.sync` |
| **پشتیبانی ربات و کاربر** | هر دو نوع حساب |
| **هندلرهای رویدادمحور** | سیستم رویداد قدرتمند با دکوراتورها |
| **سیستم فیلتر** | فیلترهای قابل ترکیب (`&`, `\|`, `~`) |
| **دکمه‌های اینلاین و ریپلای** | کیبوردهای تعاملی |
| **API مکالمه** | برای جریان‌های تعاملی ربات |
| **FSM (ماشین حالت محدود)** | مدیریت وضعیت داخلی برای ربات‌ها |
| **سیستم پلاگین** | بارگذاری پویای پلاگین‌ها |
| **میان‌افزار (Middleware)** | پردازش قبل/بعد از به‌روزرسانی‌ها |
| **زمان‌بند (Scheduler)** | زمان‌بندی داخلی وظایف |
| **بک‌اندهای ذخیره‌سازی متعدد** | حافظه، SQLite، Redis، PostgreSQL |
| **محدودیت نرخ (Rate Limiting)** | الگوریتم سطل توکن با مدیریت انتظار سیلاب |
| **پاسخ خودکار AFK** | پاسخگوی هوشمند با محدودیت نرخ به ازای هر چت |
| **مدیریت چت** | مسدود کردن، بی‌صدا کردن، سنجاق، پاکسازی — API مدیریتی |
| **آینه‌سازی پیام** | کلون کردن پیام و رسانه به صورت بلادرنگ بین چت‌ها |
| **عملیات دسته‌ای** | ارسال، حذف، فوروارد چندین پیام به صورت همزمان |
| **انتقال فایل با پیشرفت** | آپلود/دانلود با ردیابی پیشرفت |
| **لاگ حرفه‌ای** | لاگرهای ساختاریافته و فضای نام‌دار |
| **نوع‌نویسی در همه جا** | ایمنی کامل نوع |
| **معماری تمیز** | اصول SOLID، طراحی ماژولار |

### پیش‌نیازها

- پایتون 3.10 به بالا
- نیازی به کلید API خارجی نیست (کلیدهای سروش پلاس به صورت داخلی)

### نصب

```bash
pip install spluspy
```

برای رمزگذاری سریع‌تر:

```bash
pip install spluspy[speed]
```

با بک‌اند Redis:

```bash
pip install spluspy[redis]
```

با بک‌اند PostgreSQL:

```bash
pip install spluspy[postgres]
```

همه وابستگی‌های اختیاری:

```bash
pip install spluspy[all]
```

### شروع سریع

#### ساده‌ترین ربات

```python
from spluspy import Client

bot = Client("my_session")

@bot.on_message()
async def handler(client, message):
    await message.reply("سلام!")

bot.run()
```

#### حساب کاربری

```python
from spluspy import Client

client = Client("session_name")

@client.on_message()
async def handler(client, message):
    await message.reply("سلام دنیا!")

async def main():
    await client.start(phone="+98XXXXXXXXXX")
    await client.run_until_disconnected()

import asyncio
asyncio.run(main())
```

#### استفاده همگام (بدون Async/Await)

```python
from spluspy.sync import Client

bot = Client("session")

@bot.on_message()
def handler(client, message):
    message.reply("سلام!")

bot.run()
```

### رویدادها

| دکوراتور | رویداد |
|----------|--------|
| `@bot.on_message()` | پیام جدید |
| `@bot.on_edited()` | ویرایش پیام |
| `@bot.on_callback_query()` | کلیک دکمه اینلاین |
| `@bot.on_inline_query()` | کوئری اینلاین |
| `@bot.on_chat_action()` | پیوستن/خروج/سنجاق |
| `@bot.on_user_update()` | تغییر وضعیت |
| `@bot.on_message_deleted()` | حذف پیام |
| `@bot.on_message_read()` | رسید خواندن |
| `@bot.on_error()` | مدیریت خطای سراسری |

#### اولویت رویداد

```python
from spluspy.events import HandlerPriority

@bot.on_message(priority=HandlerPriority.FIRST)
async def high_priority_handler(client, message):
    # اول اجرا می‌شود
    pass

@bot.on_message(priority=HandlerPriority.LOW)
async def low_priority_handler(client, message):
    # آخر اجرا می‌شود
    pass
```

#### توقف انتشار

```python
@bot.on_message()
async def stopper(client, message):
    if message.text == "/stop":
        message.stop_propagation()
        await message.reply("توقف!")
```

### فیلترها

```python
from spluspy import filters

@bot.on_message(filters.text)                    # فقط متن
@bot.on_message(filters.private)                 # چت‌های خصوصی
@bot.on_message(filters.group)                   # گروه‌ها
@bot.on_message(filters.command("start"))        # دستور /start
@bot.on_message(filters.regex(r"\d+"))           # تطابق با عبارت باقاعده
@bot.on_message(filters.user(123))               # کاربر خاص
@bot.on_message(filters.text & filters.private)  # ترکیبی
@bot.on_message(filters.photo | filters.video)   # عکس یا ویدیو
```

### متدهای پیام

```python
await message.reply("سلام")              # پاسخ
await message.edit("متن جدید")           # ویرایش
await message.delete()                    # حذف
await message.forward(chat_id)            # فوروارد
await message.copy(chat_id)               # کپی (بدون هدر فوروارد)
await message.pin()                       # سنجاق
await message.react("❤️")                 # واکنش
await message.mark_read()                 # علامت خواندن
await message.download()                  # دانلود رسانه
await message.reply_photo("photo.jpg")    # پاسخ با عکس
await message.reply_video("video.mp4")    # پاسخ با ویدیو
await message.reply_document("file.pdf")  # پاسخ با سند
```

### دکمه‌ها

```python
from spluspy import Button

# کیبورد اینلاین
keyboard = Button.build_inline([
    Button.inline("گزینه ۱", b"opt1"),
    Button.inline("گزینه ۲", b"opt2")
])
await bot.send_message(chat_id, "انتخاب کنید:", buttons=keyboard)

# کیبورد ریپلای
kb = Button.build_reply([
    Button.text("منو"),
    Button.text("تنظیمات")
])
await bot.send_message(chat_id, "انتخاب کنید:", buttons=kb)

# حذف کیبورد
await bot.send_message(chat_id, "تمام", buttons=Button.clear())
```

### FSM (ماشین حالت محدود)

```python
from spluspy.fsm import State, StateMachine
from spluspy.storage import MemoryStorage

storage = MemoryStorage()
fsm = StateMachine(storage)

class Form:
    name = State()
    age = State()

@bot.on_message(filters.command("register"))
async def start_register(client, message):
    ctx = fsm.context(message.sender_id)
    await ctx.set_state(Form.name)
    await message.reply("نام شما چیست؟")

@bot.on_message(filters.private)
async def process_form(client, message):
    ctx = fsm.context(message.sender_id)
    state = await ctx.get_state()

    if state == Form.name:
        await ctx.set_data(name=message.text)
        await ctx.set_state(Form.age)
        await message.reply("سن شما چقدر است؟")
    elif state == Form.age:
        data = await ctx.get_data()
        await ctx.reset()
        await message.reply(f"ثبت شد! نام: {data.get('name')}, سن: {message.text}")
```

#### FSM پیشرفته: مسیریابی وضعیت با دکوراتور

```python
from spluspy.fsm import State, StateMachine, StateTransition
from spluspy.storage import SQLiteStorage

storage = SQLiteStorage("fsm.db")
sm = StateMachine(storage)

class Registration:
    name = State()
    age = State()
    complete = State()

@sm.state(Registration.name)
async def handle_name(ctx, message):
    await ctx.set(name=message.text)
    return StateTransition(to=Registration.age)

@sm.state(Registration.age)
async def handle_age(ctx, message):
    await ctx.set(age=message.text)
    return StateTransition(to=Registration.complete)

@sm.state(Registration.complete)
async def handle_complete(ctx, message):
    data = await ctx.get()
    await message.reply(f"تمام شد: {data}")
    await ctx.finish()
```

### بک‌اندهای ذخیره‌سازی

```python
from spluspy.storage import MemoryStorage, SQLiteStorage, RedisStorage, PostgresStorage, get_storage

# حافظه (پیش‌فرض)
storage = MemoryStorage()

# SQLite
storage = SQLiteStorage("data.db")

# Redis
storage = RedisStorage(host="localhost", port=6379, db=0)

# PostgreSQL
storage = PostgresStorage(dsn="postgresql://user:pass@localhost/db")

# تابع کارخانه
storage = get_storage("redis", host="localhost")
```

### سیستم پلاگین

```python
# plugins/hello.py
def register(client):
    @client.on_message(filters.command("hello"))
    async def hello_handler(client, message):
        await message.reply("سلام از پلاگین!")
```

```python
# main.py
from spluspy import Client

bot = Client("session")
bot.plugins.load("plugins")
bot.run()
```

### میان‌افزار (Middleware)

```python
from spluspy.middleware import Middleware

class LoggingMiddleware(Middleware):
    async def on_update(self, update, handler):
        print(f"به‌روزرسانی دریافت شد: {update}")
        result = await handler(update)
        print(f"هندلر تکمیل شد")
        return result

bot.middleware.add(LoggingMiddleware())
```

#### میان‌افزار محدودیت نرخ

```python
from spluspy.middleware import RateLimitMiddleware

# ۱۰ پیام در دقیقه
rate_limit = RateLimitMiddleware(max_messages=10, window_seconds=60)
bot.middleware.add(rate_limit)
```

### محدودیت نرخ

```python
from spluspy.utils import RateLimiter

limiter = RateLimiter(max_calls=10, period=60)

@bot.on_message()
async def limited_handler(client, message):
    if not limiter.allow():
        await message.reply("محدودیت نرخ! دوباره تلاش کنید.")
        return
    await message.reply("باشه")
```

### کش

```python
from spluspy.utils import LRUCache

cache = LRUCache(maxsize=1000, ttl=300)  # TTL ۵ دقیقه‌ای
cache.set("key", "value")
value = cache.get("key")
stats = cache.stats()  # {'hits': 42, 'misses': 3}
```

### پاسخ خودکار AFK

```python
from spluspy import Client, filters
from spluspy.afk import AfkManager

bot = Client("my_account")
afk = AfkManager(bot, message="الان AFK هستم. زود برمی‌گردم!")

@bot.on_message(filters.command("afk"))
async def set_afk(client, message):
    afk.set_afk(True, reason="ناهار")
    await message.reply("الان AFK هستم!")

@bot.on_message(filters.command("back"))
async def unset_afk(client, message):
    afk.set_afk(False)
    await message.reply(f"برگشتم! {afk.total_replies} پاسخ خودکار ارسال شد.")

@bot.on_message(filters.private & filters.incoming)
async def auto_reply(client, message):
    if afk.is_afk:
        await afk.handle(message)
```

### مدیریت چت

```python
from spluspy.admin import ChatAdmin

admin = ChatAdmin(bot)

await admin.ban_user(chat_id, user_id)      # مسدود کردن
await admin.unban_user(chat_id, user_id)    # رفع مسدودیت
await admin.mute_user(chat_id, user_id)     # بی‌صدا کردن
await admin.unmute_user(chat_id, user_id)   # رفع بی‌صدایی
await admin.pin_message(chat_id, message)   # سنجاق کردن
await admin.unpin_message(chat_id, message) # رفع سنجاق
await admin.unpin_all(chat_id)              # رفع همه سنجاق‌ها
await admin.purge_messages(chat_id, limit=100) # پاکسازی پیام‌ها

# عملیات دسته‌ای
await admin.bulk_action(chat_id, "ban", [user_id1, user_id2])

# لاگ مدیریتی
events = await admin.get_admin_log(chat_id, limit=50)
```

### آینه‌سازی پیام

```python
from spluspy.mirror import MessageMirror

mirror = MessageMirror(bot)

# افزودن مسیر آینه‌سازی
mirror.add_route(
    source=-1001234567890,
    targets=[-1009876543210, -1001112223334],
    strip_forward=True,
    strip_sender=False,
    add_prefix="[Mirror]"
)

# یا به صورت تدریجی
mirror.add_source(-1001234567890)
mirror.add_target(-1009876543210)

await mirror.start()
```

### زمان‌بند

```python
from spluspy.scheduler.scheduler import MessageScheduler

scheduler = MessageScheduler(bot)

# ارسال پیام هر ساعت
scheduler.schedule_interval("hourly_greeting", chat_id, "سلام!", interval=3600)

# ارسال پیام با تاخیر
scheduler.schedule_once("reminder", chat_id, "فراموش نکن!", delay=300)

# لغو وظیفه زمان‌بندی شده
scheduler.cancel("hourly_greeting")
```

### مدیریت خطا

```python
from spluspy import filters
from spluspy.errors import FloodWait, Unauthorized, BadRequest

@bot.on_message()
async def safe_handler(client, message):
    try:
        await message.reply("سلام!")
    except FloodWait as e:
        await asyncio.sleep(e.seconds)
    except Unauthorized:
        await message.reply("غیرمجاز!")
    except BadRequest as e:
        print(f"درخواست نادرست: {e}")
```

#### هندل خطای سراسری

```python
from spluspy.events import ErrorHandlerBuilder

error_handler = ErrorHandlerBuilder()
error_handler.on(FloodWait)(lambda e: print(f"انتظار سیلاب: {e.seconds} ثانیه"))
error_handler.on(Unauthorized)(lambda e: print("غیرمجاز"))

bot.on_error(error_handler.build())
```

### عملیات دسته‌ای

```python
# ارسال چندین پیام
messages = ["سلام ۱", "سلام ۲", "سلام ۳"]
results = await bot.batch_send(chat_id, messages)

# حذف چندین پیام
await bot.batch_delete(chat_id, [msg1, msg2, msg3])

# فوروارد چندین پیام
await bot.batch_forward(chat_id, [msg1, msg2])
```

### انتقال فایل با پیشرفت

```python
from spluspy.utils import ProgressTracker

# آپلود با پیشرفت
tracker = ProgressTracker(on_progress=lambda p: print(f"{p.percent}%"))
await bot.send_document(chat_id, "فایل_بزرگ.zip", progress=tracker)

# دانلود با پیشرفت
await message.download(progress=tracker)
```

### رابط خط فرمان (CLI)

```bash
# اجرای ربات
spluspy run bot.py

# اجرا با نشست سفارشی
spluspy run bot.py --session my_bot

# اطلاعات نشست
spluspy session-info my_session.session

# نمایش نسخه
spluspy version

# اعتبارسنجی اسکریپت ربات
spluspy validate bot.py
```

### Docker

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# نصب وابستگی‌های سیستمی
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# نصب spluspy
RUN pip install --no-cache-dir spluspy[all]

# کپی اسکریپت ربات
COPY bot.py .

# اجرای ربات
CMD ["python", "bot.py"]
```

ساخت و اجرا:

```bash
docker build -t my-spluspy-bot .
docker run -v ./sessions:/app/sessions my-spluspy-bot
```

### ساختار پروژه

```
spluspy/
├── __init__.py          # API عمومی
├── __version__.py       # اطلاعات نسخه
├── cli.py               # نقطه ورود CLI
├── config.py            # پیکربندی
├── compat.py            # لایه سازگاری
├── afk.py               # پاسخگوی خودکار AFK
├── admin.py             # مدیریت چت
├── mirror.py            # موتور آینه‌سازی پیام
├── client/              # کلاینت و API مکالمه
│   ├── client.py        # کلاس اصلی Client
│   └── conversation.py  # API مکالمه
├── models/              # مدل‌های دامنه (Message, User, Chat, Media, و غیره)
├── events/              # انواع رویداد و بیلدرها
├── filters/             # فیلترهای قابل ترکیب پیام
├── errors/              # سلسله مراتب استثنای سفارشی
├── session/             # بک‌اندهای نشست (SQLite, Memory, String)
├── network/             # اتصالات TCP و استخر اتصال
├── storage/             # بک‌اندهای ذخیره‌سازی کلید-مقدار
├── plugins/             # بارگذار پلاگین
├── middleware/          # سیستم میان‌افزار
├── fsm/                 # ماشین حالت محدود
├── scheduler/           # زمان‌بند وظایف
├── utils/               # لاگر، کش، کمک‌کننده‌ها
├── sync/                # کلاینت همگام‌سازی شده
└── _engine/             # موتور MTProto سطح پایین
```

### سلسله مراتب خطاها

```
SplusPyError
├── SoroushPlusAPIError
│   ├── RPCError
│   │   ├── FloodWait
│   │   ├── Unauthorized
│   │   ├── BadRequest
│   │   │   ├── ChatNotFound
│   │   │   ├── UserNotFound
│   │   │   └── MessageNotFound
│   │   └── ...
│   ├── SessionExpiredError
│   └── SessionError
├── AuthError
├── ValidationError
├── JoinChatError
│   ├── InvalidInviteLinkError
│   ├── InviteLinkExpiredError
│   ├── ChatFullError
│   ├── ChatDeactivatedError
│   └── MembershipRequiredError
└── FloodWaitError (محدودیت نرخ)
```

---

## Contributing / مشارکت

### English

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Set up the development environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e ".[dev]"
   ```
4. Make your changes
5. Run linting and formatting:
   ```bash
   ruff check spluspy/
   black spluspy/
   ```
6. Run type checking:
   ```bash
   mypy spluspy/
   ```
7. Run tests: `pytest`
8. Submit a pull request

### فارسی

1. مخزن را Fork کنید
2. شاخه ویژگی بسازید (`git checkout -b feature/your-feature`)
3. محیط توسعه را راه‌اندازی کنید:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -e ".[dev]"
   ```
4. تغییرات خود را اعمال کنید
5. لینتر و فرمت‌کننده را اجرا کنید:
   ```bash
   ruff check spluspy/
   black spluspy/
   ```
6. بررسی نوع را اجرا کنید:
   ```bash
   mypy spluspy/
   ```
7. تست‌ها را اجرا کنید: `pytest`
8. درخواست Pull ارسال کنید

---

## License / مجوز

MIT License — see [LICENSE](LICENSE) for details.

مجوز MIT — جزئیات را در [LICENSE](LICENSE) مشاهده کنید.

---

## Disclaimer / سلب مسئولیت

**English:**
SPlusPy is an unofficial third-party library. Use it responsibly and ensure your applications comply with Soroush Plus's Terms of Service.

**فارسی:**
SPlusPy یک کتابخانه غیررسمی و شخص ثالث است. مسئولانه از آن استفاده کنید و مطمئن شوید برنامه‌های شما با شرایط استفاده سروش پلاس مطابقت دارند.

---

<div align="center">

**Made with ❤️ for the Soroush Plus community**

**ساخته شده با ❤️ برای جامعه سروش پلاس**

</div>
