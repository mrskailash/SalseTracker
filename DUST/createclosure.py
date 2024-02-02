# import tkinter as tk
# from tkinter import messagebox

# import mysql.connector


# def create_source_table():
#     try:
#         # Connect to MySQL
#         conn = mysql.connector.connect(
#             host="localhost", user="root", password="", database="salestracker"
#         )

#         # Create a cursor object
#         cursor = conn.cursor()

#         # Create table if not exists
#         create_table_query = """
#             CREATE TABLE IF NOT EXISTS source (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 type VARCHAR(255),
#                 name VARCHAR(255)
#             )
#         """
#         cursor.execute(create_table_query)

#         # Commit the changes
#         conn.commit()

#         # Display success message
#         messagebox.showinfo("Success", "Source table created successfully!")

#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error creating source table: {err}")

#     finally:
#         # Close the cursor and connection
#         cursor.close()
#         conn.close()


# # Create main window
# root = tk.Tk()
# root.title("Create Source Table")

# # Create and pack a button
# btn_create_table = tk.Button(
#     root, text="Create Source Table", command=create_source_table
# )
# btn_create_table.pack(pady=10)

# # Start the Tkinter event loop
# root.mainloop()


import tkinter as tk
from tkinter import messagebox

import mysql.connector


def create_employe_table():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="salestracker"
        )

        # Create a cursor object
        cursor = conn.cursor()

        # Create table if not exists
        create_table_query = """
            CREATE TABLE IF NOT EXISTS employe (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                password VARCHAR(255),
                type VARCHAR(255)
            )
        """
        cursor.execute(create_table_query)

        # Insert values into the employe table
        insert_values_query = """
            INSERT INTO employe (name, password, type)
            VALUES
            ('admin', 'admin', 'admin'),
            ('sales1', 'admin', 'sales'),
            ('sales2', 'admin', 'sales')
        """
        cursor.execute(insert_values_query)

        # Commit the changes
        conn.commit()

        # Display success message
        messagebox.showinfo(
            "Success", "Employe table created and values inserted successfully!"
        )

    except mysql.connector.Error as err:
        # Display error message
        messagebox.showerror("Error", f"Error creating employe table: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


# Create main window
root = tk.Tk()
root.title("Create Employe Table")

# Create and pack a button
btn_create_table = tk.Button(
    root, text="Create Employe Table", command=create_employe_table
)
btn_create_table.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
