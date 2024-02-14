import sqlite3
import tkinter as tk
from tkinter import ttk


def fetch_data():
    # Connect to SQLite server
    conn = sqlite3.connect("salestracker.db")
    cursor = conn.cursor()

    # Fetch data from different tables
    cursor.execute("SELECT statustype FROM status")
    status_options = [rows[0] for rows in cursor.fetchall()]

    cursor.execute("SELECT Sourcename FROM source")
    sources = [rows[0] for rows in cursor.fetchall()]

    # Close the database connection
    conn.commit()
    conn.close()

    return status_options, sources


def update_sub_dropdown(*args):
    selected_option = dropdown_combobox.get()

    if selected_option == "(none)":
        dropdown_sub_combobox.set("")
        dropdown_sub_combobox["values"] = []
        dropdown_sub_combobox["state"] = "disabled"
    elif selected_option == "Closure":
        dropdown_sub_combobox["values"] = data[0]
        dropdown_sub_combobox["state"] = "readonly"
    elif selected_option == "Source":
        dropdown_sub_combobox["values"] = data[1]
        dropdown_sub_combobox["state"] = "readonly"


# Create main window
search_window = tk.Tk()
search_window.title("Dropdown Example")

# Create and place widgets
dropdown_label = tk.Label(search_window, text="By Dropdown", font=("Arial", 12))
dropdown_label.grid(row=2, column=0, pady=10)

dropdown_option = ["(none)", "Closure", "Source"]
dropdown_combobox = ttk.Combobox(search_window, values=dropdown_option)
dropdown_combobox.grid(row=2, column=1, pady=10)
dropdown_combobox.set("(none)")  # Set default value
dropdown_combobox.bind("<<ComboboxSelected>>", update_sub_dropdown)

data = fetch_data()

dropdown_sub_combobox = ttk.Combobox(search_window, values=data[0], state="disabled")
dropdown_sub_combobox.grid(row=2, column=2, pady=10)

# Start the main loop
search_window.mainloop()
