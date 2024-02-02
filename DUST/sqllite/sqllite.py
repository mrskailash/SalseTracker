import sqlite3
import tkinter as tk
from tkinter import ttk


def create_user_table():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("salestracker.db")
    cursor = conn.cursor()

    # Create a table for user
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            Uname TEXT NOT NULL,
            name TEXT,
            password TEXT,
            type TEXT
        )
    """
    )

    # Insert data into the user table
    data = [
        (1, "Admin", "admin", "admin", "admin"),
        (2, "sales1", "sales1", "admin", "sales"),
        (3, "sales2", "sales2", "admin", "sales"),
        # ... (add the remaining rows)
    ]

    cursor.executemany(
        """
        INSERT INTO user (id, Uname, name, password, type)
        VALUES (?, ?, ?, ?, ?)
    """,
        data,
    )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def fetch_user_data():
    # Connect to the SQLite database
    conn = sqlite3.connect("salestracker.db")
    cursor = conn.cursor()

    # Fetch data from the user table
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    return data


def display_user_data():
    # Fetch data from the database
    data = fetch_user_data()

    # Create the Tkinter window
    root = tk.Tk()
    root.title("Sales Tracker - User Display")

    # Create a Treeview widget
    tree = ttk.Treeview(root)

    # Define columns for the Treeview
    tree["columns"] = tuple(["id", "Uname", "name", "password", "type"])

    # Configure column headings
    for column in tree["columns"]:
        tree.heading(column, text=column)

    # Insert data into the Treeview
    for row in data:
        tree.insert("", "end", values=row)

    # Pack the Treeview widget
    tree.pack(expand=True, fill="both")

    # Start the Tkinter event loop
    root.mainloop()


# Call the create_user_table function to create the user table and insert data
create_user_table()

# Call the display_user_data function to show the data in the Treeview
display_user_data()
