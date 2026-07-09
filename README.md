<div align="center">

# SPlusPy

### کتابخانه پایتون برای تعامل با سروش پلاس

![Python](https://img.shields.io/badge/Python-3.5+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-GPL--3.0-green)
![Version](https://img.shields.io/badge/Version-1.0.1-orange)
![Platform](https://img.shields.io/badge/Platform-Soroush%20Plus-purple)

</div>

---

## فارسی

### SPlusPy چیه؟

**SPlusPy** یه کتابخانه پایتون asynchronous برای تعامل با پلتفرم [سروش پلاس](https://web.splus.ir) هست — هم به عنوان اکانت کاربری و هم ربات.

این کتابخانه از [Telethon](https://github.com/LonamiWebs/Telethon) fork شده و به طور اختصاصی برای اکوسیستم سروش پلاس سفارشی‌سازی شده با پشتیبانی از MTProto بومی، WebSocket transport و Layer 182.

### چرا SPlusPy؟

- **بدون نیاز به API Key** — کتابخانه خودش credentialهای سروش پلاس رو داره
- **کاملاً Asynchronous** — با `asyncio` پایتون
- **پشتیبانی از ربات و یوزر** — هر دو حالت
- **سیستم هندلر رویداد** — رویدادمحور و قدرتمند
- **دکمه‌های اینلاین و ریپلای** — کیبورد تعاملی
- **API مکالمه** — برای ربات‌های تعاملی
- **ورود با QR کد و شماره تلفن** — انعطاف‌پذیر
- **محدودیت نرخ و تلاش خودکار** — جلوگیری از بن شدن
- **سرعت بالا** — بهینه‌سازی شده با رمزنگاری سریع و صف‌های بهینه

### نصب

```bash
pip install -U splusthon
```

برای سرعت بیشتر در رمزنگاری:
```bash
pip install cryptg
```

### شروع سریع

#### ساده‌ترین ربات

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
    print('ربات فعال شد!')
    await bot.run_until_disconnected()

asyncio.run(main())
```

#### اکانت کاربری

```python
import asyncio
from spluspy import SoroushClient

client = SoroushClient('session_name')

@client.on_message(incoming=True, pattern='(?i)hello')
async def handler(event):
    await event.reply('Hey there!')

async def main():
    await client.start(phone='+98XXXXXXXXXX')
    print('وارد شدید!')
    await client.run_until_disconnected()

asyncio.run(main())
```

### انواع رویدادها

| رویداد | توضیح |
|---|---|
| `events.NewMessage` | پیام جدید دریافت شد |
| `events.MessageEdited` | پیام ویرایش شد |
| `events.CallbackQuery` | کلیک روی دکمه اینلاین |
| `events.ChatAction` | عضویت/خروج/سنجاق/تغییر عنوان |
| `events.InlineQuery` | کوئری اینلاین ربات |
| `events.UserUpdate` | آنلاین/آفلاین/تایپ کردن |
| `events.MessageDeleted` | پیام حذف شد |
| `events.MessageRead` | رسید خواندن دریافت شد |
| `events.Album` | آلبوم (گروه مدیا) دریافت شد |

### دکوراتورهای هندلر

| دکوراتور | معادل |
|---|---|
| `@client.on_message(...)` | `@client.on(events.NewMessage(...))` |
| `@client.on_edited(...)` | `@client.on(events.MessageEdited(...))` |
| `@client.on_callback_query(...)` | `@client.on(events.CallbackQuery(...))` |
| `@client.on_chat_action(...)` | `@client.on(events.ChatAction(...))` |
| `@client.on_inline_query(...)` | `@client.on(events.InlineQuery(...))` |
| `@client.on_user_update(...)` | `@client.on(events.UserUpdate(...))` |
| `@client.on_message_deleted(...)` | `@client.on(events.MessageDeleted(...))` |
| `@client.on_message_read(...)` | `@client.on(events.MessageRead(...))` |

### متدهای پیام

```python
# ارسال پیام
await client.send_message('username', 'سلام!')

# ارسال با دکمه
from spluspy import Button
await client.send_message('username', 'انتخاب کنید:', buttons=[
    [Button.inline('گزینه ۱', b'opt1'), Button.inline('گزینه ۲', b'opt2')]
])

# دریافت پیام‌ها
messages = await client.get_messages('username', limit=10)

# ویرایش پیام
await client.edit_message(msg, 'متن جدید')

# حذف پیام
await client.delete_messages(msg)

# فوروارد پیام
await client.forward_messages('destination', msg)

# تیک خواندن
await client.send_read_acknowledge(msg)
```

### ارسال فایل و رسانه

```python
# ارسال عکس
await client.send_photo(chat, 'photo.jpg')
await client.send_photo(chat, 'photo.jpg', caption='این عکسه!')

# ارسال موزیک
await client.send_audio(chat, 'song.mp3')
await client.send_audio(chat, 'song.mp3', caption='آهنگ مورد علاقه')

# ارسال ویس نوت
await client.send_audio(chat, 'voice.ogg', voice_note=True)

# ارسال ویدیو
await client.send_video(chat, 'video.mp4')
await client.send_video(chat, 'video.mp4', caption='این ویدیویه!')

# ارسال ویدیو دایره‌ای
await client.send_video(chat, 'round.mp4', video_note=True)

# ارسال فایل/سند
await client.send_document(chat, 'file.pdf')
await client.send_document(chat, 'report.docx', caption='گزارش ماهانه')

# ارسال فایل با پیشرفت آپلود
def callback(current, total):
    print(f'آپلود: {current}/{total}')

await client.send_file(chat, 'big_file.zip', progress_callback=callback)
```

### مدیریت چت (بن، کیک، پین)

```python
# بن کردن کاربر
await client.ban_chat_member(chat, user)

# بن موقت (۱ ساعت)
from datetime import timedelta
await client.ban_chat_member(chat, user, until_date=timedelta(hours=1))

# بن ولی اجازه مشاهده پیام‌ها
await client.ban_chat_member(chat, user, view_messages=False)

# آنبان کردن کاربر
await client.unban_chat_member(chat, user)

# کیک کردن کاربر
await client.kick_chat_member(chat, user)

# پین کردن پیام
await client.pin_message(chat, message)

# پین با اطلاع‌رسانی
await client.pin_message(chat, message, notify=True)

# آنپین کردن پیام
await client.unpin_message(chat, message)

# آنپین همه پیام‌ها
await client.unpin_all_messages(chat)
```

### مدیریت ادمین و دسترسی‌ها

```python
# ارتقاء به ادمین
await client.edit_admin(chat, user, pin_messages=True)

# تغییر دسترسی‌ها (محدود کردن)
await client.edit_permissions(chat, user, send_messages=False)

# حذف ادمین
await client.edit_admin(chat, user, is_admin=False)

# دریافت دسترسی‌ها
permissions = await client.get_permissions(chat, user)
```

### دکمه‌ها و کیبوردها

#### دکمه‌های اینلاین (زیر پیام)

```python
from spluspy import Button

# دکمه کالبک
Button.inline('کلیک کنید', b'callback_data')

# دکمه لینک
Button.url('بازدید', 'https://example.com')

# سوئیچ اینلاین
Button.switch_inline('جستجو', 'query')
```

#### کیبورد ریپلای (جایگزین کیبورد کاربر)

```python
# دکمه متن
Button.text('منو', resize=True)

# درخواست موقعیت
Button.request_location('اشتراک‌گذاری موقعیت')

# درخواست شماره
Button.request_phone('اشتراک‌گذاری شماره')

# پاک کردن کیبورد
Button.clear()
```

### احراز هویت

```python
# ورود با تلفن (تعاملی)
await client.start(phone='+98XXXXXXXXXX')

# ورود با توکن ربات
await client.start(bot_token='123456:ABC-DEF')

# ورود با QR کد
qr = await client.qr_login()
print(qr.url)
await qr.wait()

# احراز هویت دو مرحله‌ای
await client.edit_2fa(new_password='password', hint='راهنما')
```

### API مکالمه

```python
async with client.conversation('user', timeout=60) as conv:
    conv.send_message('اسمتون چیه؟')
    response = await conv.get_response()
    conv.send_message(f'سلام {response.text}!')
```

### انواع Session

| Session | توضیح |
|---|---|
| `MemorySession` | فقط در حافظه (با ریستارت از بین میره) |
| `SQLiteSession` | پیش‌فرض. فایل `.session` ذخیره میشه |
| `StringSession` | به صورت رشته base64 سریالایز میشه |

---

## English

### What is SPlusPy?

**SPlusPy** is an asynchronous Python 3 library for interacting with the [Soroush Plus](https://web.splus.ir) platform — as a user account or a bot account.

Built as a fork of [Telethon](https://github.com/LonamiWebs/Telethon), SPlusPy is adapted specifically for the Soroush Plus ecosystem with native MTProto, WebSocket transport, and Layer 182 support.

### Why SPlusPy?

- **No API Key Required** — Built-in Soroush Plus credentials
- **Fully Asynchronous** — Built with Python's `asyncio`
- **Bot & User Support** — Both account types
- **Event-Driven Handlers** — Powerful event system
- **Inline & Reply Buttons** — Interactive keyboards
- **Conversation API** — For interactive bot flows
- **QR Code & Phone Login** — Flexible authentication
- **Rate Limiting & Auto-Retry** — Prevent account bans
- **High Performance** — Optimized with fast encryption and efficient queues

### Installation

```bash
pip install -U splusthon
```

For faster encryption:
```bash
pip install cryptg
```

### Quick Start

#### Simplest Bot

```python
import asyncio
from spluspy import SoroushClient

bot = SoroushClient('my_bot')

@bot.on_message(incoming=True)
async def handler(event):
    if event.is_private and event.raw_text == 'Hello':
        await event.reply('Hi!')

async def main():
    await bot.start()
    print('Bot is running!')
    await bot.run_until_disconnected()

asyncio.run(main())
```

#### User Account

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

### Event Types

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

### Handler Decorators

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

### Message Methods

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

### Sending Files & Media

```python
# Send a photo
await client.send_photo(chat, 'photo.jpg')
await client.send_photo(chat, 'photo.jpg', caption='Check this out!')

# Send audio/music
await client.send_audio(chat, 'song.mp3')
await client.send_audio(chat, 'song.mp3', caption='My favorite song')

# Send voice note
await client.send_audio(chat, 'voice.ogg', voice_note=True)

# Send video
await client.send_video(chat, 'video.mp4')
await client.send_video(chat, 'video.mp4', caption='This is a video!')

# Send round video
await client.send_video(chat, 'round.mp4', video_note=True)

# Send document
await client.send_document(chat, 'file.pdf')
await client.send_document(chat, 'report.docx', caption='Monthly report')

# Send file with upload progress
def callback(current, total):
    print(f'Uploaded: {current}/{total}')

await client.send_file(chat, 'big_file.zip', progress_callback=callback)
```

### Chat Management (Ban, Kick, Pin)

```python
# Ban a user
await client.ban_chat_member(chat, user)

# Temporary ban (1 hour)
from datetime import timedelta
await client.ban_chat_member(chat, user, until_date=timedelta(hours=1))

# Ban but allow viewing messages
await client.ban_chat_member(chat, user, view_messages=False)

# Unban a user
await client.unban_chat_member(chat, user)

# Kick a user
await client.kick_chat_member(chat, user)

# Pin a message
await client.pin_message(chat, message)

# Pin with notification
await client.pin_message(chat, message, notify=True)

# Unpin a message
await client.unpin_message(chat, message)

# Unpin all messages
await client.unpin_all_messages(chat)
```

### Admin & Permissions Management

```python
# Promote to admin
await client.edit_admin(chat, user, pin_messages=True)

# Edit permissions (restrict)
await client.edit_permissions(chat, user, send_messages=False)

# Remove admin
await client.edit_admin(chat, user, is_admin=False)

# Get permissions
permissions = await client.get_permissions(chat, user)
```

### Buttons & Keyboards

#### Inline Buttons (under message)

```python
from spluspy import Button

# Callback button
Button.inline('Click me', b'callback_data')

# URL button
Button.url('Visit', 'https://example.com')

# Switch inline
Button.switch_inline('Search', 'query')
```

#### Reply Keyboard (replaces user keyboard)

```python
# Text button
Button.text('Menu', resize=True)

# Request location
Button.request_location('Share Location')

# Request phone
Button.request_phone('Share Phone')

# Clear keyboard
Button.clear()
```

### Authentication

```python
# Phone login (interactive)
await client.start(phone='+98XXXXXXXXXX')

# Bot token login
await client.start(bot_token='123456:ABC-DEF')

# QR code login
qr = await client.qr_login()
print(qr.url)
await qr.wait()

# Two-Factor Authentication
await client.edit_2fa(new_password='password', hint='hint')
```

### Conversation API

```python
async with client.conversation('user', timeout=60) as conv:
    conv.send_message('What is your name?')
    response = await conv.get_response()
    conv.send_message(f'Hello {response.text}!')
```

### Session Types

| Session | Description |
|---|---|
| `MemorySession` | In-memory only (lost on restart) |
| `SQLiteSession` | Default. Saved as `.session` file |
| `StringSession` | Serialized as base64 string |

---

## More Resources

- [API Reference](https://tl.spluspy.dev/)
- [Examples](spluspy_examples/)
- [GitHub](https://github.com/Itskillmaster/spluspy)

---

## Disclaimer

SPlusPy is an unofficial third-party library. Use it responsibly and ensure your applications comply with Soroush Plus's Terms of Service. Improper use may result in account restrictions.

---

## License

SPlusPy is open-source software distributed under the [GPL-3.0 License](LICENSE).

<div align="center">

**Made with love for the Soroush Plus community**

</div>
