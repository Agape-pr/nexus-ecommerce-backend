# Nexus E-commerce Backend

A scalable **E-commerce Backend API** built with **Django Rest Framework (DRF)** and **PostgreSQL**, following industry best practices.  
This project demonstrates professional API development with authentication, product management, cart, and order processing.  

---

##  Features

- **User Authentication** (JWT-based login, register, refresh tokens)
- **Product & Category Management** (CRUD with filtering, sorting, pagination)
- **Cart & Orders** (add to cart, checkout, order history)
- **API Documentation** with Swagger/OpenAPI
- **Database Optimization** with indexing for performance

---

##  Tech Stack

- **Backend Framework:** Django 4 + Django Rest Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** JWT (djangorestframework-simplejwt)
- **API Docs:** drf-spectacular (Swagger / ReDoc)
- **Environment Management:** python-decouple
- **Containerization (optional):** Docker

---

## 📂 Project Structure

nexus-ecommerce-backend/
│── venv/ # Virtual environment
│── src/
│ ├── config/ # Django project settings
│ ├── accounts/ # User authentication & management
│ ├── products/ # Products & categories
│ ├── orders/ # Cart & orders
│ ├── manage.py
│── requirements.txt
│── .env.example # Example environment variables
│── .gitignore
│── README.md



---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone git@github.com:Agape-pr/nexus-ecommerce-backend.git
cd nexus-ecommerce-backend
2. Create and activate virtual environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure environment variables
Copy .env.example → .env and update with your local settings:

env
Copy code
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=nexus_db
DB_USER=nexus_user
DB_PASSWORD=securepassword
DB_HOST=localhost
DB_PORT=5432
5. Run migrations
bash
Copy code
python src/manage.py migrate
6. Start development server
bash
Copy code
python src/manage.py runserver
API Endpoints
Auth
POST /api/register/ – Register a new user

POST /api/login/ – Obtain JWT access & refresh tokens

POST /api/token/refresh/ – Refresh access token

Products
GET /api/products/ – List products (with filtering, sorting, pagination)

POST /api/products/ – Create product

PUT /api/products/{id}/ – Update product

DELETE /api/products/{id}/ – Delete product

Categories
GET /api/categories/ – List categories

POST /api/categories/ – Create category

Cart & Orders
POST /api/cart/ – Add product to cart

GET /api/cart/ – View user cart

POST /api/orders/ – Place an order

GET /api/orders/ – View order history


API Documentation
Swagger UI:
 http://localhost:8000/api/schema/swagger-ui/

ReDoc:
 http://localhost:8000/api/schema/redoc/

