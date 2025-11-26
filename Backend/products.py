from fastapi import APIRouter
from util import get_conn
from fastapi.responses import JSONResponse



router = APIRouter(tags=['Products'])



 # CREATE A PRODUCT
@router.post('/products')
def create_products(products_id,products_name,category,price):
    conn = get_conn()
    cur = conn.cursor()
    query = " INSERT INTO products VALUES (%s,%s,%s,%s)"
    values =(products_id,products_name,category,price)
    cur.execute(query,values)
    conn.commit()
    cur.close()
    conn.close()
    return{"message":"created successfully"}

# READ PRODUCTS
@router.get('/products')
def get_products():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM products;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return JSONResponse(content=rows)
# READ BY ID 
@router.get('/product/{product_id}')
def get_product_by_id(product_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE products_id=%s", (product_id,))
    row = cur.fetchone()
    if not row:
        return JSONResponse(content={'msg': 'products Not found'})
    cur.close()
    conn.close()
    return JSONResponse(content=row)


# 3.UPDATE PRODUCTS DETAILS

@router.put("/products/{products_id}")
def update_products(products_id, products_name, category, price):
    conn = get_conn()
    cur = conn.cursor()
    query = "UPDATE products SET products_name=%s, category=%s, price=%s WHERE products_id=%s"
    values = (products_name, category, price,products_id)
    cur.execute(query, values)
    conn.commit()
    cur.close()
    conn.close()
    return {"message": 'Products updated'}

# 4. DELETE PRODUCTS
@router.delete("/products/{products_id}")
def delete_product(products_id):
    conn = get_conn()
    cur = conn.cursor()
    query = " DELETE FROM products WHERE products_id =%s"
    values = (products_id,)
    cur.execute(query,values)
    conn.commit()
    cur.close()
    conn.close()
    return{"Message" : "Deleted successfull"}