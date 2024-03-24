from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# conn = sqlite3.connect('orders_data.db')
# cursor = conn.cursor()

def get_connection():
    conn = sqlite3.connect('./data/orders_data.db')
    cursor = conn.cursor()
    return conn, cursor

class Order(BaseModel):
    customer_id: int
    order_date: str
    total_amount: float

@app.get("/orders")
def get_orders():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return orders

@app.get("/order/{order_id}")
def get_order(order_id: int):
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM orders WHERE  order_id=?", (order_id,))
    order = cursor.fetchone()
    cursor.close()
    conn.close()
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")

@app.post("/new-order")
def create_order(order: Order):
    conn, cursor = get_connection()
    cursor.execute("INSERT INTO orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)",
                   (order.customer_id, order.order_date, order.total_amount))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Order created successfully"}

# Endpoint to update an existing order
@app.put("/update-order/{order_id}")
def update_order(order_id: int, order: Order):
    conn, cursor = get_connection()
    cursor.execute("UPDATE orders SET customer_id=?, order_date=?, total_amount=? WHERE order_id=?",
                   (order.customer_id, order.order_date, order.total_amount, order_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Order updated successfully"}

# Endpoint to delete an order
@app.delete("/delete-order/{order_id}")
def delete_order(order_id: int):
    conn, cursor = get_connection()
    cursor.execute("DELETE FROM orders WHERE order_id=?", (order_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Order deleted successfully"}