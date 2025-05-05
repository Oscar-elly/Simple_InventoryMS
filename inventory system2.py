import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to connect to the MySQL database
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="PRIME",
            user="PRIME",
            password="Underscore12",
            database="inventory"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error connecting to database: {err}")
        return None

# Function to add a product to the database
def add_product(name, price, quantity):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, price, quantity))
        conn.commit()
        messagebox.showinfo("Success", "Product added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error adding product: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
# Function to delete a product from the database
def delete_product(product_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "DELETE FROM products WHERE id = %s"
        cursor.execute(query, (product_id,))
        conn.commit()
        messagebox.showinfo("Success", "Product deleted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error deleting product: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Function to create the GUI for deleting a product
def delete_product_gui():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Product")

    tk.Label(delete_window, text="Enter Product ID:").grid(row=0, column=0)

    product_id_entry = tk.Entry(delete_window)
    product_id_entry.grid(row=0, column=1)

    def delete_from_db():
        product_id = product_id_entry.get()
        if product_id:
            delete_product(int(product_id))
            delete_window.destroy()
        else:
            messagebox.showerror("Error", "Please enter a valid Product ID.")

    tk.Button(delete_window, text="Delete", command=delete_from_db).grid(row=1, column=0, columnspan=2)

# Function to create the main GUI
def create_gui():
    global root
    root = tk.Tk()
    root.title("Inventory Management System")

    tk.Button(root, text="Add Product", command=add_product_gui).pack()
    tk.Button(root, text="View Products", command=display_products).pack()
    tk.Button(root, text="Delete Product", command=delete_product_gui).pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()

# Function to create the GUI for adding a product
def add_product_gui():
    add_window = tk.Toplevel(root)
    add_window.title("Add Product")

    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    tk.Label(add_window, text="Price:").grid(row=1, column=0)
    tk.Label(add_window, text="Quantity:").grid(row=2, column=0)

    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)
    price_entry = tk.Entry(add_window)
    price_entry.grid(row=1, column=1)
    quantity_entry = tk.Entry(add_window)
    quantity_entry.grid(row=2, column=1)

    def add_to_db():
        name = name_entry.get()
        price = float(price_entry.get())
        quantity = int(quantity_entry.get())
        add_product(name, price, quantity)
        add_window.destroy()

    tk.Button(add_window, text="Add", command=add_to_db).grid(row=3, column=0, columnspan=2)

# Function to display all products in the database
def display_products():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "SELECT * FROM products"
        cursor.execute(query)
        products = cursor.fetchall()
        product_list = "\n".join([f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}" for product in products])
        messagebox.showinfo("Products", product_list)
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error fetching products: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Function to create the main GUI
def create_gui():
    global root
    root = tk.Tk()
    root.title("Inventory Management System")

    tk.Button(root, text="Add Product", command=add_product_gui).pack()
    tk.Button(root, text="View Products", command=display_products).pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()
