# 📦 Product Management REST API

A RESTful API built with **FastAPI** that performs complete **CRUD (Create, Read, Update, Delete)** operations on product data stored in a JSON file.

This project was developed while learning FastAPI to understand API development, request validation, routing, query parameters, path parameters, and backend application structure. It demonstrates how to build clean and well-documented REST APIs using modern Python development practices.

---

## 🚀 Features

* ✅ Create new products
* ✅ Retrieve all products
* ✅ Retrieve a product by ID
* ✅ Update existing products
* ✅ Delete products using SKU
* ✅ Search products by name
* ✅ Sort products by price (Ascending/Descending)
* ✅ Pagination using `limit` and `offset`
* ✅ Request validation using Pydantic
* ✅ Automatic UUID generation for products
* ✅ Automatic creation timestamp
* ✅ Proper HTTP status codes and exception handling
* ✅ Interactive API documentation with Swagger UI and ReDoc

---

## 🛠️ Tech Stack

* **Python 3.x**
* **FastAPI**
* **Pydantic**
* **Uvicorn**
* **JSON** (File-based storage)

---

## 📁 Project Structure

```text
product-management-api/
│
├── main.py                  # FastAPI application
├── schema/
│   └── product.py           # Pydantic request models
├── services/
│   └── products.py          # CRUD service functions
├── products.json            # Product data storage
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sumit-bhole/FastApi-Demo-Project.git
```

### 2. Navigate to the project folder

```bash
cd FastApi-Demo-Project
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📌 API Endpoints

| Method | Endpoint                       | Description                        |
| ------ | ------------------------------ | ---------------------------------- |
| GET    | `/`                            | Welcome endpoint                   |
| GET    | `/get_products`                | Retrieve all products              |
| GET    | `/list_products`               | Search, sort and paginate products |
| GET    | `/get_product/{product_id}`    | Retrieve product by ID             |
| POST   | `/add_product`                 | Create a new product               |
| PUT    | `/update_product/{product_id}` | Update an existing product         |
| DELETE | `/delete_product/{sku}`        | Delete a product by SKU            |

---

# 🔍 Search & Pagination

The `/list_products` endpoint supports the following query parameters:

| Parameter       | Type    | Description                  |
| --------------- | ------- | ---------------------------- |
| `name`          | String  | Search products by name      |
| `sort_by_price` | Boolean | Sort products by price       |
| `order`         | String  | `asc` or `desc`              |
| `limit`         | Integer | Number of products to return |
| `offset`        | Integer | Pagination offset            |

### Example Request

```
GET /list_products?name=phone&sort_by_price=true&order=asc&limit=5&offset=0
```

---

# 📝 Sample Product Request

```json
{
    "name": "Wireless Mouse",
    "brand": "Logitech",
    "category": "Electronics",
    "price": 799,
    "sku": "WM-101"
}
```

---

# ✅ Example Success Response

```json
{
    "id": "1dcdf8dd-49f7-45ea-a0ec-ff7ec8ca8e7a",
    "name": "Wireless Mouse",
    "brand": "Logitech",
    "category": "Electronics",
    "price": 799,
    "sku": "WM-101",
    "created_at": "2026-07-06T10:25:31.932Z"
}
```

---

# ❌ Error Handling

The API returns meaningful HTTP responses.

| Status Code | Meaning                      |
| ----------- | ---------------------------- |
| **200**     | Request Successful           |
| **201**     | Product Created Successfully |
| **400**     | Invalid Request              |
| **404**     | Product Not Found            |

---

# 🎯 What I Learned

During this project, I gained practical experience with:

* Building REST APIs using FastAPI
* CRUD operations
* Request validation using Pydantic
* Query Parameters
* Path Parameters
* UUID generation
* JSON file handling
* Exception handling
* API documentation with Swagger
* Organizing backend projects into services and schemas

---

# 🔮 Future Improvements

Some features that can be added in future versions:

* Database integration (PostgreSQL/MySQL)
* SQLAlchemy ORM
* JWT Authentication
* User Management
* Docker Support
* Unit Testing with Pytest
* Logging
* Environment Variables
* API Versioning
* GitHub Actions (CI/CD)
* Deployment on Render or Railway

---

# 👨‍💻 Author

**Sumit Bhole**