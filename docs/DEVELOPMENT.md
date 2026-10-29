# توسعه، تست و انتشار

## محیط توسعه

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## بررسی قبل از انتشار

```bash
python -m compileall -q spluspy
python -m pytest
python -m build
```

## چک‌لیست انتشار

- [ ] نسخه در `spluspy/version.py` و `pyproject.toml` هماهنگ باشد.
- [ ] تست‌ها روی نسخه‌های پشتیبانی‌شدهٔ Python اجرا شوند.
- [ ] هیچ توکن، session، شماره تلفن یا فایل محرمانه‌ای وارد بسته نشود.
- [ ] changelog و migration notes به‌روزرسانی شوند.
- [ ] نصب wheel در یک محیط تمیز تست شود.
- [ ] تست integration برای endpointهای فعال انجام شود.

## خط‌مشی سازگاری

نام‌های عمومی قدیمی حذف نشوند مگر با deprecation دوره‌دار. قابلیت جدیدی که endpoint آن تأیید نشده نباید به‌عنوان پشتیبانی قطعی مستند شود.
