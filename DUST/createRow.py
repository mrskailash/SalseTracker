import tkinter as tk
from tkinter import messagebox
import mysql.connector

def add_row_entry():
    new_row_entry = tk.Entry(rows_frame)
    new_row_entry.grid(row=row_count, column=0, padx=10, pady=5)
    row_entries.append(new_row_entry)

def insert_data():
    # Get values from entry widgets
    table_name = "leadlist"  # Hardcoded table name
    row_values = [entry.get() for entry in row_entries]

    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Provide your MySQL password if set
            database="salestracker"
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Create the INSERT query
        insert_query = f"INSERT INTO {table_name} (date, {', '.join(row_values)}) VALUES (CURDATE(), {', '.join(['%s'] * len(row_values))})"
        
        # Execute the query
        cursor.execute(insert_query, row_values)

        # Commit changes and close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        # Display success message
        messagebox.showinfo("Success", "Row added successfully!")

    except mysql.connector.Error as err:
        # Display error message
        messagebox.showerror("Error", f"Error adding row: {err}")

# Create main window for adding rows
row_root = tk.Tk()
row_root.title("Add Rows")

# Frame to contain entry fields for rows
rows_frame = tk.Frame(row_root)
rows_frame.pack(padx=10, pady=10)

# Initial row entry
row_entries = []
row_count = 1
first_row_entry = tk.Entry(rows_frame)
first_row_entry.grid(row=row_count, column=0, padx=10, pady=5)
row_entries.append(first_row_entry)

# Button to add a new row entry
add_row_button = tk.Button(row_root, text="Add Row", command=add_row_entry)
add_row_button.pack(pady=10)

# Button to insert data into the database
insert_data_button = tk.Button(row_root, text="Insert Data", command=insert_data)
insert_data_button.pack(pady=10)

# Run the Tkinter main loop for adding rows
row_root.mainloop()
