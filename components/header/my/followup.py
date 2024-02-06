import sqlite3
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
from tkcalendar import DateEntry


class FollowUp:
    followup_icon = None
    view_icon = None
    search_icon = None
    date_filter_icon = None
    refresh_icon = None

    def __init__(self, parent):
        self.parent = parent

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
            cursor.execute("SELECT id,  date, fullname,address FROM leadlist")

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
                ) = lead_row
                self.tree.insert(
                    "",
                    "end",
                    values=(
                        lead_no,
                        date,
                        name,
                        address,
                    ),
                )

        def on_double_click(event):
            item = self.tree.selection()
            if item:
                open_detail_window(item)

        def open_detail_window(item):
            def center_window(window, width, height):
                screen_width = window.winfo_screenwidth()
                screen_height = window.winfo_screenheight()
                x_coordinate = int((screen_width - width) / 2)
                y_coordinate = int((screen_height - height) / 2)
                window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

            detail_window = tk.Toplevel(parent)
            detail_window.geometry("500x450")
            center_window(detail_window, 500, 450)
            detail_window.title("Custom Location Window")

            details_btn_clr = "#0086B3"
            history_btn = tk.Button(
                detail_window,
                text="History",
                bg=details_btn_clr,
                font=("Arial", 12),
                height=1,
                width=12,
            )
            history_btn.pack(side=tk.LEFT, anchor="n")

            details_container = tk.Frame(
                detail_window,
                height=450,
                width=500,
                borderwidth=0,
                relief=tk.GROOVE,
                highlightthickness=-0,
            )
            details_container.place(y=32)

            self.tree = ttk.Treeview(
                details_container,
                columns=("Lead No", "Date", "Notes"),
                show="headings",
            )
            headings = ["Lead No", "Date", "Notes"]
            for i, headings in enumerate(headings):
                self.tree.heading(i, text=headings, anchor="center")

            self.tree.column("Lead No", width=50, anchor="center")
            self.tree.column("Date", width=50, anchor="center")
            self.tree.column("Notes", width=50, anchor="center")

            self.tree.pack(fill="both", expand=True)

            info_container = tk.Frame(
                details_container,
                height=450,
                width=500,
                bg="white",
                borderwidth=0,
                relief=tk.GROOVE,
                highlightthickness=-0,
            )

            info_container.pack(fill=tk.BOTH, expand=True)
            info_container.grid_propagate(False)

        lead_heading = tk.Frame(parent, bg="white", width=1505, height=55)
        lead_heading.pack(side=tk.TOP, anchor=tk.NW)

        separator = tk.Frame(parent, bg="black", height=2, width=1510)
        separator.pack(pady=5)

        lead_heading_menu2 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu2.place(x=12, y=10)

        lead_heading_menu3 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu3.place(x=80, y=10)

        lead_heading_menu4 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu4.place(x=150, y=10)

        lead_heading_menu5 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu5.place(x=220, y=10)

        lead_heading_menu6 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu6.place(x=300, y=10)

        self.followup_icon = Image.open("asset/followup/call.png")
        self.followup_icon = self.followup_icon.resize((25, 25))
        self.followup_icon = ImageTk.PhotoImage(self.followup_icon)

        followup_button = tk.Button(
            lead_heading_menu2,
            image=self.followup_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            # command=fetch_lead_data,
        )
        followup_button.grid(row=0, column=1, padx=5)

        followup_text = tk.Label(
            lead_heading_menu2,
            text="followup",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        followup_text.grid(row=1, column=1)

        self.view_icon = Image.open("asset/followup/view.png")
        self.view_icon = self.view_icon.resize((25, 25))
        self.view_icon = ImageTk.PhotoImage(self.view_icon)

        view_button = tk.Button(
            lead_heading_menu3,
            image=self.view_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
        )
        view_button.grid(row=0, column=1, padx=5)

        view_text = tk.Label(
            lead_heading_menu3,
            text="View",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        view_text.grid(row=1, column=1)

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
            command=show_date_window,
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

        lead_list_text = tk.Label(
            parent, text="Pending for Followup", font=("Arial", 16)
        )
        lead_list_text.place(x=5, y=80)
        self.tree = ttk.Treeview(
            parent,
            columns=(
                "Lead No",
                "Date",
                "Name",
                "Location",
                "Follow up 1",
                "Follow up 2",
                "Follow up 3",
                "Follow up 4",
                "Follow up 5",
                "Follow up 6",
            ),
            show="headings",
            height=10,
        )

        headings = [
            "Lead No",
            "Date",
            "Name",
            "Location",
            "Follow up 1",
            "Follow up 2",
            "Follow up 3",
            "Follow up 4",
            "Follow up 5",
            "Follow up 6",
        ]
        for i, headings in enumerate(headings):
            self.tree.heading(i, text=headings, anchor="center")
        self.tree.column("Lead No", width=50, anchor="center")
        self.tree.column("Date", width=50, anchor="center")
        self.tree.column("Name", width=50, anchor="center")
        self.tree.column("Location", width=50, anchor="center")
        self.tree.column("Follow up 1", width=50, anchor="center")
        self.tree.column("Follow up 2", width=50, anchor="center")
        self.tree.column("Follow up 3", width=50, anchor="center")
        self.tree.column("Follow up 4", width=50, anchor="center")
        self.tree.column("Follow up 5", width=50, anchor="center")
        self.tree.column("Follow up 6", width=50, anchor="center")
        self.tree.bind("<Double-1>", on_double_click)
        self.tree.pack(fill="both", expand=True, padx=10, pady=45)

        populate_treeview()
