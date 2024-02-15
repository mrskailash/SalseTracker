import sqlite3
import tkinter as tk
from tkinter import messagebox


def menu_command(option):
    messagebox.showinfo("Selected Option", f"You selected: {option}")


# Create main window
root = tk.Tk()
root.title("Filter Menu")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create filter menu
filter_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Filter", menu=filter_menu)

# Add sub-options for the "ID" option
id_menu = tk.Menu(filter_menu, tearoff=0)
filter_menu.add_cascade(label="ID Options", menu=id_menu)
id_menu.add_command(label="Ascending", command=lambda: menu_command("ID Ascending"))
id_menu.add_command(label="Descending", command=lambda: menu_command("ID Descending"))

# Fetch options for the "Status" menu from the database
connection = sqlite3.connect(
    "salestracker.db"
)  # Replace with your actual database file
cursor = connection.cursor()
cursor.execute("SELECT statustype FROM status")
status_options = [rows[0] for rows in cursor.fetchall()]

# Add sub-options for the "Status" option
status_menu = tk.Menu(filter_menu, tearoff=0)
filter_menu.add_cascade(label="Status Options", menu=status_menu)
for option in status_options:
    status_menu.add_command(
        label=option, command=lambda opt=option: menu_command(f"Status - {opt}")
    )

# Fetch options for the "Assign" menu from the database
cursor.execute("SELECT name FROM user WHERE id >= 2")
assign_names = [rows[0] for rows in cursor.fetchall()]

# Add sub-options for the "Assign" option
assign_menu = tk.Menu(filter_menu, tearoff=0)
filter_menu.add_cascade(label="Assign Options", menu=assign_menu)
for option in assign_names:
    assign_menu.add_command(
        label=option, command=lambda opt=option: menu_command(f"Assign - {opt}")
    )

# Start the Tkinter event loop
root.mainloop()
