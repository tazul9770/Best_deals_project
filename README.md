# 🛒 Best Deals - E-commerce API  

**Best Deals** is a Django Rest Framework (DRF)-based **E-commerce API** project.  
It allows users to browse products, add/remove items from the cart, place orders, and track them.  

The project uses **JWT authentication via Djoser** and provides auto-generated API documentation using **drf_yasg (Swagger/Redoc)**.  

---

## 🚀 Features  

| Feature                  | Description                                                   | Status   |
|---------------------------|---------------------------------------------------------------|----------|
| 🔐 **User Authentication** | JWT-based secure login/signup with Djoser                   | ✅ Done  |
| 📦 **Product Management**  | CRUD operations for products                                | ✅ Done  |
| 🏷 **Category Management** | Organize products into categories                          | ✅ Done  |
| 🛒 **Cart System**         | Add, remove, update items in the cart                       | ✅ Done  |
| 📦 **Order Processing**    | Place orders & manage order details                         | ✅ Done  |
| 📑 **Swagger API Docs**    | Auto-generated Swagger & Redoc API Documentation            | ✅ Done  |

---

## 🛠 Technologies Used  

- **Backend**: Django, Django Rest Framework (DRF)  
- **Authentication**: Djoser (JWT-based)  
- **API Docs**: drf_yasg (Swagger / Redoc)  
- **Database**: PostgreSQL / SQLite  
- **Others**: Python 3.8+, Virtualenv, SMTP for email  

---

## ⚙️ Installation Guide  

### ✅ Prerequisites  
- Python **3.8+**  
- Django  
- PostgreSQL (optional, default is SQLite)  
- Virtual Environment (recommended)  

---

### 🔽 Setup Steps  

**1. Clone the repository**  
```bash
git clone https://github.com/yourusername/best_deals.git
cd best_deals

2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install dependencies

pip install -r requirements.txt


4. Create .env file in the root directory with the following content:

SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=best_deals_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=*
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password
EMAIL_USE_TLS=True


5. Apply migrations

python manage.py migrate


6. Create a superuser

python manage.py createsuperuser


7. Run the development server

python manage.py runserver


Server running at:
👉 http://127.0.0.1:8000/

🔑 Authentication (JWT via Djoser)
Obtain Access Token
POST /api/auth/jwt/create/
{
    "email": "user@example.com",
    "password": "yourpassword"
}

Use Token in API requests
Authorization: JWT your_access_token

📑 API Documentation

Swagger UI → http://127.0.0.1:8000/swagger/

Redoc UI → http://127.0.0.1:8000/redoc/
