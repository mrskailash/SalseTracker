import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class Closure:
    filter_icon = None
    search_icon = None
    date_filter_icon = None
    refresh_icon = None

    def __init__(self, parent):
        self.parent = parent

        def fetch_filter_lead(option):
            # Implement the logic to fetch data based on the selected filter option
            # Connect to SQLite database (replace 'your_database.db' with the actual database file)
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Fetch data from the 'leadlist' table based on the selected filter option
            cursor.execute(
                "SELECT id, date, fullname, address, email, status FROM leadlist WHERE status = ?",
                (option,),
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

        def fetch_lead_open_data():
            # Connect to SQLite database (replace 'your_database.db' with the actual database file)
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Fetch data from the 'leadlist' table
            cursor.execute(
                "SELECT id, date, fullname, address, email, status FROM leadlist WHERE LOWER(status) = 'open'"
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

        lead_heading_menu3 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu3.place(x=10, y=10)

        lead_heading_menu4 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu4.place(x=80, y=10)

        lead_heading_menu5 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu5.place(x=150, y=10)

        lead_heading_menu6 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu6.place(x=230, y=10)

        def show_menu(filtermenu, button):

            filtermenu.post(
                button.winfo_rootx(), button.winfo_rooty() + button.winfo_height()
            )

        connection = sqlite3.connect(
            "salestracker.db"
        )  # Replace with your actual database file
        cursor = connection.cursor()
        cursor.execute("SELECT statustype FROM status")
        status_options = [rows[0] for rows in cursor.fetchall()]

        status_menu = tk.Menu(lead_heading_menu3, tearoff=0)

        for option in status_options:
            status_menu.add_command(
                label=option,
                command=lambda opt=option: fetch_filter_lead(opt),
            )
        self.filter_icon = Image.open("asset/filter_icon/filter.png")
        self.filter_icon = self.filter_icon.resize((25, 25))
        self.filter_icon = ImageTk.PhotoImage(self.filter_icon)

        filtermenu_button = tk.Button(
            lead_heading_menu3,
            image=self.filter_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            command=lambda: show_menu(status_menu, filtermenu_button),
        )
        filtermenu_button.grid(
            row=0,
            column=0,
            padx=15,
        )

        filterlable = tk.Label(
            lead_heading_menu3, text="Filter", bg="white", font=("Arial", 12)
        )
        filterlable.grid(row=1, column=0, padx=15, pady=2)
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
            command=fetch_lead_open_data,
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

        def change_status_option(option):
            item = self.tree.selection()
            if item:
                selected_lead_data = self.tree.item(item, "values")[:2]
                lead_id = selected_lead_data[0]
                title = f"Change Status - ID: {lead_id}"
                result = messagebox.askokcancel(
                    title, f"Do you want to change the status to {option}?"
                )

                if result:
                    update_lead_data(lead_id, option)

        def update_lead_data(lead_id, new_status):
            # Connect to your SQLite database
            connection = sqlite3.connect("salestracker.db")

            # Create a cursor object
            cursor = connection.cursor()

            # Update the 'status' column to the specified new_status for the specified lead_id
            cursor.execute(
                "UPDATE leadlist SET status = ? WHERE id = ?", (new_status, lead_id)
            )

            # Commit the changes
            connection.commit()

            # Close the database connection
            connection.close()

        def open_context_menu(event):
            item = self.tree.selection()
            if item:
                menu.post(event.x_root, event.y_root)

        # Modify your existing menu creation code to include the change_status_option function

        connection = sqlite3.connect("salestracker.db")
        cursor = connection.cursor()
        cursor.execute("SELECT statustype FROM status")
        change_status_options = [rows[0] for rows in cursor.fetchall()]

        # Add filtering options for Status
        change_status_menu = tk.Menu(self.tree, tearoff=0)

        for option in change_status_options:
            change_status_menu.add_command(
                label=option,
                command=lambda opt=option: change_status_option(opt),
            )

        # Assuming `self.tree` is the parent widget for the menu
        menu = tk.Menu(self.tree, tearoff=0)
        menu.add_cascade(label="Change Status", menu=change_status_menu)

        self.tree.bind("<Button-3>", open_context_menu)  # Right-click event
        fetch_lead_open_data()
