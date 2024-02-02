import tkinter as tk
from tkinter import messagebox
import mysql.connector

def create_table():
    # Get values from entry widgets
    table_name = table_name_entry.get()

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

        # Create the table with a few columns (modify as needed)
        create_table_query = f"""
            CREATE TABLE {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                quantity INT,
                price DECIMAL(10, 2)
            )
        """
        cursor.execute(create_table_query)

        # Commit changes and close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        # Display success message
        messagebox.showinfo("Success", f"Table '{table_name}' created successfully!")

    except mysql.connector.Error as err:
        # Display error message
        messagebox.showerror("Error", f"Error creating table: {err}")

# Create main window for creating table
table_root = tk.Tk()
table_root.title("Create Table")

# Create labels and entry widgets for table creation
tk.Label(table_root, text="Table Name:").grid(row=0, column=0, padx=10, pady=10)
table_name_entry = tk.Entry(table_root)
table_name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a button to execute the create_table function
create_table_button = tk.Button(table_root, text="Create Table", command=create_table)
create_table_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop for table creation
table_root.mainloop()
