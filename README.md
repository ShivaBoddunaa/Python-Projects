<<<<<<< HEAD
# 🏥 Doctor Appointment Management System

A simple **Python CLI-based Hospital/Clinic Management System** to manage Doctors, Patients, and Appointments.

This project allows users to:
- Add Doctors  
- Register Patients  
- Book Appointments  
- Cancel Appointments  
- View Doctor Schedules  
- Generate Daily Appointment Lists  
- View Patient History  

---

## 📌 Features

### 👨‍⚕️ Doctor Management
- Add new doctor  
- Choose speciality  
- Assign availability days  
- View all doctors  
- View hospital departments  

### 🧑‍💼 Patient Management
- Register new patient  
- View all registered patients  
- Display patient history  

### 📅 Appointment Management
- Book appointment  
- Cancel appointment  
- View doctor schedule  
- Generate daily appointment list  
- View all appointments  

---


=======
<<<<<<< HEAD
# 🏪 SuperShop Management System  
A complete mini retail management system built using **FastAPI (Backend)** and **Streamlit (Frontend)**.  
It supports full CRUD operations for **Employees**, **Products**, and **Sales** using a PostgreSQL database.

---

# 📂 Project Structure

```
Super_shop/
│
├── Backend/              # FastAPI backend
│     ├── main.py
│     ├── employees.py
│     ├── products.py
│     ├── sales.py
│     ├── util.py
│     └── README.md
│
├── Frontend/             # Streamlit frontend
│     ├── app.py
│     └── README.md
│
└── README.md             # Root README (this file)
```

---

# 🚀 Tech Stack

### **Backend**
- FastAPI  
- PostgreSQL  
- Psycopg2  
- Uvicorn  

### **Frontend**
- Streamlit  
- Python Requests  

---

# 🔧 How to Run the Project

## 1️⃣ Run Backend (FastAPI)
```
cd Backend
uvicorn main:app --reload
```

API Docs (Swagger UI):  
➡️ `http://127.0.0.1:8000/docs`

---

## 2️⃣ Run Frontend (Streamlit)
```
cd Frontend
streamlit run app.py
```

---

# 📌 Features

### 👥 Employees
- Add / View / Update / Delete  
- Role & region selection  
- Clean card-style UI  

### 📦 Products
- Add / View / Update / Delete  
- Category + pricing  

### 💰 Sales
- Record sales  
- Update & delete sales  
- View history  

---

# 🗄 Database  
Backend uses PostgreSQL connection via:
```
util.py → get_conn()
```

Tables used:
- `employees`
- `products`
- `sales`

---

# 📸 Screenshots (Optional)
*(You can add screenshots after running your app)*

---

# 👨‍💻 Author  
SuperShop project created using Python, FastAPI & Streamlit.

=======
# Python-Projects
Collection of my Python Projects
>>>>>>> 18b8894cccaa59e60ab724eb2b1e8c8d4cf83811
>>>>>>> 59b2223850228fe2a2abd2b9353a3707d631a91a
