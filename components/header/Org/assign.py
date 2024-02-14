import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class Assign:
    search_icon = None
    date_filter_icon = None
    refresh_icon = None
    filter_icon = None

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

        def fetch_lead_data(self):
            # Connect to SQLite database (replace 'your_database.db' with the actual database file)
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Fetch data from the 'leadlist' table
            cursor.execute(
                "SELECT id, date, fullname, address, email, assignto FROM leadlist"
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
        separator.pack(pady=10)

        lead_heading_menu4 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu4.place(x=12, y=10)

        lead_heading_menu5 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu5.place(x=80, y=10)

        # lead_heading_menu6 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        # lead_heading_menu6.place(x=80, y=10)

        self.refresh_icon = Image.open("asset/assign/user-check.png")
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
            # command=fetch_lead_data,
        )
        refresh_button.grid(row=0, column=1)

        refresh_text = tk.Label(
            lead_heading_menu4,
            text="assign",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        refresh_text.grid(row=1, column=1)

        def show_filter(filtermenu, button):

            filtermenu.post(
                button.winfo_rootx(), button.winfo_rooty() + button.winfo_height()
            )

        menu_font = ("Arial", 12)
        filtermenu = tk.Menu(lead_heading_menu5, tearoff=0, font=menu_font)
        assign_menu = tk.Menu(filtermenu, tearoff=0)
        filtermenu.add_cascade(label="By Assign", menu=assign_menu)
        assign_options = ["SalesRep1", "SalesRep2"]
        for option in assign_options:
            assign_menu.add_command(label=option)
        self.filter_icon = Image.open("asset/filter_icon/filter.png")
        self.filter_icon = self.filter_icon.resize((25, 25))
        self.filter_icon = ImageTk.PhotoImage(self.filter_icon)

        filtermenu_button = tk.Button(
            lead_heading_menu5,
            image=self.filter_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            command=lambda: show_filter(filtermenu, filtermenu_button),
        )
        filtermenu_button.grid(
            row=0,
            column=1,
        )

        filterlable = tk.Label(
            lead_heading_menu5, text="Filter", bg="white", font=("Arial", 12)
        )
        filterlable.grid(row=1, column=1)

        # self.search_icon = Image.open("asset/Lead_icon/search.png")
        # self.search_icon = self.search_icon.resize((25, 25))
        # self.search_icon = ImageTk.PhotoImage(self.search_icon)

        # search_button = tk.Button(
        #     lead_heading_menu6,
        #     image=self.search_icon,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     bg="white",
        #     height=25,
        #     width=25,
        #     command=search_window,
        # )
        # search_button.grid(row=0, column=1)

        # search_text = tk.Label(
        #     lead_heading_menu6,
        #     text="search",
        #     fg="black",
        #     bg="white",
        #     font=("Arial", 12),
        # )
        # search_text.grid(row=1, column=1)

        lead_list_text = tk.Label(parent, text="Lead List", font=("Arial", 16))
        lead_list_text.place(x=15, y=80)

        self.tree = ttk.Treeview(
            parent,
            columns=(
                "Lead No",
                "Date",
                "Name",
                "Address",
                "Email",
                "Assign To",
            ),
            show="headings",
            height=10,
        )
        headings = [
            "Lead No",
            "Date",
            "Name",
            "Address",
            "Email",
            "Assign To",
        ]
        for i, headings in enumerate(headings):
            self.tree.heading(i, text=headings, anchor="center")

        self.tree.column("Lead No", width=50, anchor="center")
        self.tree.column("Date", width=50, anchor="center")
        self.tree.column("Name", width=50, anchor="center")
        self.tree.column("Address", width=50, anchor="center")
        self.tree.column("Email", width=50, anchor="center")
        self.tree.column("Assign To", width=50, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=45)

        fetch_lead_data(self)
