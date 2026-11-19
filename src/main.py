from database import get_connection, create_table
from product import add_product
from product import get_all_products
from product import update_product
from product import delete_product

def main():
    conn = get_connection()
    
    if conn is not None:
        create_table(conn)

        while True:
            print("\n----OPTION----")
            print("1. Add Product")
            print("2. View Inventory")
            print("3. Update Stock Ouantity")
            print("4. Delete Product")
            print("5. EXit")

            option = input("Choose: ")

            if option == "1":
                name = input("Enter name: ")

                price = input("Enter price: ")

                quantity = input("Enter quantity: ")

                add_product(conn, name, price, quantity)

            elif option == "2":
                get_all_products(conn)

            elif option == "3":
                product_id = int(input("Enter your product id: "))

                new_quantity = int(input("Enter new quantity: "))

                update_product(conn, product_id, new_quantity)

            elif option == "4":
                product_id = int(input("Enter your product id: "))

                delete_product(conn, product_id)

            elif option == "5":
                conn.close()
                print("Thanks for using INVENTORY SYSTEM")
                break

if __name__ == "__main__":
    main()





            