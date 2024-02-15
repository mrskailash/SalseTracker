import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class Closure:
    search_icon = None
    date_filter_icon = None
    refresh_icon = None

    def __init__(self, parent):
        self.parent = parent

        def fetch_lead_data():
            # Connect to SQLite database (replace 'your_database.db' with the actual database file)
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Fetch data from the 'leadlist' table
            cursor.execute(
                "SELECT id, date, fullname, address, email, status FROM leadlist"
            )
            data = cursor.fetchall()

            # Clear existing data in the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insert fetched data into the Treeview
            for row in data:
                self.tree.insert("", "end", values=row)

            # Commit and close the connection
            conn.commit()
            conn.close()

        lead_heading = tk.Frame(parent, bg="white", width=1300, height=55)
        lead_heading.pack(side=tk.TOP, anchor=tk.NW)

        separator = tk.Frame(parent, bg="black", height=2, width=1510)
        separator.pack(pady=5)

        lead_heading_menu4 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu4.place(x=12, y=10)

        lead_heading_menu5 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu5.place(x=80, y=10)

        lead_heading_menu6 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu6.place(x=150, y=10)

        self.refresh_icon = Image.open("asset/Lead_icon/refresh.png")
        self.refresh_icon = self.refresh_icon.resize((25, 25))
        self.refresh_icon = ImageTk.PhotoImage(self.refresh_icon)

        refresh_button = tk.Button(
            lead_heading_menu4,
            image=self.refresh_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            command=fetch_lead_data,
        )
        refresh_button.grid(row=0, column=1, padx=5)

        refresh_text = tk.Label(
            lead_heading_menu4,
            text="Refresh",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        refresh_text.grid(row=1, column=1)

        self.date_filter_icon = Image.open("asset/Lead_icon/calendar.png")
        self.date_filter_icon = self.date_filter_icon.resize((25, 25))
        self.date_filter_icon = ImageTk.PhotoImage(self.date_filter_icon)

        date_filter_button = tk.Button(
            lead_heading_menu5,
            image=self.date_filter_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
        )
        date_filter_button.grid(row=0, column=1, padx=5)

        date_filter_text = tk.Label(
            lead_heading_menu5,
            text="date filter",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        date_filter_text.grid(row=1, column=1)

        self.search_icon = Image.open("asset/Lead_icon/search.png")
        self.search_icon = self.search_icon.resize((25, 25))
        self.search_icon = ImageTk.PhotoImage(self.search_icon)

        search_button = tk.Button(
            lead_heading_menu6,
            image=self.search_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            # command=search_window,
        )
        search_button.grid(row=0, column=1, padx=5)

        search_text = tk.Label(
            lead_heading_menu6,
            text="search",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        search_text.grid(row=1, column=1)

        lead_list_text = tk.Label(parent, text="Open Lead", font=("Arial", 16))
        lead_list_text.place(x=15, y=80)

        self.tree = ttk.Treeview(
            parent,
            columns=(
                "Lead No",
                "Date",
                "Name",
                "Address",
                "Email",
                "Status",
            ),
            show="headings",
        )
        headings = [
            "Lead No",
            "Date",
            "Name",
            "Address",
            "Email",
            "Status",
        ]
        for i, headings in enumerate(headings):
            self.tree.heading(i, text=headings, anchor="center")

        self.tree.column("Lead No", width=50, anchor="center")
        self.tree.column("Date", width=50, anchor="center")
        self.tree.column("Name", width=50, anchor="center")
        self.tree.column("Address", width=50, anchor="center")
        self.tree.column("Email", width=50, anchor="center")
        self.tree.column("Status", width=50, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=45)

        def closelead(selected_lead_data=None):
            if selected_lead_data:
                lead_id = selected_lead_data[0]
                title = f"Close Lead - ID: {lead_id}"
            else:
                title = "Close Lead"
                # Create a message box
            result = messagebox.askokcancel(title, "Do you want to Close This lead ?")

            # Check the result and update the status if OK button is clicked
            if result and selected_lead_data:
                update_lead_data(lead_id)

        def on_double_click(event):
            item = self.tree.selection()
            if item:
                selected_lead_data = self.tree.item(item, "values")[:2]
                closelead(selected_lead_data)

        def update_lead_data(lead_id):
            # Connect to your SQLite database
            connection = sqlite3.connect(
                "salestracker.db"
            )  # Replace with your database name

            # Create a cursor object
            cursor = connection.cursor()

            # Update the 'status' column to 'close' for the specified lead_id
            cursor.execute(
                "UPDATE leadlist SET status = 'close' WHERE id = ?", (lead_id,)
            )

            # Commit the changes
            connection.commit()

            # Close the database connection
            connection.close()

        def open_context_menu(event):
            item = self.tree.selection()
            if item:
                menu.post(event.x_root, event.y_root)

        menu = tk.Menu(self.tree, tearoff=0)
        menu.add_command(label="Close Lead", command=closelead)
        self.tree.bind("<Button-3>", open_context_menu)  # Right-click event
        self.tree.bind("<Double-1>", on_double_click)
        fetch_lead_data()
