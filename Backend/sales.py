from fastapi import APIRouter
from util import get_conn
from fastapi.responses import JSONResponse



router = APIRouter(tags=['Sales'])






#CREATE SALES
@router.post('/sales')
def create_sales(sale_id, sale_date,employee_id, product_id, quantity, total_amount):
    conn = get_conn()
    cur = conn.cursor()
    query = " INSERT INTO sales VALUES (%s,%s,%s,%s,%s,%s)"
    values =(sale_id, sale_date,employee_id, product_id, quantity, total_amount)
    cur.execute(query,values)
    conn.commit()
    cur.close()
    conn.close()
    return{"message":"created successfully"}


# READ SALES
@router.get('/sales')
def get_sales():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM sales;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

#READ SALES BY ID
@router.get('/sale/{sale_id}')
def get_sale_by_id(sale_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales WHERE sale_id=%s", (sale_id,))
    row = cur.fetchone()
    if not row:
        return JSONResponse(content={'msg': 'sales Not found'})
    cur.close()
    conn.close()
    return row


# 3.UPDATE SALES DETAILS

@router.put("/sales/{sale_id}")
def update_products(sale_id, sale_date,employee_id, product_id, quantity, total_amount):
    conn = get_conn()
    cur = conn.cursor()
    query = "UPDATE sales SET sale_date=%s, employee_id=%s, product_id=%s,quantity=%s,total_amount=%s WHERE sale_id=%s"
    values = ( sale_date,employee_id, product_id, quantity, total_amount,sale_id)
    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()
    return {"message": 'sales updated'}

# 4. DELETE SALES
@router.delete("/sales/{sale_id}")
def delete_product(sale_id):
    conn = get_conn()
    cur = conn.cursor()
    query = " DELETE FROM sales WHERE sale_id =%s"
    values = (sale_id)
    cur.execute(query,values)
    conn.commit()
    cur.close()
    conn.close()
    return{"Message" : "Deleted successfull"}