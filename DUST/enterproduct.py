# import tkinter as tk
# from tkinter import messagebox

# import mysql.connector


# def save_product():
#     # Get the product name from the entry widget
#     product_name = product_name_entry.get()

#     try:
#         # Connect to MySQL server
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",  # Provide your MySQL password if set
#             database="salestracker",
#         )

#         # Create a cursor object
#         cursor = connection.cursor()

#         # Insert the product name into the products table
#         insert_query = "INSERT INTO products (productname) VALUES (%s)"
#         data = (product_name,)
#         cursor.execute(insert_query, data)

#         # Commit changes and close cursor and connection
#         connection.commit()
#         cursor.close()
#         connection.close()

#         # Display success message
#         messagebox.showinfo("Success", f"Product '{product_name}' saved successfully!")

#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error saving product: {err}")


# # Create main window for saving products
# root = tk.Tk()
# root.title("Save Product")

# # Create labels and entry widgets for product saving
# tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=10, pady=10)
# product_name_entry = tk.Entry(root)
# product_name_entry.grid(row=0, column=1, padx=10, pady=10)

# # Create a button to execute the save_product function
# save_button = tk.Button(root, text="Save Product", command=save_product)
# save_button.grid(row=1, column=0, columnspan=2, pady=10)

# # Run the Tkinter main loop for saving products
# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector
# import random
#
# def save_amount():
#     # Generate a random amount
#     generated_amount = random.randint(1000, 10000)
#
#     try:
#         # Connect to MySQL server
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",  # Provide your MySQL password if set
#             database="salestracker"
#         )
#
#         # Create a cursor object
#         cursor = connection.cursor()
#
#         # Insert the generated amount into the products table
#         insert_query = "INSERT INTO products (amount) VALUES (%s)"
#         data = (generated_amount,)
#         cursor.execute(insert_query, data)
#
#         # Commit changes and close cursor and connection
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         # Display success message
#         messagebox.showinfo("Success", f"Amount '{generated_amount}' saved successfully!")
#
#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error saving amount: {err}")
#
# # Create main window for saving amounts
# root = tk.Tk()
# root.title("Save Amount")
#
# # Create a button to execute the save_amount function
# save_button = tk.Button(root, text="Save Amount", command=save_amount)
# save_button.pack(padx=10, pady=10)
#
# # Run the Tkinter main loop for saving amounts
# root.mainloop()
#


import random
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import messagebox

import mysql.connector


def insert_random_dates():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Provide your MySQL password if set
            database="salestracker",
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Get the current date
        current_date = datetime.now()

        # Generate 50 random dates in 'yyyy-mm-dd' format
        random_date_list = [
            (current_date + timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d")
            for _ in range(50)
        ]

        # Insert new rows with random dates into the leadlist table
        insert_query = "INSERT INTO leadlist (date) VALUES (%s)"
        data = [(date,) for date in random_date_list]
        cursor.executemany(insert_query, data)

        # Commit changes and close cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        # Display success message
        messagebox.showinfo("Success", "Random dates inserted successfully!")

    except mysql.connector.Error as err:
        # Display error message
        messagebox.showerror("Error", f"Error inserting random dates: {err}")


# Create main window for updating dates
root = tk.Tk()
root.title("Insert Random Dates")

# Create a button to execute the insert_random_dates function
insert_button = tk.Button(root, text="Insert Random Dates", command=insert_random_dates)
insert_button.pack(padx=10, pady=10)

# Run the Tkinter main loop for inserting random dates
root.mainloop()


# import random
# import tkinter as tk
# from tkinter import messagebox

# import mysql.connector


# def generate_indian_names():
#     # List of Indian names
#     indian_names = [
#         "Aditya",
#         "Aarav",
#         "Amit",
#         "Ananya",
#         "Bhavya",
#         "Chetan",
#         "Divya",
#         "Esha",
#         "Farhan",
#         "Gauri",
#         "Harsh",
#         "Ishaan",
#         "Jaya",
#         "Kunal",
#         "Lavanya",
#         "Mohan",
#     ]

#     # Shuffle the list to get random names
#     random.shuffle(indian_names)

#     # Return the first 16 names
#     return indian_names[:16]


# def save_names():
#     try:
#         # Connect to MySQL server
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",  # Provide your MySQL password if set
#             database="salestracker",
#         )

#         # Create a cursor object
#         cursor = connection.cursor()

#         # Generate 16 random Indian names
#         name_list = generate_indian_names()

#         # Loop through lead IDs from 1 to 16
#         for lead_id, lead_name in enumerate(name_list, start=1):
#             # Update the existing lead's name in the leadlist table
#             update_query = "UPDATE leadlist SET name = %s WHERE id = %s"
#             data = (lead_name, lead_id)
#             cursor.execute(update_query, data)

#         # Commit changes and close cursor and connection
#         connection.commit()
#         cursor.close()
#         connection.close()

#         # Display success message
#         messagebox.showinfo("Success", "Names updated successfully!")

#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error updating names: {err}")


# # Create main window for updating names
# root = tk.Tk()
# root.title("Update Names")

# # Create a button to execute the save_names function
# save_button = tk.Button(root, text="Update Names", command=save_names)
# save_button.pack(padx=10, pady=10)

# # Run the Tkinter main loop for updating names
# root.mainloop()

#
# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector
# import random
#
#
# def generate_indian_names():
#     # List of Indian names
#     indian_names = ["Aditya", "Aarav", "Amit", "Ananya", "Bhavya", "Chetan", "Divya", "Esha", "Farhan", "Gauri",
#                     "Harsh", "Ishaan", "Jaya", "Kunal", "Lavanya", "Mohan"]
#
#     # Shuffle the list to get random names
#     random.shuffle(indian_names)
#
#     # Return the first 16 names
#     return indian_names[:16]
#
#
# def generate_surnames():
#     # List of Indian surnames
#     indian_surnames = ["Kumar", "Sharma", "Verma", "Singh", "Patel", "Gupta", "Das", "Reddy", "Shah", "Jha", "Mishra",
#                        "Rao", "Malhotra", "Choudhary", "Pandey", "Yadav"]
#
#     # Shuffle the list to get random surnames
#     random.shuffle(indian_surnames)
#
#     # Return the first 16 surnames
#     return indian_surnames[:16]
#
#
# def generate_emails(names, surnames):
#     # Combine names and surnames to create email addresses
#     emails = [f"{name.lower()}.{surname.lower()}@gmail.com" for name, surname in zip(names, surnames)]
#     return emails
#
#
# def save_emails():
#     try:
#         # Connect to MySQL server
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",  # Provide your MySQL password if set
#             database="salestracker"
#         )
#
#         # Create a cursor object
#         cursor = connection.cursor()
#
#         # Generate 16 random Indian names and surnames
#         names = generate_indian_names()
#         surnames = generate_surnames()
#
#         # Generate email addresses
#         emails = generate_emails(names, surnames)
#
#         # Loop through lead IDs from 1 to 16
#         for lead_id, email in enumerate(emails, start=1):
#             # Update the existing lead's email in the leadlist table
#             update_query = "UPDATE leadlist SET email = %s WHERE id = %s"
#             data = (email, lead_id)
#             cursor.execute(update_query, data)
#
#         # Commit changes and close cursor and connection
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         # Display success message
#         messagebox.showinfo("Success", "Emails updated successfully!")
#
#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error updating emails: {err}")
#
#
# # Create main window for updating emails
# root = tk.Tk()
# root.title("Update Emails")
#
# # Create a button to execute the save_emails function
# save_button = tk.Button(root, text="Update Emails", command=save_emails)
# save_button.pack(padx=10, pady=10)
#
# # Run the Tkinter main loop for updating emails
# root.mainloop()
#
# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector
# import random
#
# def generate_salespersons():
#     # List of salespersons
#     salespersons = ["Nikhil", "Himanshu"]
#
#     # Shuffle the list to get random salespersons
#     random.shuffle(salespersons)
#
#     # Repeat the shuffled list to match the number of rows (16)
#     return salespersons * 8
#
# def save_salespersons():
#     try:
#         # Connect to MySQL server
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",  # Provide your MySQL password if set
#             database="salestracker"
#         )
#
#         # Create a cursor object
#         cursor = connection.cursor()
#
#         # Generate 16 random salespersons
#         salespersons = generate_salespersons()
#
#         # Loop through lead IDs from 1 to 16
#         for lead_id, salesperson in enumerate(salespersons, start=1):
#             # Update the existing lead's salesperson in the leadlist table
#             update_query = "UPDATE leadlist SET salesperson = %s WHERE id = %s"
#             data = (salesperson, lead_id)
#             cursor.execute(update_query, data)
#
#         # Commit changes and close cursor and connection
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         # Display success message
#         messagebox.showinfo("Success", "Salespersons updated successfully!")
#
#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error updating salespersons: {err}")
#
# # Create main window for updating salespersons
# root = tk.Tk()
# root.title("Update Salespersons")
#
# # Create a button to execute the save_salespersons function
# save_button = tk.Button(root, text="Update Salespersons", command=save_salespersons)
# save_button.pack(padx=10, pady=10)
#
# # Run the Tkinter main loop for updating salespersons
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector
# import random
#
# def generate_addresses():
#     # List of city names
#     cities = ["Udaipur", "Jaipur", "Dabok", "Mavli"]
#
#     # List of random streets
#     streets = ["Gulab Bagh Road", "Bapu Bazaar", "Airport Road", "Station Road", "City Palace Road", "Saheliyon Ki Bari"]
#
#     # Generate 16 random addresses with city and street
#     addresses = [f"{random.choice(streets)}, {random.choice(cities)}" for _ in range(16)]
#
#     return addresses
#
# def save_addresses():
#     try:
#         # Connect to MySQL server
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",  # Provide your MySQL password if set
#             database="salestracker"
#         )
#
#         # Create a cursor object
#         cursor = connection.cursor()
#
#         # Generate 16 random addresses
#         addresses = generate_addresses()
#
#         # Loop through lead IDs from 1 to 16
#         for lead_id, address in enumerate(addresses, start=1):
#             # Update the existing lead's address in the leadlist table
#             update_query = "UPDATE leadlist SET address = %s WHERE id = %s"
#             data = (address, lead_id)
#             cursor.execute(update_query, data)
#
#         # Commit changes and close cursor and connection
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         # Display success message
#         messagebox.showinfo("Success", "Addresses updated successfully!")
#
#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error updating addresses: {err}")
#
# # Create main window for updating addresses
# root = tk.Tk()
# root.title("Update Addresses")
#
# # Create a button to execute the save_addresses function
# save_button = tk.Button(root, text="Update Addresses", command=save_addresses)
# save_button.pack(padx=10, pady=10)
#
# # Run the Tkinter main loop for updating addresses
# root.mainloop()

#
# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector
# import random
#
# def generate_sources():
#     # List of sources
#     sources = ["Indiamart", "Reference", "Amazon", "Flipkart"]
#
#     # Shuffle the list to get random sources
#     random.shuffle(sources)
#
#     # Repeat the shuffled list to match the number of rows (18)
#     return sources * 4
#
# def generate_assignees():
#     # List of assignees
#     assignees = ["Nikhil"] * 5 + ["Himanshu"] * 6 + ["Nikhil"] * 5 + ["Himanshu"] * 2
#
#     # Shuffle the list to get random assignees
#     random.shuffle(assignees)
#
#     # Return the first 18 assignees
#     return assignees[:18]
#
# def generate_statuses():
#     # List of statuses
#     statuses = ["Meeting Done", "Close", "Running", "Cancel", "Hold"]
#
#     # Shuffle the list to get random statuses
#     random.shuffle(statuses)
#
#     # Repeat the shuffled list to match the number of rows (18)
#     return statuses * 4
#
# def save_lead_data():
#     try:
#         # Connect to MySQL server
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",  # Provide your MySQL password if set
#             database="salestracker"
#         )
#
#         # Create a cursor object
#         cursor = connection.cursor()
#
#         # Generate 18 random sources, assignees, and statuses
#         sources = generate_sources()
#         assignees = generate_assignees()
#         statuses = generate_statuses()
#
#         # Loop through lead IDs from 1 to 18
#         for lead_id, (source, assignee, status) in enumerate(zip(sources, assignees, statuses), start=1):
#             # Update the existing lead's data in the leadlist table
#             update_query = "UPDATE leadlist SET source = %s, asignto = %s, status = %s WHERE id = %s"
#             data = (source, assignee, status, lead_id)
#             cursor.execute(update_query, data)
#
#         # Commit changes and close cursor and connection
#         connection.commit()
#         cursor.close()
#         connection.close()
#
#         # Display success message
#         messagebox.showinfo("Success", "Lead data updated successfully!")
#
#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error updating lead data: {err}")
#
# # Create main window for updating lead data
# root = tk.Tk()
# root.title("Update Lead Data")
#
# # Create a button to execute the save_lead_data function
# save_button = tk.Button(root, text="Update Lead Data", command=save_lead_data)
# save_button.pack(padx=10, pady=10)
#
# # Run the Tkinter main loop for updating lead data
# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# 
# import mysql.connector
# 
# 
# def execute_queries():
#     try:
#         # Connect to MySQL
#         conn = mysql.connector.connect(
#             host="localhost", user="root", password="", database="salestracker"
#         )
# 
#         # Create a cursor object
#         cursor = conn.cursor()
# 
#         # Create table if not exists
#         create_table_query = """
#             CREATE TABLE IF NOT EXISTS leadlist (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 date DATE,
#                 name VARCHAR(255),
#                 salesperson VARCHAR(255),
#                 address VARCHAR(255),
#                 email VARCHAR(255),
#                 source VARCHAR(255),
#                 asignto VARCHAR(255),
#                 status VARCHAR(255)
#             )
#         """
#         cursor.execute(create_table_query)
# 
# 
#         # Display success message
#         messagebox.showinfo("Success", "Table and row created successfully!")
# 
#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error executing queries: {err}")
# 
#     finally:
#         # Close the cursor and connection
#         cursor.close()
#         conn.close()
# 
# 
# # Create main window
# root = tk.Tk()
# root.title("Execute MySQL Queries")
# 
# # Create and pack a button
# btn_execute = tk.Button(root, text="Execute Queries", command=execute_queries)
# btn_execute.pack(pady=10)
# 
# # Start the Tkinter event loop
# root.mainloop() tk
# from tkinter import messagebox
# 
# import mysql.connector
# 
# 
# def execute_queries():
#     try:
#         # Connect to MySQL
#         conn = mysql.connector.connect(
#             host="localhost", user="root", password="", database="salestracker"
#         )
# 
#         # Create a cursor object
#         cursor = conn.cursor()
# 
#         # Create table if not exists
#         create_table_query = """
#             CREATE TABLE IF NOT EXISTS leadlist (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 date DATE,
#                 name VARCHAR(255),
#                 salesperson VARCHAR(255),
#                 address VARCHAR(255),
#                 email VARCHAR(255),
#                 source VARCHAR(255),
#                 asignto VARCHAR(255),
#                 status VARCHAR(255)
#             )
#         """
#         cursor.execute(create_table_query)
# 
# 
#         # Display success message
#         messagebox.showinfo("Success", "Table and row created successfully!")
# 
#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error executing queries: {err}")
# 
#     finally:
#         # Close the cursor and connection
#         cursor.close()
#         conn.close()
# 
# 
# # Create main window
# root = tk.Tk()
# root.title("Execute MySQL Queries")
# 
# # Create and pack a button
# btn_execute = tk.Button(root, text="Execute Queries", command=execute_queries)
# btn_execute.pack(pady=10)
# 
# # Start the Tkinter event loop
# root.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# import mysql.connector


# def execute_queries():
#     try:
#         # Connect to MySQL
#         conn = mysql.connector.connect(
#             host="localhost", user="root", password="", database="salestracker"
#         )

#         # Create a cursor object
#         cursor = conn.cursor()

#         # Create table if not exists
#         create_table_query = """
#             CREATE TABLE IF NOT EXISTS products (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 productname VARCHAR(255),
#                 amount INT
#             )
#         """
#         cursor.execute(create_table_query)

#         # Display success message
#         messagebox.showinfo("Success", "Table created successfully or already exists.")

#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error creating table: {err}")
#         return

#     finally:
#         # Close the cursor and connection
#         cursor.close()
#         conn.close()


# # Create main window
# root = tk.Tk()
# root.title("Execute MySQL Queries")

# # Create and pack a button
# btn_execute = tk.Button(root, text="Execute Queries", command=execute_queries)
# btn_execute.pack(pady=10)

# # Start the Tkinter event loop
# root.mainloop()


# import random
# import tkinter as tk
# from tkinter import messagebox

# import mysql.connector


# def generate_random_product_names():
#     # List of sample product names related to CCTV technology
#     product_names = [
#         "CCTV Camera",
#         "Dome Camera",
#         "Bullet Camera",
#         "IP Camera",
#         "PTZ Camera",
#         "DVR (Digital Video Recorder)",
#         "NVR (Network Video Recorder)",
#         "Security System",
#         "Surveillance Kit",
#         "Video Doorbell",
#         "Wireless Camera",
#         "Hidden Camera",
#         "Covert Camera",
#         "Security Camera System",
#         "Night Vision Camera",
#         "Outdoor Camera",
#         "Indoor Camera",
#         "Smart Home Security",
#         "Panoramic Camera",
#         "Fish-eye Camera",
#         "360-Degree Camera",
#         "Thermal Imaging Camera",
#         "License Plate Recognition Camera",
#         "AI-powered Camera",
#         "Facial Recognition Camera",
#         "Vandal-Proof Camera",
#         "Weatherproof Camera",
#         "Infrared Camera",
#         "Ultra HD Camera",
#         "PoE Camera",
#         "Solar-Powered Camera",
#         "Wireless Security System",
#         "Video Analytics Camera",
#         "Body-worn Camera",
#         "Mobile Surveillance",
#         "Smart Street Lighting with CCTV",
#         "Smart City Surveillance",
#         "Cloud-Based Surveillance",
#         "Biometric Access Control",
#         "CCTV Accessories",
#         "Security Monitoring",
#         "Public Safety Solutions",
#         "Wireless CCTV Transmitter",
#         "Mobile DVR",
#         "Thermal Body Temperature Camera",
#         "License Plate Capture System",
#         "AI-powered Analytics System",
#         "Remote Viewing System",
#         # ... (rest of the product names)
#     ]

#     # Ensure that the sample size is not larger than the population
#     sample_size = min(50, len(product_names))

#     # Randomly select product names
#     selected_product_names = random.sample(product_names, sample_size)

#     return selected_product_names


# def insert_data():
#     try:
#         # Connect to MySQL
#         conn = mysql.connector.connect(
#             host="localhost", user="root", password="", database="salestracker"
#         )

#         # Create a cursor object
#         cursor = conn.cursor()

#         # Generate random product names
#         product_names = generate_random_product_names()

#         # Insert data into the "products" table
#         for product_name in product_names:
#             amount = random.randint(100, 1000)  # Random amount between 100 and 1000
#             insert_query = f"INSERT INTO products (productname, amount) VALUES ('{product_name}', {amount})"
#             cursor.execute(insert_query)

#         # Commit the changes
#         conn.commit()

#         # Display success message
#         messagebox.showinfo("Success", "Data inserted successfully!")

#     except mysql.connector.Error as err:
#         # Display error message
#         messagebox.showerror("Error", f"Error inserting data: {err}")

#     finally:
#         # Close the cursor and connection
#         cursor.close()
#         conn.close()


# # Create main window
# root = tk.Tk()
# root.title("Insert Random Data into Products")

# # Create and pack a button to insert data
# btn_insert_data = tk.Button(root, text="Insert Data", command=insert_data)
# btn_insert_data.pack(pady=10)

# # Start the Tkinter event loop
# root.mainloop()
