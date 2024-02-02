import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class Users:
    search_icon = None
    date_filter_icon = None
    refresh_icon = None

    def __init__(self, parent):
        self.parent = parent

        def center_window(window, width, height):
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x_coordinate = int((screen_width - width) / 2)
            y_coordinate = int((screen_height - height) / 2)
            window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        def search_window():
            search_window = tk.Toplevel(parent)
            search_window.title("Small Window")
            search_window.geometry("500x50")
            center_window(search_window, 487, 348)
            search_window.resizable(False, False)
            search_window.title("Product Details")

        def fetch_employe_data():
            # Connect to MySQL server
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()
            # Fetch data from the leadlist table
            cursor.execute("SELECT Uname, name, type FROM user")
            lead_data = cursor.fetchall()

            # Close the database connection
            conn.commit()
            conn.close()

            # Clear existing data in the treeview
            self.tree.delete(*self.tree.get_children())

            # Insert fetched data into the treeview
            for leadrow in lead_data:
                (uname, name, employee_type) = leadrow
                self.tree.insert("", "end", values=(uname, name, employee_type))

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
            command=fetch_employe_data,
        )
        refresh_button.grid(row=0, column=1, padx=5)

        refresh_text = tk.Label(
            lead_heading_menu4,
            text="refresh",
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
            command=search_window,
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

        lead_list_text = tk.Label(parent, text="User List", font=("Arial", 16))
        lead_list_text.place(x=15, y=80)

        self.tree = ttk.Treeview(
            parent,
            columns=("name", "Login Name", "Profile type"),
            show="headings",
            height=10,
        )
        headings = ["name", "Login Name", "Profile type"]
        for i, headings in enumerate(headings):
            self.tree.heading(i, text=headings, anchor="center")

        self.tree.column(
            "name",
            anchor="center",
        )
        self.tree.column(
            "Login Name",
            anchor="center",
        )
        self.tree.column(
            "Profile type",
            anchor="center",
        )

        self.tree.pack(fill="y", side=tk.LEFT, padx=10, pady=45)

        userentry = tk.Frame(
            parent, relief="solid", borderwidth=2, bg="white", height=600, width=750
        )
        userentry.place(x=615, y=112)
        userentry.grid_propagate(False)

        name = tk.Label(userentry, text="Name", font=("Arial", 12), bg="white")
        name.grid(column=0, row=0, padx=15, pady=12)

        name_entry = tk.Entry(
            userentry, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=50
        )
        name_entry.grid(column=1, row=0, padx=15, pady=12)

        mobile = tk.Label(userentry, text="Mobile no", font=("Arial", 12), bg="white")
        mobile.grid(column=0, row=1, padx=15, pady=12)

        mobile_entry = tk.Entry(
            userentry, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=50
        )
        mobile_entry.grid(column=1, row=1, padx=15, pady=12)

        email = tk.Label(userentry, text="Email", font=("Arial", 12), bg="white")
        email.grid(column=0, row=2, padx=15, pady=12)

        email_entry = tk.Entry(
            userentry, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=50
        )
        email_entry.grid(column=1, row=2, padx=15, pady=12)

        profile = tk.Label(userentry, text="profile", font=("Arial", 12), bg="white")
        profile.grid(column=0, row=3, padx=15, pady=12)

        profile_entry = tk.Entry(
            userentry, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=50
        )
        profile_entry.grid(column=1, row=3, padx=15, pady=12)
        # Fetch data and populate the table
        fetch_employe_data()
