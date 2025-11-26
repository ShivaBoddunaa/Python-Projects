from fastapi import FastAPI
from fastapi.responses import JSONResponse
import psycopg2
from psycopg2.extras import RealDictCursor
from employees import router as employee_router
from products import router as product_router
from sales import router as sale_router


app = FastAPI()
app.include_router(employee_router)
app.include_router(product_router)
app.include_router(sale_router)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
# from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# import psycopg2
# from psycopg2.extras import RealDictCursor
 
# app = FastAPI()
 
 
# DB_URL = 'postgresql://postgres.plfcbrrmqulhjavgkyhf:1234567@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres'
 
# def get_conn():
#     conn = psycopg2.connect(DB_URL)
#     return conn
 
#  # CREATE AN EMPLOYEE
# @app.post('/employees')
# def create_employees(employee_id,name,position,region):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = " INSERT INTO employees VALUES (%s,%s,%s,%s)"
#     values =(employee_id,name,position,region)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return{"message":"created successfully"}

      
# #1. Read employee
# @app.get('/employees')
# def get_employees():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM employees;')
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return JSONResponse(content=rows)
    
# @app.get('/employee/{employee_id}')
# def get_employee_by_id(employee_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM employees WHERE employee_id=%s", (employee_id,))
#     row = cur.fetchone()
#     if not row:
#         return JSONResponse(content={'msg': 'Employee Not found'})
#     cur.close()
#     conn.close()
#     return JSONResponse(content=row)



# # 3.UPDATE EMPLOYEES DETAILS

# @app.put("/employees/{employee_id}")
# def update_employee(employee_id, name, position, region):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = "UPDATE employees SET name=%s, position=%s, region=%s WHERE employee_id=%s"
#     values = (name, position, region, employee_id)
#     cur.execute(query, values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {"message": 'Employee updated'}

# # 4. DELETE EMPLOYEE
# @app.delete("/employees/{employee_id}")
# def delete_employee(employee_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = " DELETE FROM employees WHERE employee_id =%s"
#     values = (employee_id)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return{"Message" : "Deleted successfull"}




#  # CREATE A PRODUCT
# @app.post('/products')
# def create_products(products_id,products_name,category,price):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = " INSERT INTO products VALUES (%s,%s,%s,%s)"
#     values =(products_id,products_name,category,price)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return{"message":"created successfully"}

# # READ PRODUCTS
# @app.get('/products')
# def get_products():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM products;')
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return JSONResponse(content=rows)
# # READ BY ID 
# @app.get('/product/{product_id}')
# def get_product_by_id(product_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM products WHERE products_id=%s", (product_id,))
#     row = cur.fetchone()
#     if not row:
#         return JSONResponse(content={'msg': 'products Not found'})
#     cur.close()
#     conn.close()
#     return JSONResponse(content=row)


# # 3.UPDATE PRODUCTS DETAILS

# @app.put("/products/{products_id}")
# def update_products(products_id, products_name, category, price):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = "UPDATE products SET products_name=%s, category=%s, price=%s WHERE products_id=%s"
#     values = (products_name, category, price,products_id)
#     cur.execute(query, values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {"message": 'Products updated'}

# # 4. DELETE PRODUCTS
# @app.delete("/products/{products_id}")
# def delete_product(products_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = " DELETE FROM products WHERE products_id =%s"
#     values = (products_id,)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return{"Message" : "Deleted successfull"}



# #CREATE SALES
# @app.post('/sales')
# def create_sales(sale_id, sale_date,employee_id, product_id, quantity, total_amount):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = " INSERT INTO sales VALUES (%s,%s,%s,%s,%s,%s)"
#     values =(sale_id, sale_date,employee_id, product_id, quantity, total_amount)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return{"message":"created successfully"}


# # READ SALES
# @app.get('/sales')
# def get_sales():
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM sales;')
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return rows

# #READ SALES BY ID
# @app.get('/sale/{sale_id}')
# def get_sale_by_id(sale_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM sales WHERE sale_id=%s", (sale_id,))
#     row = cur.fetchone()
#     if not row:
#         return JSONResponse(content={'msg': 'sales Not found'})
#     cur.close()
#     conn.close()
#     return row


# # 3.UPDATE SALES DETAILS

# @app.put("/sales/{sale_id}")
# def update_products(sale_id, sale_date,employee_id, product_id, quantity, total_amount):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = "UPDATE products SET sale_date=%s, employee_id=%s, product_id=%s,quantity=%s,total_amount WHERE sale_id=%s"
#     values = ( sale_date,employee_id, product_id, quantity, total_amount,sale_id)
#     cur.execute(query, values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return {"message": 'sales updated'}

# # 4. DELETE SALES
# @app.delete("/sales/{sale_id}")
# def delete_product(sale_id):
#     conn = get_conn()
#     cur = conn.cursor()
#     query = " DELETE FROM sales WHERE sale_id =%s"
#     values = (sale_id)
#     cur.execute(query,values)
#     conn.commit()
#     cur.close()
#     conn.close()
#     return{"Message" : "Deleted successfull"}


