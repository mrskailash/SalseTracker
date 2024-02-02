import tkinter as tk
from tkinter import messagebox

import mysql.connector


def create_database():
    # Get values from entry widgets
    host = host_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    database_name = database_entry.get()

    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host, user=username, password=password
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Create the database
        cursor.execute(f"CREATE DATABASE {database_name}")

        # Close cursor and connection
        cursor.close()
        connection.close()

        # Display success message
        messagebox.showinfo(
            "Success", f"Database '{database_name}' created successfully!"
        )

    except mysql.connector.Error as err:
        # Display error message
        messagebox.showerror("Error", f"Error creating database: {err}")


# Create main window
root = tk.Tk()
root.title("Create Database")

# Create labels and entry widgets
tk.Label(root, text="Host:").grid(row=0, column=0, padx=10, pady=10)
host_entry = tk.Entry(root)
host_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Username:").grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Database Name:").grid(row=3, column=0, padx=10, pady=10)
database_entry = tk.Entry(root)
database_entry.grid(row=3, column=1, padx=10, pady=10)

# Create a button to execute the create_database function
create_button = tk.Button(root, text="Create Database", command=create_database)
create_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()
