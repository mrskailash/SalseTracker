import tkinter as tk
from tkinter import ttk

import mysql.connector


def make_entry_uneditable(entry):
    entry.config(state=tk.DISABLED, readonlybackground="white")


def fetch_lead_data():
    # Connect to MySQL server
    db_connection = mysql.connector.connect(
        host="localhost", user="root", password="", database="salestracker"
    )

    # Create a cursor object
    cursor = db_connection.cursor()

    # Fetch data from the leadlist table
    cursor.execute("SELECT fullname, address FROM leadlist")

    lead_data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    db_connection.close()

    return lead_data


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


root = tk.Tk()
root.geometry("500x500")

# Create a canvas with a vertical scrollbar
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill="both", expand=True)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", on_configure)

# Create a frame inside the canvas to hold your widgets
infocontainer = tk.Frame(canvas, relief="solid", borderwidth=2)
infocontainer.pack(ipadx=5, ipady=5)
infocontainer.pack_propagate(False)

# Fetch data
lead_data = fetch_lead_data()

# Create Entry widgets for each row of data
for i, entry_data in enumerate(lead_data, start=1):
    name_entry = tk.Entry(infocontainer, width=28, justify="center")
    name_entry.insert(0, entry_data[0])
    make_entry_uneditable(name_entry)
    name_entry.grid(row=i, column=0, ipady=5)

    address_entry = tk.Entry(infocontainer, width=28, justify="center")
    address_entry.insert(0, entry_data[1])
    make_entry_uneditable(address_entry)
    address_entry.grid(row=i, column=1, ipady=5)

# Add the frame to the canvas
canvas.create_window((0, 0), window=infocontainer, anchor="nw")

root.mainloop()
