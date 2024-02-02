import tkinter as tk
from tkinter import messagebox, ttk

import mysql.connector
from PIL import Image, ImageTk


class Assign:
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
        refresh_button.grid(row=0, column=1, padx=5)

        refresh_text = tk.Label(
            lead_heading_menu4,
            text="assign",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        refresh_text.grid(row=1, column=1)

        # self.date_filter_icon = Image.open("asset/Lead_icon/calendar.png")
        # self.date_filter_icon = self.date_filter_icon.resize((25, 25))
        # self.date_filter_icon = ImageTk.PhotoImage(self.date_filter_icon)

        # date_filter_button = tk.Button(
        #     lead_heading_menu5,
        #     image=self.date_filter_icon,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     bg="white",
        #     height=25,
        #     width=25,
        # )
        # date_filter_button.grid(row=0, column=1, padx=5)

        # date_filter_text = tk.Label(
        #     lead_heading_menu5,
        #     text="search",
        #     fg="black",
        #     bg="white",
        #     font=("Arial", 12),
        # )
        # date_filter_text.grid(row=1, column=1)

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
        search_button.grid(row=0, column=1)

        search_text = tk.Label(
            lead_heading_menu6,
            text="search",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        search_text.grid(row=1, column=1)

        lead_list_text = tk.Label(parent, text="Lead List", font=("Arial", 16))
        lead_list_text.place(x=15, y=80)

        self.tree = ttk.Treeview(
            parent,
            columns=(
                "Lead No",
                "Date",
                "Name",
                "Contact Person",
                "Amount",
                "Assign To",
            ),
            show="headings",
            height=10,
        )

        self.tree.heading("Lead No", text="Lead No")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Contact Person", text="Contact Person")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Assign To", text="Assign To")

        self.tree.pack(fill="both", expand=True, padx=10, pady=45)

        # Fetch data and populate the table
        # fetch_lead_data()
