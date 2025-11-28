# 🛒 SuperShop Backend (FastAPI)

This folder contains the **FastAPI backend** for the SuperShop Management System.  
The backend provides complete CRUD APIs for **Employees**, **Products**, and **Sales**, and connects to a PostgreSQL database.

---

## 📁 Files Overview

### 🔹 `main.py`
Main FastAPI application that includes all routers:
```python
app.include_router(employee_router)
app.include_router(product_router)
app.include_router(sale_router)
```

### 🔹 `employees.py`
Contains all CRUD API endpoints for employee management:
- Create (`POST /employees`)
- Read (`GET /employees`)
- Read by ID (`GET /employee/{id}`)
- Update (`PUT /employees/{id}`)
- Delete (`DELETE /employees/{id}`)

### 🔹 `products.py`
CRUD operations for products.

### 🔹 `sales.py`
CRUD operations for sales.

### 🔹 `util.py`
Handles PostgreSQL connection:
```python
def get_conn():
    return psycopg2.connect(DB_URL)
```

---

## 🚀 How to Run the Backend

### 1️⃣ Install Dependencies
```bash
pip install fastapi uvicorn psycopg2
```

### 2️⃣ Start the API Server
```bash
uvicorn main:app --reload
```

### 3️⃣ Open API Documentation
FastAPI automatically generates docs:

🔗 Swagger UI  
```
http://127.0.0.1:8000/docs
```

---

## 🗄️ Database

Backend uses PostgreSQL with the connection string in `util.py`.  
Tables required:
- `employees`
- `products`
- `sales`

---

## 📌 Features

- Organized modular FastAPI structure  
- Separate routers for each module  
- PostgreSQL database connectivity  
- Complete CRUD for all modules  
- Used by Streamlit frontend  

---

## 👨‍💻 Author
Backend built for SuperShop Management System using FastAPI and PostgreSQL.
