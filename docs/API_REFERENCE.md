# API Reference — راهنمای سطح عمومی

> این راهنما نمای کلی بخش‌های مهم را توضیح می‌دهد. فهرست امضاهای استخراج‌شده از تمام فایل‌ها در `METHODS_CATALOG.md` قرار دارد.

## کلاینت سلف‌بات

ورود پیشنهادی:

```python
from spluspy.selfbot import Client, events, filters
```

`Client` نام جایگزین `SoroushClient` است. کلاینت سلف‌بات در `spluspy/client/soroushclient.py` و لایهٔ پایهٔ آن در `spluspy/client/telegrambaseclient.py` قرار دارد. متدهای درخواست در `spluspy/methods/` به دسته‌های مختلف تقسیم شده‌اند؛ برای مشاهدهٔ نام و امضای متدهای عمومی هر ماژول به کاتالوگ مراجعه کنید.

## کلاینت ربات رسمی

ورود پیشنهادی:

```python
from spluspy.bot import Bot, BotClient, Robot, filters
```

`Bot` و `BotClient` alias کلاس `Robot` هستند. سازنده از توکن و تنظیماتی مانند مسیر SQLite، تعداد retry، parse mode و rate limit پشتیبانی می‌کند.

متدهای چرخهٔ عمر:

- `start()` — شروع polling در محیط async
- `stop()` — درخواست توقف حلقهٔ اجرا
- `close()` — بستن session HTTP و پایگاه‌دادهٔ داخلی
- `start_webhook()` — اجرای webhook در محیط async
- `run_webhook()` — اجرای blocking برای اسکریپت مستقل
- `add_shutdown_hook()` — ثبت hook برای shutdown

دسته‌های اصلی متدهای API در `Robot` شامل `getMe`, `getUpdates`, `setWebhook`, `deleteWebhook`, `getWebhookInfo`, `sendMessage`, ارسال رسانه، مدیریت پیام، callback query، اطلاعات چت و دانلود فایل است. نام دقیق و پارامترها در کاتالوگ آمده است.

## مدل‌ها

مدل‌های HTTP در `spluspy.http_api.types` تعریف شده‌اند؛ از جمله `User`, `Chat`, `Message`, `Update`, `CallbackQuery`, `InlineQuery`, `File`, `PhotoSize`, `Document`, `Video` و مدل‌های صفحه‌کلید. این مدل‌ها با شکل پاسخ API سرویس هماهنگ شده‌اند و نباید با رویدادهای سلف‌بات یکی فرض شوند.

## رویدادها، فیلترها و middleware

- `spluspy.events`: رویدادهای سلف‌بات مانند پیام جدید، ویرایش/حذف پیام و عملیات چت.
- `spluspy.filters`: ترکیب فیلترها با `&`, `|` و `~`.
- `spluspy.middleware`: `BaseMiddleware`, `MiddlewareManager`, `MiddlewareStop`, `MiddlewareSkip`.
- `spluspy.fsm`: مدیریت state و context.
- `spluspy.plugins`: مدیریت افزونه‌ها.
- `spluspy.scheduler`: زمان‌بندی وظایف.
- `spluspy.sessions`: backendهای ذخیره‌سازی session.

## نکتهٔ سازگاری

API ربات رسمی و سلف‌بات به‌صورت جداگانه مستند شده‌اند چون transport، مدل رویداد، روش احراز هویت و قابلیت‌های سمت سرویس یکسان نیستند. متد جدید برای endpoint تأییدنشده اضافه نکنید؛ ابتدا قابلیت سرویس را بررسی و سپس تست integration بنویسید.
