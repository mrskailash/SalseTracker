import sqlite3
import tkinter as tk
from tkinter import ttk

import mysql.connector
from PIL import Image, ImageTk
from tkcalendar import DateEntry


class LeadHeader:
    search_icon = None
    date_filter_icon = None
    refresh_icon = None
    add_icon = None
    ok_icon = None
    close_icon = None

    def __init__(self, parent):
        self.parent = parent
        self.open_detail_windows = []

        def search_window():
            search_window = tk.Toplevel(parent)
            search_window.title("Search Window")
            search_window.geometry("450x170+1000+80")
            search_window.resizable(False, False)

            name_label = tk.Label(search_window, text="Name", font=("Arial", 12))
            name_label.grid(row=0, column=0, padx=5, pady=10)

            name_entry = tk.Entry(search_window, width=25)
            name_entry.grid(row=0, column=1, padx=5, pady=10)

            text_label = tk.Label(search_window, text="By Text", font=("Arial", 12))
            text_label.grid(row=1, column=0, pady=10)

            by_text_option = [
                "(none)",
                "address",
                "contact person",
                "email",
                "notes",
                "telephone",
            ]
            text_combobox = ttk.Combobox(search_window, values=by_text_option)
            text_combobox.grid(row=1, column=1, padx=5, pady=10)

            text_entry = tk.Entry(search_window, width=25)
            text_entry.grid(row=1, column=2, padx=5, pady=10)

            dropdown_label = tk.Label(
                search_window, text="By Dropdown", font=("Arial", 12)
            )
            dropdown_label.grid(row=2, column=0, pady=10)

            dropdown_option = ["(none)", "Closure", "Source"]
            dropdown_combobox = ttk.Combobox(search_window, values=dropdown_option)
            dropdown_combobox.grid(row=2, column=1, pady=10)

            dropdown_sub_option = ["-OPEN-", "close", "won", "lost"]
            dropdown_sub_combobox = ttk.Combobox(
                search_window, values=dropdown_sub_option
            )
            dropdown_sub_combobox.grid(row=2, column=2, pady=10)

            search_btn = tk.Button(search_window, text="Search", font=("Arial", 12))
            search_btn.place(x=365, y=135)

        def show_date_window():
            date_window = tk.Toplevel(parent)
            date_window.title("Date Filter Window")
            date_window.geometry("450x100+1000+80")
            # date_window.resizable(False, False)

            from_label = tk.Label(date_window, text="From")
            from_label.grid(row=0, column=0, pady=10, padx=5)

            from_date_entry = DateEntry(date_window, width=25)
            from_date_entry.grid(row=0, column=1, pady=10, padx=5)

            to_label = tk.Label(date_window, text="to", pady=10, padx=5)
            to_label.grid(row=0, column=2)

            to_date_entry = DateEntry(date_window, width=25)
            to_date_entry.grid(row=0, column=3, pady=10, padx=5)

            search_btn = tk.Button(date_window, text="Search", font=("Arial", 12))
            search_btn.place(x=210, y=50)

        def fetch_lead_data():
            # Connect to MySQL server
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Fetch data from the leadlist table
            cursor.execute(
                "SELECT id, date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company FROM leadlist"
            )

            lead_data = cursor.fetchall()

            # Close the database connection
            conn.commit()
            conn.close()
            # Clear existing data in the treeview
            self.tree.delete(*self.tree.get_children())

            return lead_data

        def populate_treeview():
            lead_data = fetch_lead_data()

            for lead_row in lead_data:
                (
                    lead_no,
                    date,
                    name,
                    address,
                    mobile,
                    email,
                    source,
                    assignto,
                    status,
                    refrenceby,
                    product,
                    remark,
                    company,
                ) = lead_row
                self.tree.insert(
                    "",
                    "end",
                    values=(
                        lead_no,
                        date,
                        name,
                        address,
                        mobile,
                        email,
                        source,
                        assignto,
                        status,
                        refrenceby,
                        product,
                        remark,
                        company,
                    ),
                )

        def on_double_click(event):
            item = self.tree.selection()
            if item:
                selected_lead_data = self.tree.item(item, "values")[:2]
            open_detail_window(selected_lead_data)

        def open_detail_window(selected_lead_data):
            def close_detail_window():
                self.open_detail_windows.remove(detail_window)
                detail_window.destroy()

            detail_window = tk.Toplevel(parent)
            detail_window.geometry(f"500x800+{1000}+{10}")
            detail_window.title("Custom Location Window")
            lead_no, name = selected_lead_data
            detail_window.title(f"Lead Details - Lead No: {lead_no}, Name: {name}")
            # Close any existing detail window
            if self.open_detail_windows:
                existing_window = self.open_detail_windows[0]
                existing_window.destroy()
                self.open_detail_windows.clear()
            self.open_detail_windows.append(detail_window)
            self.open_detail_windows.append(detail_window)

            self.ok_icon = Image.open("asset/Lead_icon/check.png")
            self.ok_icon = self.ok_icon.resize((25, 25))
            self.ok_icon = ImageTk.PhotoImage(self.ok_icon)

            ok_btn = tk.Button(
                detail_window,
                image=self.ok_icon,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
            )
            ok_btn.place(x=12, y=8)

            ok_label = tk.Label(detail_window, text="ok")
            ok_label.place(x=10, y=35)

            self.close_icon = Image.open("asset/Lead_icon/close.png")
            self.close_icon = self.close_icon.resize((25, 25))
            self.close_icon = ImageTk.PhotoImage(self.close_icon)

            close_btn = tk.Button(
                detail_window,
                image=self.close_icon,
                borderwidth=2,
                highlightthickness=0,
                relief="flat",
                command=close_detail_window,
            )
            close_btn.place(x=450, y=8)

            close_label = tk.Label(detail_window, text="close")
            close_label.place(x=450, y=35)

            separator1 = tk.Frame(detail_window, height=2, width=490, bg="black")
            separator1.place(y=55)

            followup1_label = tk.Label(detail_window, text="Follow Up-1")
            followup1_label.place(x=10, y=70)

            followup1 = tk.Text(detail_window, wrap=tk.WORD, width=57, height=6)
            followup1.place(x=10, y=90)

            followup2_label = tk.Label(detail_window, text="Follow Up-2")
            followup2_label.place(x=10, y=190)

            followup2 = tk.Text(detail_window, wrap=tk.WORD, width=57, height=6)
            followup2.place(x=10, y=210)

            followup3_label = tk.Label(detail_window, text="Follow Up-3")
            followup3_label.place(x=10, y=310)

            followup3 = tk.Text(detail_window, wrap=tk.WORD, width=57, height=6)
            followup3.place(x=10, y=330)

            followup4_label = tk.Label(detail_window, text="Follow Up-4")
            followup4_label.place(x=10, y=430)

            followup4 = tk.Text(detail_window, wrap=tk.WORD, width=57, height=6)
            followup4.place(x=10, y=450)

            followup5_label = tk.Label(detail_window, text="Follow Up-5")
            followup5_label.place(x=10, y=550)

            followup5 = tk.Text(detail_window, wrap=tk.WORD, width=57, height=6)
            followup5.place(x=10, y=570)

            followup6_label = tk.Label(detail_window, text="Follow Up-6")
            followup6_label.place(x=10, y=670)

            followup6 = tk.Text(detail_window, wrap=tk.WORD, width=57, height=6)
            followup6.place(x=10, y=690)

        def open_context_menu(event):
            item = self.tree.selection()
            if item:
                menu.post(event.x_root, event.y_root)

        def add_followup():
            on_double_click(None)

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
            command=populate_treeview,
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
            command=show_date_window,
        )
        date_filter_button.grid(row=0, column=1, padx=5)

        date_filter_text = tk.Label(
            lead_heading_menu5,
            text="Date Filter",
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
            text="Search",
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
                "Address",
                "Mobile",
                "Email",
                "Source",
                "Assign To",
                "Status",
                "Referance By ",
                "Products",
                "Remark",
                "Company",
            ),
            show="headings",
        )

        headings = [
            "Lead No",
            "Date",
            "Name",
            "Address",
            "Mobile",
            "Email",
            "Source",
            "Assign To",
            "Status",
            "Referance By ",
            "Products",
            "Remark",
            "Company",
        ]
        for i, headings in enumerate(headings):
            self.tree.heading(i, text=headings, anchor="center")

        self.tree.column("Lead No", width=50, anchor="center")
        self.tree.column("Date", width=50, anchor="center")
        self.tree.column("Name", width=50, anchor="center")
        self.tree.column("Address", width=50, anchor="center")
        self.tree.column("Mobile", width=50, anchor="center")
        self.tree.column("Email", width=50, anchor="center")
        self.tree.column("Source", width=50, anchor="center")
        self.tree.column("Assign To", width=50, anchor="center")
        self.tree.column("Status", width=50, anchor="center")
        self.tree.column("Referance By ", width=50, anchor="center")
        self.tree.column("Products", width=50, anchor="center")
        self.tree.column("Remark", width=50, anchor="center")
        self.tree.column("Company", width=50, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=45)
        self.tree.bind("<Double-1>", on_double_click)
        self.tree.bind("<Button-3>", open_context_menu)  # Right-click event

        menu = tk.Menu(self.tree, tearoff=0)
        menu.add_command(label="Add", command=add_followup)
        menu.add_command(
            label="View",
        )
        menu.add_command(
            label="Edit",
        )

        # Fetch data and populate the table
        populate_treeview()
