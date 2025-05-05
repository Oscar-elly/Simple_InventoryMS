import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "oscar" and password == "cake":
        welcome_window.destroy()
        show_main_window()
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Function to show the main window after successful login
def show_main_window():
    main_window = tk.Tk()
    main_window.title("Inventory Management System")

    def add_inventory():
        # Functionality to add inventory to the database
        pass

    def view_inventory():
        # Functionality to view inventory from the database
        pass

    def delete_inventory():
        # Functionality to delete inventory from the database
        pass

    add_button = tk.Button(main_window, text="Add Inventory", command=add_inventory)
    add_button.pack()

    view_button = tk.Button(main_window, text="View Inventory", command=view_inventory)
    view_button.pack()

    delete_button = tk.Button(main_window, text="Delete Inventory", command=delete_inventory)
    delete_button.pack()

    main_window.mainloop()

# Welcome window for login
welcome_window = tk.Tk()
welcome_window.title("Welcome to Inventory Management System")

username_label = tk.Label(welcome_window, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(welcome_window)
username_entry.grid(row=0, column=1)

password_label = tk.Label(welcome_window, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(welcome_window, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(welcome_window, text="Login", command=login)
login_button.grid(row=2, columnspan=2)

welcome_window.mainloop()
