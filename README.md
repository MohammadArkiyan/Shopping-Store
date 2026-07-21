<div align="center">

# 🛒 Shopping Store

**[فارسی](#فارسی) | [English](#english)**

</div>

---

<a id="english"></a>
## English

A complete, fully functional online shopping platform built with **Django** on the backend and **HTML, CSS, Bootstrap, jQuery, JavaScript** on the frontend.

![Python](https://img.shields.io/badge/python-3.x-blue)
![Django](https://img.shields.io/badge/django-framework-092E20?logo=django)
![License](https://img.shields.io/badge/license-MIT-orange)
![Status](https://img.shields.io/badge/status-completed-brightgreen)

> 🎨 **Frontend Credit:** The frontend template used in this project is based on a design by [HTMLCodex](https://htmlcodex.com/). All rights to the original frontend design belong to HTMLCodex. Only custom modifications and personalization were applied to the frontend in this project — all backend logic, Django integration, and dynamic functionality were fully implemented by me.

### 📋 Table of Contents
- [About the Project](#-about-the-project)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Routes](#-routes)
- [Installation](#-installation)
- [Admin Panel](#-admin-panel)
- [Technical Notes](#-technical-notes)
- [Security](#-security)
- [Credits](#-credits)
- [License](#-license)
- [Contact](#-contact)

---

### 📖 About the Project

**Shopping Store** is a complete e-commerce platform built to demonstrate advanced web development concepts with Django. It offers product management, a smart shopping cart, order processing, user management, discount coupons, user reviews, and a fully responsive UI.

---

### ✨ Features

#### Product Management
- Add, edit, and delete products from the admin panel
- Category management
- Product listing with full details (name, price, description, images, category)
- Filter products by price, size, and color (AJAX, no page refresh)
- **Live Search** via AJAX — results appear once the search term is 2+ characters
- Paginator to control the number of products shown per page

#### Shopping Cart
- Select products to purchase, with add/remove/edit quantity options
- Cart stored in **Session** — for both guest and logged-in users
- Guest users' cart items are automatically saved to the database upon login
- Automatic total price calculation
- Real-time (AJAX) update of cart item count in the Navbar, without page refresh
- Real-time price updates when quantities change on the cart page

#### Orders & Checkout
- Order placement and user address management
- Automatically pre-fills the Checkout form with the last used address (editable)
- Order list view for both users and admin, with order status updates

#### Users & Profile
- Secure sign-up and login with password hashing
- Profile editing: name, email, profile picture
- Profile info displayed in the "My Account" section (visible only to logged-in users)

#### Coupons
- Create unique discount codes from the admin panel
- Apply discount codes on the cart page with instant total recalculation
- Expired coupons are rejected with an appropriate error message

#### User Reviews
- Users can leave a review on the product detail page (logged-in users only)
- Reviews are shown publicly only after admin approval (via the *Publication Status* checkbox)

#### Other
- Contact form; messages are sent directly to the admin panel
- Fully responsive design for mobile, tablet, and desktop
- Dynamic homepage sections: **Categories**, **Featured Products**, and **Recent Products** (max 8 items)
- Rotating vendor logo carousel powered by JavaScript

---

### 🛠 Tech Stack

**Backend:**
- Python
- Django

**Frontend:**
- HTML5 / CSS3
- Bootstrap
- JavaScript / jQuery (AJAX for cart, filters, live search, etc.)
- Base template by [HTMLCodex](https://htmlcodex.com/), with custom modifications

**Database:**
- SQLite (for development and testing)

---

### 📁 Project Structure

```
shoppingstore_project/
├── manage.py                # Main Django management script
├── db.sqlite3                # SQLite database
├── requirements.txt           # Python dependencies
├── static/                    # Static files (CSS, JS, images)
├── media/                     # User-uploaded files
├── templates/                  # Base template (shared across pages)
│
├── shoppingstore/               # Home page app
├── account/                    # User app (signup, login, profile)
├── product/                    # Products, categories, and product details
├── cart/                       # Shopping cart app
├── checkout/                   # Final order/checkout form app
├── coupon/                     # Discount coupon app (on the cart page)
└── contact/                    # Contact us app
```

---

### 🔗 Routes

| Section | URL | Description |
|---|---|---|
| Home | `/` | Homepage |
| Login | `/account/login` | Login page |
| Sign up | `/account/signup` | Registration page |
| Profile | `/account/profile` | View and edit profile |
| Cart | `/cart` | Shopping cart page |
| Checkout | `/checkout` | Shipping/order details form |
| Contact | `/contact` | Contact form |
| Shop | `/shop` | Product listing, filters, and paginator |
| Product Detail | `/shop/detail/<product_id>` | Product details + reviews section |
| Admin Panel | `/admin` | Full site management |

---

### 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/username/shopping-store.git
cd shopping-store

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create a superuser for admin panel access
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

The project will be available at:
```
http://127.0.0.1:8000
```

---

### 🔑 Admin Panel

Access the admin panel at:
```
http://127.0.0.1:8000/admin
```

> ⚠️ **Security note:** The `admin/admin` credentials are for the development environment only. Before deploying this project to production, make sure to create a superuser with a strong, unique username and password, and never commit login credentials to a public repository.

From the admin panel you can fully manage products, categories, users, orders, discount coupons, and reviews.

---

### 📌 Technical Notes

- The **Categories** section on the homepage only displays categories marked as *Featured* in the admin panel.
- The **Featured Products** section only shows products with the *is_featured* field checked in the admin panel.
- The **Recent Products** section displays the most recently added products (up to 8 items).
- On the Checkout page, if a user has previously filled out the form, it is automatically pre-filled on subsequent visits (and remains editable). Saved addresses can be viewed under the *Addresses* section in the admin panel.

---

### 🔒 Security

- User passwords are hashed using strong algorithms
- Protection against **XSS** and **CSRF** attacks

---

### 🙏 Credits

- **Frontend Design:** The base frontend template for this project was designed by [HTMLCodex](https://htmlcodex.com/). Only custom modifications and personalizations were made to this template in this project; all backend logic and Django development were carried out by me.

---

### 📄 License

This project is licensed under the MIT License — see the LICENSE file for details. Note that the frontend template remains subject to the original license terms of [HTMLCodex](https://htmlcodex.com/).

### 📬 Contact

**Mohammad Arkian**

If you have any questions or suggestions, feel free to reach out via the Issues tab of this repository, or through:
- Email: mohammadarkiyan21@gmail.com
- GitHub: https://github.com/MohammadArkiyan

<div align="right">

[⬆ Back to top](#shopping-store)

</div>

---

<a id="فارسی"></a>
## فارسی

فروشگاه آنلاین کامل و کاربردی، ساخته‌شده با **Django** در بک‌اند و **HTML, CSS, Bootstrap, jQuery, JavaScript** در فرانت‌اند.

![Python](https://img.shields.io/badge/python-3.x-blue)
![Django](https://img.shields.io/badge/django-framework-092E20?logo=django)
![License](https://img.shields.io/badge/license-MIT-orange)
![Status](https://img.shields.io/badge/status-completed-brightgreen)

> 🎨 **اعتبار طراحی فرانت‌اند:** قالب فرانت‌اند این پروژه بر پایه‌ی طراحی [HTMLCodex](https://htmlcodex.com/) است. تمام حقوق طراحی اولیه‌ی فرانت‌اند متعلق به HTMLCodex می‌باشد؛ در این پروژه صرفاً تغییرات و شخصی‌سازی‌های سفارشی (Custom) روی بخش فرانت‌اند اعمال شده و منطق بک‌اند، اتصال به Django و قابلیت‌های داینامیک به‌طور کامل توسط من پیاده‌سازی شده است.

### 📋 فهرست مطالب
- [درباره پروژه](#-درباره-پروژه)
- [قابلیت‌ها](#-قابلیتها)
- [تکنولوژی‌های استفاده‌شده](#-تکنولوژیهای-استفادهشده)
- [ساختار پروژه](#-ساختار-پروژه)
- [آدرس‌های پروژه (Routes)](#-آدرسهای-پروژه-routes)
- [نصب و راه‌اندازی](#-نصب-و-راهاندازی)
- [پنل ادمین](#-پنل-ادمین)
- [نکات فنی](#-نکات-فنی)
- [امنیت](#-امنیت)
- [اعتبارها](#-اعتبارها)
- [لایسنس](#-لایسنس)
- [تماس](#-تماس)

---

### 📖 درباره پروژه

**Shopping Store** یک پلتفرم فروشگاهی کامل است که با هدف پیاده‌سازی مفاهیم پیشرفته توسعه‌ی وب با Django طراحی شده. این پروژه امکاناتی نظیر مدیریت محصولات، سبد خرید هوشمند، سفارش‌گذاری، مدیریت کاربران، کد تخفیف، نظرات کاربران و رابط کاربری کاملاً واکنش‌گرا (Responsive) را ارائه می‌دهد.

---

### ✨ قابلیت‌ها

#### مدیریت محصولات
- افزودن، ویرایش و حذف محصولات از طریق پنل ادمین
- مدیریت دسته‌بندی‌ها (Categories)
- نمایش لیست محصولات با جزئیات کامل (نام، قیمت، توضیحات، تصاویر، دسته‌بندی)
- فیلتر محصولات بر اساس قیمت، سایز و رنگ (AJAX، بدون رفرش صفحه)
- **جستجوی زنده (Live Search)** با AJAX — از ۲ کاراکتر به بعد نتیجه نمایش داده می‌شود
- Paginator برای کنترل تعداد محصولات نمایشی در هر صفحه

#### سبد خرید (Cart)
- انتخاب محصول برای خرید با امکان افزودن/حذف/ویرایش تعداد
- ذخیره‌سازی سبد خرید در **Session** — هم برای کاربران مهمان و هم کاربران وارد‌شده
- انتقال خودکار سبد خرید کاربر مهمان به دیتابیس پس از ورود (Login)
- محاسبه‌ی خودکار جمع کل قیمت
- بروزرسانی آنی (AJAX) تعداد آیتم‌های سبد خرید در Navbar، بدون رفرش صفحه
- بروزرسانی آنی قیمت‌ها هنگام تغییر تعداد کالا در صفحه سبد خرید

#### سفارش‌گذاری و Checkout
- ثبت سفارش و مدیریت آدرس‌های کاربر
- استفاده‌ی خودکار از آخرین آدرس ثبت‌شده در فرم Checkout (با امکان ویرایش)
- مشاهده لیست سفارشات برای کاربر و ادمین، و تغییر وضعیت سفارش

#### کاربران و پروفایل
- ثبت‌نام و ورود امن با رمزنگاری Hash برای پسورد
- ویرایش پروفایل: نام، ایمیل، تصویر پروفایل
- نمایش اطلاعات پروفایل کاربر در بخش «My Account» (فقط برای کاربران Logged-in)

#### کد تخفیف (Coupon)
- ایجاد کد تخفیف اختصاصی از پنل ادمین
- اعمال کد تخفیف در صفحه سبد خرید با محاسبه آنی مبلغ نهایی
- بررسی تاریخ انقضای کد و نمایش پیام خطا در صورت منقضی بودن

#### نظرات کاربران (Reviews)
- ثبت نظر برای محصول، فقط برای کاربران وارد‌شده (Logged-in)
- نظرات پس از تایید ادمین (از طریق تیک *Publication Status*) برای عموم نمایش داده می‌شوند

#### سایر
- فرم تماس با ما؛ پیام‌ها مستقیماً به پنل ادمین ارسال می‌شوند
- طراحی کاملاً واکنش‌گرا (Responsive) برای موبایل، تبلت و لپ‌تاپ
- بخش‌های داینامیک صفحه اصلی: **Categories**، **Featured Products** و **Recent Products** (حداکثر ۸ آیتم)
- نمایش چرخشی لوگوی فروشندگان با JavaScript

---

### 🛠 تکنولوژی‌های استفاده‌شده

**بک‌اند:**
- Python
- Django

**فرانت‌اند:**
- HTML5 / CSS3
- Bootstrap
- JavaScript / jQuery (AJAX برای سبد خرید، فیلتر، جستجوی زنده و ...)
- قالب پایه از [HTMLCodex](https://htmlcodex.com/) با شخصی‌سازی‌های سفارشی

**پایگاه داده:**
- SQLite (برای توسعه و تست)

---

### 📁 ساختار پروژه

```
shoppingstore_project/
├── manage.py                # فایل اجرایی اصلی مدیریت پروژه
├── db.sqlite3                # پایگاه داده SQLite
├── requirements.txt           # وابستگی‌های پایتون پروژه
├── static/                    # فایل‌های استاتیک (CSS, JS, تصاویر)
├── media/                     # فایل‌های آپلودشده توسط کاربران
├── templates/                  # قالب پایه (مشترک بین تمام صفحات)
│
├── shoppingstore/               # اپ صفحه اصلی (Home)
├── account/                    # اپ مربوط به کاربران (ثبت‌نام، ورود، پروفایل)
├── product/                    # اپ محصولات، دسته‌بندی‌ها و جزئیات کالا
├── cart/                       # اپ سبد خرید
├── checkout/                   # اپ فرم نهایی ثبت سفارش
├── coupon/                     # اپ کد تخفیف (در صفحه سبد خرید)
└── contact/                    # اپ فرم تماس با ما
```

---

### 🔗 آدرس‌های پروژه (Routes)

| بخش | آدرس | توضیح |
|---|---|---|
| صفحه اصلی | `/` | Home |
| ورود | `/account/login` | صفحه Login |
| ثبت‌نام | `/account/signup` | صفحه ثبت‌نام |
| پروفایل | `/account/profile` | مشاهده و ویرایش پروفایل |
| سبد خرید | `/cart` | صفحه Cart |
| تسویه حساب | `/checkout` | فرم مشخصات ارسال کالا |
| تماس با ما | `/contact` | فرم تماس |
| فروشگاه | `/shop` | لیست محصولات، فیلترها و Paginator |
| جزئیات محصول | `/shop/detail/<product_id>` | جزئیات کالا + بخش نظرات (Reviews) |
| پنل ادمین | `/admin` | مدیریت کامل سایت |

---

### 🚀 نصب و راه‌اندازی

```bash
# ۱. کلون کردن ریپازیتوری
git clone https://github.com/username/shopping-store.git
cd shopping-store

# ۲. ساخت محیط مجازی
python -m venv venv
source venv/bin/activate      # ویندوز: venv\Scripts\activate

# ۳. نصب پکیج‌ها
pip install -r requirements.txt

# ۴. اجرای مایگریشن‌ها
python manage.py migrate

# ۵. ساخت سوپریوزر برای دسترسی به پنل ادمین
python manage.py createsuperuser

# ۶. اجرای سرور
python manage.py runserver
```

پروژه روی آدرس زیر در دسترس خواهد بود:
```
http://127.0.0.1:8000
```

---

### 🔑 پنل ادمین

آدرس دسترسی به پنل مدیریت:
```
http://127.0.0.1:8000/admin
```

> ⚠️ **توجه امنیتی:** یوزر/پسورد `admin/admin` صرفاً برای محیط توسعه (Development) مناسب است. پیش از انتشار پروژه در محیط Production، حتماً یک سوپریوزر با نام کاربری و رمز عبور قوی و اختصاصی بسازید و از انتشار اطلاعات ورود در مخزن عمومی گیت‌هاب خودداری کنید.

از طریق پنل ادمین می‌توانید محصولات، دسته‌بندی‌ها، کاربران، سفارشات، کدهای تخفیف و نظرات را به‌طور کامل مدیریت کنید.

---

### 📌 نکات فنی

- بخش **Categories** در صفحه اصلی فقط دسته‌بندی‌هایی را نمایش می‌دهد که در پنل ادمین گزینه‌ی *Featured* برای آن‌ها فعال شده باشد.
- بخش **Featured Products** فقط محصولاتی را نشان می‌دهد که فیلد *is_featured* آن‌ها در پنل ادمین تیک خورده باشد.
- بخش **Recent Products** جدیدترین محصولات اضافه‌شده را نمایش می‌دهد (حداکثر ۸ مورد).
- در فرم Checkout، اگر کاربر پیش‌تر این فرم را پر کرده باشد، دفعات بعد به‌صورت خودکار پر می‌شود (قابل ویرایش). آدرس‌های ذخیره‌شده از بخش *Addresses* در پنل ادمین قابل مشاهده هستند.

---

### 🔒 امنیت

- رمزنگاری پسورد کاربران با الگوریتم‌های Hash
- محافظت در برابر حملات **XSS** و **CSRF**

---

### 🙏 اعتبارها

- **طراحی فرانت‌اند:** قالب پایه‌ی فرانت‌اند این پروژه توسط [HTMLCodex](https://htmlcodex.com/) طراحی شده است. در این پروژه فقط تغییرات و شخصی‌سازی‌های سفارشی روی این قالب اعمال شده؛ تمام منطق بک‌اند و توسعه با Django توسط من انجام شده است.

---

### 📄 لایسنس

این پروژه تحت لایسنس MIT منتشر شده است — برای جزئیات بیشتر فایل LICENSE را ببینید. توجه داشته باشید قالب فرانت‌اند تابع شرایط لایسنس اصلی [HTMLCodex](https://htmlcodex.com/) است.

### 📬 تماس

**محمد ارکیان**

اگر سوال یا پیشنهادی داشتید، از طریق بخش Issues همین ریپازیتوری یا اطلاعات تماس زیر با من در ارتباط باشید:
- ایمیل: mohammadarkiyan21@gmail.com
- گیت‌هاب: https://github.com/MohammadArkiyan

<div align="right">

[⬆ بازگشت به بالا](#shopping-store)

</div>
