
# ConcordiaBookModule

ConcordiaBook is a web/mobile application for students to trade textbooks they no longer use for textbooks they need. This web application built with [Django](https://www.djangoproject.com/).  

## 🛠️ Tech Stack

- Python 3.10+
- Django 4.x
- SQLite (default, can be replaced with PostgreSQL / MySQL)
- Bootstrap 5 (frontend styling)

---

## Authors

- [@Yuelin Wen](https://github.com/yuelinwen)
- Email: wenyuelinca@gmail.com

## 📌 API Routes

| Description                     | Method | Endpoint                                      |
|----------------------------------|--------|-----------------------------------------------|
| Admin                            | GET    | /admin                                       |
| Login                            | POST   | /auth/login                                  |
| Register                         | POST   | /auth/register                               |
| Logout                           | POST   | /auth/logout                                 |
| List textbooks                   | GET    | /textbooks                                   |
| Filter textbooks by course code  | GET    | /textbooks/?courseCode&availability=true     |
| Add new textbook                 | POST   | /textbooks/add                               |


## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yuelinwen/ConcordiaBookModule.git
cd myproject
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server to start my project
```bash
python manage.py runserver
```

Visit 👉 http://127.0.0.1:8000/


