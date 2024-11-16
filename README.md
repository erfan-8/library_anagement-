# سیستم مدیریت کتابخانه با پایتون و Tkinter

این پروژه یک اپلیکیشن گرافیکی برای مدیریت کتابخانه است که با استفاده از **پایتون** و رابط کاربری **Tkinter** ساخته شده است. دیتابیس این برنامه با استفاده از **SQLite3** مدیریت می‌شود. این سیستم امکان مدیریت اطلاعات کتاب‌ها را با یک رابط کاربری ساده و کاربرپسند فراهم می‌کند.

## امکانات

- **افزودن کتاب جدید**: ذخیره اطلاعات کتاب شامل عنوان، نویسنده، سال انتشار و کد ISBN.
- **مشاهده تمام کتاب‌ها**: نمایش تمام کتاب‌های ذخیره شده به صورت لیست.
- **جستجوی کتاب‌ها**: جستجو بر اساس عنوان، نویسنده، سال انتشار یا ISBN.
- **ویرایش اطلاعات کتاب‌ها**: تغییر اطلاعات کتاب‌های موجود.
- **حذف کتاب‌ها**: حذف رکورد کتاب‌های انتخاب شده از دیتابیس.
- **رابط کاربری ساده و زیبا**: استفاده از ویجت‌های Tkinter برای تعامل کاربر با برنامه.

## نحوه عملکرد

1. **Frontend (فایل `main.py`)**:
   - رابط کاربری گرافیکی برای تعامل کاربران.
   - امکان انجام عملیات مختلف مانند افزودن، ویرایش، حذف و جستجوی کتاب‌ها.
   - استفاده از ویجت‌های Tkinter مانند Label، Button، Entry و Listbox.

2. **Backend (فایل `backend.py`)**:
   - مدیریت دیتابیس با استفاده از SQLite3.
   - شامل توابع مختلف برای عملیات CRUD:
     - `insert`: افزودن کتاب جدید.
     - `view`: مشاهده تمام کتاب‌ها.
     - `search`: جستجوی کتاب.
     - `update`: ویرایش اطلاعات کتاب.
     - `delete`: حذف کتاب.
   - ذخیره اطلاعات به صورت دائمی در فایل دیتابیس `books.db`.

## فایل‌ها

- **`main.py`**: رابط کاربری گرافیکی برنامه.
- **`backend.py`**: مدیریت عملیات دیتابیس.

---

با استفاده از این سیستم می‌توانید به راحتی کتاب‌های خود را مدیریت کنید. اگر نظری داشتید یا مایل به مشارکت بودید، خوشحال می‌شویم با ما در میان بگذارید. 😊
