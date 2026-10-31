# spluspy


کتابخانهٔ async پایتون برای کار با سروش‌پلاس؛ شامل دو کلاینت مستقل:

- **Self-bot**: کار با حساب کاربری از طریق پیاده‌سازی socket/MTProto کتابخانه.
- **Official Bot**: کار با توکن ربات و HTTP Bot API رسمی.

> نکته: قابلیت‌های هر کلاینت تابع API و دسترسی‌های واقعی سرویس است. وجود متد در کتابخانه به‌تنهایی تضمین نمی‌کند که سرور آن عملیات را پشتیبانی کند.

## نصب

Python 3.9 یا بالاتر:

```bash
python -m pip install .
```

برای توسعه و اجرای تست‌ها:

```bash
python -m pip install -e ".[dev]"
python -m pytest
```

## انتخاب کلاینت

### 1) سلف‌بات

```python
from spluspy.selfbot import Client, events, filters

app = Client("my-session")

@app.on(events.NewMessage)
async def on_message(event):
    if event.raw_text == "سلام":
        await event.respond("سلام! 👋")

app.run()
```

کلاینت سلف‌بات از `spluspy.client.SoroushClient` استفاده می‌کند. امضای سازنده و روش احراز هویت را با نسخهٔ فعلی سورس و راهنمای مربوط به همان حساب بررسی کنید.

### 2) ربات رسمی

```python
import asyncio
from spluspy.bot import Bot, filters

bot = Bot("YOUR_BOT_TOKEN")

@bot.on_message(filters.text("/start"))
async def on_start(client, event):
    chat_id = getattr(event, "chat_id", None)
    if chat_id is not None:
        await client.sendMessage(chat_id, "سلام! ربات آماده است.")

async def main():
    await bot.start()

if __name__ == "__main__":
    asyncio.run(main())
```

نمونه‌ها باید متناسب با ساختار updateهای دریافتی و API فعال حساب شما تنظیم شوند؛ توکن را در سورس عمومی یا مخزن Git قرار ندهید.

## مسیرهای ایمپورت

```python
# روش قدیمی (برای سازگاری حفظ شده)
from spluspy import Client, Robot, filters

# روش روشن‌تر و پیشنهادی
from spluspy.selfbot import Client
from spluspy.bot import Bot, BotClient, Robot
```

`Bot` و `BotClient` نام‌های جایگزین برای کلاس `Robot` هستند؛ کلاس جدید یا کلاینت مستقل جداگانه‌ای ایجاد نمی‌کنند.

## امکانات موجود در سورس

- کلاینت سلف‌بات و متدهای شبکه/پیام‌رسانی
- کلاینت رسمی HTTP با polling و webhook
- مدل‌های پیام، کاربر، گروه، فایل و update
- فیلترها و هندلرهای پیام، callback، inline query و raw update
- middleware، FSM، سیستم پلاگین، scheduler، AFK و message mirror
- session storage و ابزارهای رمزنگاری

## رفتار در خطا و اتصال

- برای خطاهای شبکه، سیاست retry و محدودیت نرخ را بررسی کنید؛ همهٔ خطاها قابل retry نیستند.
- در production، logging را فعال کنید و توکن/کد ورود/اطلاعات سشن را در log چاپ نکنید.
- برای webhook، HTTPS و مسیر غیرقابل حدس را در زیرساخت خود تنظیم کنید؛ اعتبارسنجی secret token را مطابق امکانات API فعال کنید.
- sessionها و فایل‌های پایگاه‌داده را محرمانه نگه دارید.

## تست و توسعه

```bash
python -m compileall -q spluspy
python -m pytest
```

تست‌های این مخزن شامل بررسی ساختار، import surface و کامپایل هستند. برای ادعای سازگاری end-to-end باید تست‌های integration با محیط آزمایشی و endpointهای واقعی سروش‌پلاس نیز اجرا شوند.

## مستندات بیشتر

- [معماری و شروع سریع](docs/ARCHITECTURE.md)
- [راهنمای متدها و API](docs/API_REFERENCE.md)
- [امنیت و انتشار](docs/DEVELOPMENT.md)
- [فهرست متدهای استخراج‌شده از سورس](docs/METHODS_CATALOG.md)
