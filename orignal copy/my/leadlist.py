import tkinter as tk
from tkinter import messagebox, ttk

import mysql.connector
from PIL import Image, ImageTk
from tkcalendar import DateEntry


class LeadHeader:
    search_icon = None
    date_filter_icon = None
    refresh_icon = None

    def __init__(self, parent):
        self.parent = parent

        def search_window():
            search_window = tk.Toplevel(parent)
            search_window.title("Small Window")
            search_window.geometry("50x50")
            search_window.resizable(False, False)
            search_window.title("product Details")

        def fetch_lead_data():
            # Connect to MySQL server
            db_connection = mysql.connector.connect(
                host="localhost", user="root", password="", database="salestracker"
            )

            # Create a cursor object
            cursor = db_connection.cursor()

            # Fetch data from the leadlist table
            cursor.execute("SELECT id, date, name, salesperson, asignto FROM leadlist")
            lead_data = cursor.fetchall()

            # Close the database connection
            cursor.close()
            db_connection.close()

            # Clear existing data in the treeview
            self.tree.delete(*self.tree.get_children())

            # Insert fetched data into the treeview
            for leadrow in lead_data:
                (lead_no, date, name, contact_person, assign_to) = leadrow
                self.tree.insert(
                    "", "end", values=(lead_no, date, name, contact_person, assign_to)
                )

        lead_heading = tk.Frame(parent, bg="gray", width=1505, height=80)
        lead_heading.pack(side=tk.TOP, anchor=tk.NW)

        separator = tk.Frame(parent, bg="black", height=2, width=1510)
        separator.pack(pady=5)

        lead_heading_menu4 = tk.Frame(lead_heading, bg="gray", height=50, width=55)
        lead_heading_menu4.place(x=12, y=10)

        lead_heading_menu5 = tk.Frame(lead_heading, bg="gray", height=50, width=55)
        lead_heading_menu5.place(x=80, y=10)

        lead_heading_menu6 = tk.Frame(lead_heading, bg="gray", height=50, width=55)
        lead_heading_menu6.place(x=150, y=10)

        self.refresh_icon = Image.open("asset/Lead_icon/refresh.png")
        self.refresh_icon = self.refresh_icon.resize((30, 30))
        self.refresh_icon = ImageTk.PhotoImage(self.refresh_icon)

        refresh_button = tk.Button(
            lead_heading_menu4,
            image=self.refresh_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="gray",
            height=30,
            width=30,
            command=fetch_lead_data,
        )
        refresh_button.grid(row=0, column=1, padx=5)

        refresh_text = tk.Label(
            lead_heading_menu4,
            text="refresh",
            fg="white",
            bg="gray",
            font=("Arial", 12),
        )
        refresh_text.grid(row=1, column=1)

        self.date_filter_icon = Image.open("asset/Lead_icon/calendar.png")
        self.date_filter_icon = self.date_filter_icon.resize((30, 30))
        self.date_filter_icon = ImageTk.PhotoImage(self.date_filter_icon)

        date_filter_button = tk.Button(
            lead_heading_menu5,
            image=self.date_filter_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="gray",
            height=30,
            width=30,
        )
        date_filter_button.grid(row=0, column=1, padx=5)

        date_filter_text = tk.Label(
            lead_heading_menu5,
            text="date filter",
            fg="white",
            bg="gray",
            font=("Arial", 12),
        )
        date_filter_text.grid(row=1, column=1)

        self.search_icon = Image.open("asset/Lead_icon/search.png")
        self.search_icon = self.search_icon.resize((30, 30))
        self.search_icon = ImageTk.PhotoImage(self.search_icon)

        search_button = tk.Button(
            lead_heading_menu6,
            image=self.search_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="gray",
            height=30,
            width=30,
            command=search_window,
        )
        search_button.grid(row=0, column=1, padx=5)

        search_text = tk.Label(
            lead_heading_menu6, text="search", fg="white", bg="gray", font=("Arial", 12)
        )
        search_text.grid(row=1, column=1)

        lead_list_text = tk.Label(parent, text="Lead List", font=("Arial", 16))
        lead_list_text.place(x=5, y=100)

        self.tree = ttk.Treeview(
            parent,
            columns=("ID", "Date", "Name", "Sales Person", "Assign To"),
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Sales Person", text="Sales Person")
        self.tree.heading("Assign To", text="Assign To")

        self.tree.pack(fill="both", expand=True, padx=10, pady=45)

        # Fetch data and populate the table
        fetch_lead_data()
