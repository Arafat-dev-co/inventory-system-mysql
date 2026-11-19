from database import get_connection
from database import create_table

def add_product(conn, name, price, quantity):
    cursor = conn.cursor()

    query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"

    values = (name, price, quantity)
    cursor.execute(query, values)
    conn.commit()
    print(f"Sucessfully added {name} to the database")

def get_all_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()

    for row in results:
        print(f"ID: {row[0]} | {row[1]} | ${row[2]} | {row[3]}")

def update_product(conn, product_id, new_quantity):
    cursor = conn.cursor()

    query = "UPDATE products SET quantity = %s WHERE id = %s"

    cursor.execute(query, (new_quantity, product_id,))
    conn.commit()

    print("Product update")


def delete_product(conn, product_id):
    cursor = conn.cursor()

    query = "DELETE FROM products WHERE id = %s"

    cursor.execute(query, (product_id,))
    conn.commit()

    print("Product deleted") 
