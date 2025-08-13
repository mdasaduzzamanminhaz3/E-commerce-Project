# 🛒 PhiMart – E-Commerce API (Django REST Framework)

**PhiMart** is a fully functional **E-commerce REST API** built using **Django REST Framework (DRF)**.  
It provides core e-commerce features such as product browsing, category management, cart operations, and order processing.  
The project uses **JWT Authentication** for secure user access and **Swagger (drf_yasg)** for interactive API documentation.

---

##  Features

- **User Authentication**
  - Secure **JWT-based login** & registration (using `djangorestframework-simplejwt`).
  - Role-based access for users and admins.
- **Product Management**
  - Create, read, update, and delete products.
  - Category-based product filtering.
- **Category Management**
  - CRUD operations for product categories.
- **Shopping Cart**
  - Add/remove products from the cart.
  - View cart items and total.
- **Orders**
  - Place orders from cart items.
  - View order history.
- **API Documentation**
  - Integrated **Swagger UI** & **Redoc** via `drf_yasg`.

---

## Tech Stack

- **Backend Framework**: Django, Django REST Framework
- **Authentication**: JWT (via `djangorestframework-simplejwt`)
- **API Docs**: Swagger / Redoc (`drf_yasg`)
- **Database**: SQLite (default) – easily switchable to PostgreSQL/MySQL
- **Environment Management**: Python `venv` or `pipenv`

## Installation & Setup

###  Clone the Repository
```bash
git clone https://github.com/yourusername/phimart.git
cd phimart
```

###  Create & Activate Virtual Environment
```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

###  Install Dependencies
```bash
pip install -r requirements.txt
```

###  Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

###  Create Superuser
```bash
python manage.py createsuperuser
```

###  Run Server
```bash
python manage.py runserver
```
Server will be running at:  
 `http://127.0.0.1:8000/`

---

##  JWT Authentication

- **Obtain Token**:  
  `POST /api/token/` → returns `access` and `refresh` tokens.
- **Refresh Token**:  
  `POST /api/token/refresh/`
- Use:  
  `Authorization: Bearer <access_token>` in API requests.

---

## 📜 API Documentation (Swagger)

- **Swagger UI**:  
   `http://127.0.0.1:8000/swagger/`
- **Redoc**:  
   `http://127.0.0.1:8000/redoc/`

---

##  API Endpoints Overview

| Endpoint                  | Method | Description                        | Auth Required |
|---------------------------|--------|------------------------------------|---------------|
| `/api/products/`          | GET    | List all products                  | No            |
| `/api/products/{id}/`     | GET    | Get single product details         | No            |
| `/api/products/`          | POST   | Create product                     | Yes (Admin)   |
| `/api/categories/`        | GET    | List all categories                | No            |
| `/api/cart/`               | GET    | View current user cart             | Yes           |
| `/api/cart/add/`          | POST   | Add product to cart                | Yes           |
| `/api/orders/`            | GET    | List user orders                   | Yes           |
| `/api/orders/`            | POST   | Place new order                    | Yes           |

*(Full details available in Swagger)*

---

##  Contribution

1. **Fork** the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to branch:
   ```bash
   git push origin feature-name
   ```
5. Open a **Pull Request**.

---

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
```