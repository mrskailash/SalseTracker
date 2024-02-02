import tkinter as tk
from tkinter import messagebox

import mysql.connector


def execute_queries():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="salestracker"
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Create table if not exists
        create_table_query = """
            CREATE TABLE IF NOT EXISTS Source  (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sourcename VARCHAR(255)
            )
        """

        # Execute the query
        cursor.execute(create_table_query)

        # Commit changes
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        messagebox.showinfo("Success", "Table created successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


# Create main window
root = tk.Tk()
root.title("Execute MySQL Queries")

# Create and pack a button
btn_execute = tk.Button(root, text="Execute Queries", command=execute_queries)
btn_execute.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
