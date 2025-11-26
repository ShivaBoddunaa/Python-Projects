# 🛍️ SuperShop Frontend (Streamlit)

This folder contains the Streamlit-based user interface for the SuperShop Management System.

## Modules
### Employees:
- Create employee
- Update employee
- Delete employee
- List employees

### Products:
- Create product
- Update product
- Delete product
- List products

### Sales:
- Create sale
- Update sale
- Delete sale
- List sales

## How to Run
Install:
```bash
pip install streamlit requests
```

Run:
```bash
streamlit run app.py
```

## How It Works
Frontend sends API calls to FastAPI backend such as:
```python
requests.get("http://127.0.0.1:8000/employees")
```

## UI Features
- Clean layout
- Dialog-based forms
- Toast notifications
