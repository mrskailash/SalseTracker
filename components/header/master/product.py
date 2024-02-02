import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk
from tkcalendar import DateEntry


class Product:
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

        def fetch_product_names():
            # Connect to MySQL server
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Fetch product names from the database
            cursor.execute("SELECT id,productname FROM products")
            product_names = cursor.fetchall()

            # Close the database connection
            conn.commit()
            conn.close()

            for lead_row in product_names:
                (
                    id,
                    name,
                ) = lead_row
                self.tree.insert("", "end", values=(id, name, ""))

        lead_heading = tk.Frame(parent, bg="white", width=1300, height=55)
        lead_heading.pack(side=tk.TOP, anchor=tk.NW)

        separator = tk.Frame(parent, bg="black", height=2, width=1510)
        separator.pack(pady=5)

        lead_heading_menu1 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu1.place(x=12, y=8)

        lead_heading_menu2 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu2.place(x=80, y=8)

        lead_heading_menu3 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu3.place(x=150, y=8)

        lead_heading_menu4 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu4.place(x=220, y=10)

        lead_heading_menu6 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu6.place(x=290, y=10)

        self.add_icon = Image.open("asset/Lead_icon/plus.png")
        self.add_icon = self.add_icon.resize((25, 25))
        self.add_icon = ImageTk.PhotoImage(self.add_icon)

        add_button = tk.Button(
            lead_heading_menu1,
            image=self.add_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            # command=clear_entries,
        )
        add_button.grid(row=0, column=1, padx=5)

        add_text = tk.Label(
            lead_heading_menu1, text="new", fg="black", bg="white", font=("Arial", 12)
        )
        add_text.grid(row=1, column=1)

        self.save_icon = Image.open("asset/Lead_icon/diskette.png")
        self.save_icon = self.save_icon.resize((25, 25))
        self.save_icon = ImageTk.PhotoImage(self.save_icon)

        save_button = tk.Button(
            lead_heading_menu2,
            image=self.save_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
        )
        save_button.grid(row=0, column=1, padx=5)

        save_text = tk.Label(
            lead_heading_menu2, text="save", fg="black", bg="white", font=("Arial", 12)
        )
        save_text.grid(row=1, column=1)

        self.delete_icon = Image.open("asset/Lead_icon/delete.png")
        self.delete_icon = self.delete_icon.resize((25, 25))
        self.delete_icon = ImageTk.PhotoImage(self.delete_icon)

        delete_button = tk.Button(
            lead_heading_menu3,
            image=self.delete_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
        )
        delete_button.grid(row=0, column=1, padx=5)

        delete_text = tk.Label(
            lead_heading_menu3,
            text="delete",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        delete_text.grid(row=1, column=1)
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
            # command=fetch_lead_data,
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

        lead_list_text = tk.Label(
            parent, text="Product List", bg="white", font=("Arial", 16)
        )
        lead_list_text.place(x=5, y=70)

        self.tree = ttk.Treeview(
            parent,
            columns=("id", "Name", "Description"),
            show="headings",
        )
        headings = ["id", "Name", "Description"]
        for i, headings in enumerate(headings):
            self.tree.heading(i, text=headings, anchor="center")

        self.tree.column("id", anchor="center")
        self.tree.column("Name", anchor="center")
        self.tree.column("Description", anchor="center")

        self.tree.pack(side=tk.LEFT, fill="y", pady=30, padx=5)

        productentry = tk.Frame(
            parent, relief="solid", borderwidth=2, bg="white", height=648, width=750
        )
        productentry.place(x=610, y=98)
        productentry.grid_propagate(False)
        product_name = tk.Label(
            productentry, text="Product Name", font=("Arial", 12), bg="white"
        )
        product_name.grid(column=0, row=0, padx=15, pady=12)

        product_name_entry = tk.Entry(
            productentry,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=50,
        )
        product_name_entry.grid(column=1, row=0, padx=15, pady=12)

        Description = tk.Label(
            productentry, text="Description", font=("Arial", 12), bg="white"
        )
        Description.grid(column=0, row=1)

        Description_entry = tk.Text(
            productentry,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=38,
            height=5,
        )
        Description_entry.place(x=150, y=50)

        fetch_product_names()
