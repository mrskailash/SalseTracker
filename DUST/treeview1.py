import tkinter as tk
from tkinter import ttk

import mysql.connector


def fetch_data_from_db():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Provide your MySQL password if set
        database="salestracker",
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Fetch data from the database
    cursor.execute("SELECT * FROM leadlist")
    data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    connection.close()

    return data


def populate_treeview():
    data = fetch_data_from_db()

    for entry in data:
        tree.insert("", tk.END, values=entry)


def on_double_click(event):
    item = tree.selection()
    if item:
        open_detail_window(item)


def open_detail_window(item):
    detail_window = tk.Toplevel(root)
    detail_window.title("Details")
    detail_window.geometry("300x200")


# Create the main window
root = tk.Tk()
root.title("Tkinter Treeview Table Example")
root.geometry("500x500")

# Create a Treeview
tree = ttk.Treeview(
    root,
    columns=(
        "LeadNo",
        "Date",
        "Name",
        "contact person ",
        "address",
        "phone",
        "email",
    ),
    show="headings",
)

headings = [
    "Lead No",
    "Date",
    "Name",
    "contact person ",
    "address",
    "phone",
    "email",
]
for i, heading in enumerate(headings):
    tree.heading(i, text=heading, anchor="center")

# Define column widths
tree.column("LeadNo", width=50, anchor="center")
tree.column("Date", width=80, anchor="center")
tree.column("Name", width=100, anchor="center")
tree.column("contact person ", width=120, anchor="center")
tree.column("address", width=80, anchor="center")
tree.column("phone", width=120, anchor="center")
tree.column("email", width=100, anchor="center")

# Pack the Treeview
tree.pack(fill=tk.BOTH, expand=True)

# Populate the Treeview with data from the database
populate_treeview()

# Bind double-click event to open a new window
tree.bind("<Double-1>", on_double_click)

# Start the Tkinter event loop
root.mainloop()
