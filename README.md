
# ربات دانلود ویدیو از Pornhub برای تلگرام

یک ربات تلگرام ساده که توسط [پوریا حسینی](https://t.me/isPoori) ساخته شده است و به کاربران این امکان را می‌دهد که ویدیوهای سایت Pornhub را مستقیماً در تلگرام جستجو و دانلود کنند. این ربات از کتابخانه **yt-dlp** برای دانلود ویدیوها استفاده می‌کند و ویدیوهای دانلود شده را به طور مستقیم به کاربر ارسال می‌کند. این ربات برای کسانی که می‌خواهند به سرعت و بدون ترک تلگرام ویدیو دانلود کنند، بسیار مناسب است.

---

## ویژگی‌ها

- **جستجوی ویدیو**: آدرس لینک جستجو از سایت Pornhub را وارد کنید و ربات اولین ویدیو را پیدا می‌کند.
- **دانلود ویدیو**: ویدیوی انتخابی را مستقیماً به چت شما دانلود می‌کند.
- **راحتی استفاده**: با ارسال آدرس جستجو یا لینک مستقیم ویدیو با ربات تعامل کنید.
- **دانلود خودکار**: ربات دانلود ویدیو را به طور خودکار در پس‌زمینه انجام می‌دهد.

---

## پیش‌نیازها

قبل از اجرای ربات، باید چندین وابستگی را نصب کنید:

1. **پایتون 3.6 یا بالاتر**
2. **توکن ربات تلگرام** (میتوانید آن را از [@BotFather در تلگرام](https://t.me/BotFather) دریافت کنید)
3. **yt-dlp**: یک فورک از youtube-dl که برای دانلود ویدیوها استفاده می‌شود.
4. **Requests**: برای ارسال درخواست‌های HTTP به Pornhub.
5. **BeautifulSoup**: برای تجزیه محتوای HTML.
6. **کتابخانه تلگرام**: برای تعامل با API تلگرام.

---

## مراحل نصب

### 1. کلون کردن مخزن

مخزن این پروژه را به سیستم محلی خود کلون کنید:

```bash
git clone https://github.com/your-username/Telegram-Pornhub-Downloader.git
cd Telegram-Pornhub-Downloader
```

### 2. نصب وابستگی‌ها

مطمئن شوید که `pip` را نصب کرده‌اید و با استفاده از دستور زیر وابستگی‌های پایتون را نصب کنید:

```bash
pip install -r requirements.txt
```

فایل `requirements.txt` را با محتوای زیر ایجاد کنید:

```
python-telegram-bot
yt-dlp
requests
beautifulsoup4
```

### 3. تنظیم توکن ربات تلگرام

فایل `main.py` را باز کرده و `'TOKEN'` را با توکن ربات خود که از **@BotFather** دریافت کرده‌اید، جایگزین کنید:

```python
TOKEN = 'Token'
```

### 4. اجرای ربات

پس از تنظیمات، می‌توانید ربات را با دستور زیر اجرا کنید:

```bash
python3 main.py
```

ربات حالا در حال اجرا است و منتظر دریافت پیام‌ها می‌باشد.

---

## نحوه استفاده از ربات

### 1. شروع ربات

پس از راه‌اندازی ربات، می‌توانید با ارسال `/start` به ربات، از آن شروع کنید. ربات پاسخ خواهد داد با:

```
سلام! لینک جستجو یا ویدیو را بفرستید.
```

### 2. ارسال لینک جستجو یا لینک ویدیو

- برای جستجوی ویدیو، یک آدرس جستجوی مانند `https://www.pornhub.com/video/search?q=keyword` را ارسال کنید.
- برای دانلود ویدیو به صورت مستقیم، لینک ویدیو را ارسال کنید.

مثال از آدرس جستجو:

```
https://www.pornhub.com/video/search?q=funny
```

### 3. منتظر بمانید تا ربات ویدیو را دانلود کند

ربات پاسخ خواهد داد با پیام زیر:

```
در حال جستجو برای ویدیو، لطفاً منتظر بمانید...
```

سپس ویدیو را دانلود کرده و آن را به شما ارسال می‌کند.

---

## توضیح کد

- **`start()`**: این تابع زمانی که کاربر `/start` را ارسال می‌کند فعال می‌شود و پیام خوش‌آمدگویی ارسال می‌کند.
- **`fetch_pornhub_video_url()`**: این تابع آدرس جستجو را دریافت کرده، صفحه Pornhub را می‌خواند و اولین ویدیو را پیدا کرده و لینک آن را برمی‌گرداند.
- **`download_video()`**: این تابع ویدیو را با استفاده از **yt-dlp** دانلود کرده و فایل ویدیو را به کاربر ارسال می‌کند.
- **`handle_message()`**: این تابع پیام‌های دریافتی از کاربر را پردازش کرده و بررسی می‌کند که آیا لینک جستجو یا ویدیو معتبر است و سپس فرآیند دانلود را آغاز می‌کند.
- **`main()`**: تابع اصلی که ربات را راه‌اندازی کرده و منتظر دریافت پیام‌ها است.

---

## رفع اشکال

- **خطا در هنگام دانلود**: مطمئن شوید که **yt-dlp** به درستی نصب شده است. برای بررسی می‌توانید دستور `yt-dlp --version` را اجرا کنید.
- **ربات پاسخ نمی‌دهد**: مطمئن شوید که توکن ربات شما درست است و هیچ مشکلی در شبکه وجود ندارد.

---

## مجوز

این پروژه به صورت **Open-Source** و تحت [MIT License](LICENSE) منتشر شده است.

---

## نویسنده

این پروژه توسط **[پوریا حسینی](https://t.me/isPoori)** توسعه داده شده است. برای هرگونه سوال یا مشکل می‌توانید از طریق تلگرام با او تماس بگیرید.

---

## تقدیر و تشکر

- **yt-dlp**: برای مدیریت فرآیند دانلود ویدیو.
- **BeautifulSoup**: برای تجزیه HTML و استخراج لینک‌های ویدیو.
- **Telegram Bot API**: برای فراهم کردن امکان تعامل با تلگرام.

---

## سلب مسئولیت

این ربات صرفاً برای مقاصد آموزشی طراحی شده است و باید با مسئولیت کامل از آن استفاده کنید. اطمینان حاصل کنید که در استفاده از این ابزار قوانین و مقررات مربوطه را رعایت می‌کنید.
