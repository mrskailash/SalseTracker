import tkinter as tk
from tkinter import ttk

import mysql.connector


class TreeviewTable:
    def __init__(self, root):
        self.root = root
        self.root.title("Treeview Table")

        # Create Treeview widget
        self.tree = ttk.Treeview(
            root,
            columns=(
                "ID",
                "Name",
                "Sales Person",
                "Address",
                "Email",
                "Source",
                "Assign To",
                "Status",
            ),
        )

        # Set column headings
        self.tree.heading("#0", text="Row Name")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Sales Person", text="Sales Person")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Source", text="Source")
        self.tree.heading("Assign To", text="Assign To")
        self.tree.heading("Status", text="Status")

        # Add Treeview to the window
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Fetch data and populate the table
        self.fetch_lead_data()

    def fetch_lead_data(self):
        # Connect to MySQL server
        db_connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="salestracker"
        )

        # Create a cursor object
        cursor = db_connection.cursor()

        # Fetch data from the leadlist table
        cursor.execute(
            "SELECT id, name, salesperson, address, email, source, asignto, status FROM leadlist"
        )
        lead_data = cursor.fetchall()

        # Close the database connection
        cursor.close()
        db_connection.close()

        # Clear existing data in the treeview
        self.tree.delete(*self.tree.get_children())

        # Insert fetched data into the treeview
        for row in lead_data:
            (
                lead_id,
                name,
                sales_person,
                address,
                email,
                source,
                assign_to,
                status,
            ) = row
            self.tree.insert(
                "",
                "end",
                values=(
                    lead_id,
                    name,
                    sales_person,
                    address,
                    email,
                    source,
                    assign_to,
                    status,
                ),
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = TreeviewTable(root)
    root.mainloop()
