import sqlite3
import tkinter as tk
from tkinter import messagebox


def fetch_lead_data():
    # Connect to your SQLite database
    connection = sqlite3.connect("salestracker.db")  # Replace with your database name

    # Create a cursor object
    cursor = connection.cursor()

    # Replace 'leadlist' with your table name and 'id' with the appropriate column name
    cursor.execute("SELECT id FROM leadlist LIMIT 1")

    # Fetch the data
    result = cursor.fetchone()

    # Close the database connection
    connection.close()

    return result


def on_double_click(event):
    # Fetch lead data from the database
    lead_data = fetch_lead_data()

    if lead_data:
        lead_id = lead_data[0]
        title = f"Close Lead - ID: {lead_id}"
    else:
        title = "Close Lead"

    # Create a message box with dynamic title
    result = messagebox.askokcancel(title, "Do you want to proceed?")

    # Check the result and print "ok" if OK button is clicked
    if result:
        print("ok")


# Create the main tkinter window
root = tk.Tk()
root.title("Double Click Message Box Example")

# Create a label to demonstrate double-click
label = tk.Label(root, text="Double click here")
label.pack(pady=20)

# Bind double-click event to the label
label.bind("<Double-1>", on_double_click)

# Run the Tkinter event loop
root.mainloop()
