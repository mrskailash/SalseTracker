import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk
from tkcalendar import DateEntry

last_filtered_data_window = None


class Closure:
    filter_icon_copy = None
    filter_icon = None
    search_icon = None
    date_filter_icon = None
    refresh_icon = None

    def __init__(self, parent):
        self.parent = parent

        def search_window():

            def fetch_data():
                # Connect to MySQL server
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()
                # Fetch data from different tables

                cursor.execute("SELECT statustype FROM status")
                status_options = [rows[0] for rows in cursor.fetchall()]

                cursor.execute("SELECT Sourcename FROM source")
                sources = [rows[0] for rows in cursor.fetchall()]

                # Close the database connection

                conn.commit()
                conn.close()

                return status_options, sources

            def update_text_entry(*args):
                selected_option = text_combobox.get()

                if selected_option == "(none)":
                    text_entry.config(state="disabled")
                else:
                    text_entry.config(state="normal")

            def update_sub_dropdown(*args):
                selected_option = dropdown_combobox.get()

                if selected_option == "(none)":
                    dropdown_sub_combobox.set("")
                    dropdown_sub_combobox["values"] = []
                    dropdown_sub_combobox["state"] = "disabled"
                elif selected_option == "Closure":
                    dropdown_sub_combobox["values"] = data[0]
                    dropdown_sub_combobox["state"] = "readonly"
                elif selected_option == "Source":
                    dropdown_sub_combobox["values"] = data[1]
                    dropdown_sub_combobox["state"] = "readonly"

            global search_window
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
                "assignto",
                "email",
                "mobileno",
                "ref_by",
            ]
            text_combobox = ttk.Combobox(search_window, values=by_text_option)
            text_combobox.grid(row=1, column=1, padx=5, pady=10)
            text_combobox.set("(none)")  # Set default value
            text_combobox.bind("<<ComboboxSelected>>", update_text_entry)
            text_entry = tk.Entry(search_window, width=25, state="disabled")
            text_entry.grid(row=1, column=2, padx=5, pady=10)

            dropdown_label = tk.Label(
                search_window, text="By Dropdown", font=("Arial", 12)
            )
            dropdown_label.grid(row=2, column=0, pady=10)

            dropdown_option = ["(none)", "Closure", "Source"]
            dropdown_combobox = ttk.Combobox(search_window, values=dropdown_option)
            dropdown_combobox.grid(row=2, column=1, pady=10)
            dropdown_combobox.set("(none)")  # Set default value
            dropdown_combobox.bind("<<ComboboxSelected>>", update_sub_dropdown)

            data = fetch_data()

            dropdown_sub_combobox = ttk.Combobox(
                search_window, values=data[0], state="disable"
            )
            dropdown_sub_combobox.grid(row=2, column=2, pady=10)

            def search():
                # Get the name input
                name = name_entry.get()

                # Get the selected column for By Text option
                selected_text_column = text_combobox.get()
                # Get the text input for By Text option
                text_input = text_entry.get()

                # Get the selected column for By Dropdown option
                selected_dropdown_column = dropdown_combobox.get()
                # Get the selected submenu option for By Dropdown option
                selected_submenu_option = dropdown_sub_combobox.get()

                # Connect to the database
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()

                # Construct the SQL query based on the selected column and input
                if selected_text_column != "(none)" and len(text_input) >= 3:
                    # By Text option
                    query = f"SELECT id, date, fullname, address, email, status FROM leadlist WHERE {selected_text_column} LIKE ?"
                    cursor.execute(query, (f"%{text_input}%",))
                elif selected_dropdown_column != "(none)" and selected_submenu_option:
                    # By Dropdown option
                    # Map the display names to database column names
                    column_mapping = {"Closure": "status", "Source": "source"}
                    mapped_column = column_mapping.get(
                        selected_dropdown_column, selected_dropdown_column
                    )
                    # Construct the SQL query based on the mapped column and submenu option
                    query = f"SELECT id, date, fullname, address, email, status FROM leadlist WHERE {mapped_column} LIKE ?"
                    cursor.execute(query, (f"%{selected_submenu_option}%",))
                elif len(name) >= 3:
                    # If neither By Text nor By Dropdown is selected, use the name for search
                    query = f"SELECT id, date, fullname, address, email, status FROM leadlist WHERE fullname LIKE ?"
                    cursor.execute(query, (f"%{name}%",))
                else:
                    # No valid input, do nothing
                    conn.close()
                    return

                result = cursor.fetchall()

                # Close the database connection
                conn.close()

                # Display the results in a new window
                show_results(result)
                search_window.destroy()

            search_btn = tk.Button(
                search_window, text="Search", font=("Arial", 12), command=search
            )
            search_btn.place(x=365, y=135)

        def show_results(data):
            # Create a new window
            result_window = tk.Toplevel(parent)
            result_window.title("Search Results")
            result_window.geometry("1000x400+495+80")

            # Create a Treeview to display the results
            self.tree = ttk.Treeview(
                result_window,
                columns=(1, 2, 3, 4, 5, 6),
                show="headings",
            )

            # Set column names
            self.tree.heading(1, text="Lead No")
            self.tree.heading(2, text="Date")
            self.tree.heading(3, text="Fullname")
            self.tree.heading(4, text="Address")
            self.tree.heading(5, text="Email")
            self.tree.heading(6, text="Status")

            # Set column width
            for i in range(1, 6):
                self.tree.column(i, width=50, anchor="center")

                # Insert data into the tree
            for row in data:
                self.tree.insert("", "end", values=row)

            self.tree.pack(fill="both", expand=True)

        def destroy_previous_window():
            global last_filtered_data_window
            if last_filtered_data_window:
                last_filtered_data_window.destroy()

        def show_date_window():
            global date_window
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

            def search_data():
                # Get the selected dates
                global temp_from_date, temp_to_date

                from_date = from_date_entry.get_date()
                to_date = to_date_entry.get_date()

                # Fetch data from the database based on the converted date range
                conn = sqlite3.connect(
                    "salestracker.db"
                )  # Change this to your database file
                cursor = conn.cursor()

                # Modify the SQL query to fit your table structure
                query = f"SELECT id, date, fullname, address, email, status FROM leadlist WHERE date BETWEEN ? AND ?"
                cursor.execute(query, (from_date, to_date))

                data = cursor.fetchall()

                conn.close()

                # Open the new window to display the filtered data
                display_filtered_data(data)

                temp_from_date = from_date
                temp_to_date = to_date

            search_btn = tk.Button(
                date_window, text="Search", font=("Arial", 12), command=search_data
            )
            search_btn.place(x=210, y=50)

        def display_filtered_data(data):
            global last_filtered_data_window
            destroy_previous_window()
            date_window.destroy()

            def show_menu(filtermenu, button):

                filtermenu.post(
                    button.winfo_rootx(), button.winfo_rooty() + button.winfo_height()
                )

            def sort_data(column, data, descending):
                # Sort the data based on the selected column
                global last_filtered_data_window
                destroy_previous_window()
                sorted_data = sorted(
                    data, key=lambda x: x[column - 1], reverse=descending
                )
                # Display the sorted data in the filtered_data_window
                display_filtered_data(sorted_data)

            def fetch_filter_data(from_date, to_date, filter_option):

                global last_filtered_data_window
                destroy_previous_window()
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()

                # Modify the SQL query based on the filter option
                if filter_option.startswith("By Status"):
                    # Extract the status from the filter option
                    status = filter_option.split(": ")[1]

                    query = f"SELECT id, date, fullname, address, email, status FROM leadlist WHERE date BETWEEN ? AND ? AND status = ?"
                    cursor.execute(query, (from_date, to_date, status))
                elif filter_option.startswith("By Assign"):
                    # Extract the assignee from the filter option
                    assignee = filter_option.split(": ")[1]

                    query = f"SELECT id, date, fullname, address, email, status FROM leadlist WHERE date BETWEEN ? AND ? AND assignto = ?"
                    cursor.execute(query, (from_date, to_date, assignee))

                data = cursor.fetchall()
                conn.close()

                # Open the new window to display the filtered data
                display_filtered_data(data)

            filtered_data_window = tk.Toplevel(parent)
            filtered_data_window.title("Short Data")
            filtered_data_window.geometry("1000x400+515+50")
            last_filtered_data_window = filtered_data_window

            menu_font = ("Arial", 12)
            short_box = tk.Frame(
                filtered_data_window, height=50, width=1000, bg="white"
            )
            short_box.pack(side=tk.TOP, anchor="nw", fill="y", ipady=5)
            filtermenu = tk.Menu(short_box, tearoff=0, font=menu_font)

            # Add sorting options for ID
            id_menu = tk.Menu(filtermenu, tearoff=0)
            filtermenu.add_cascade(label="By ID", menu=id_menu)
            id_menu.add_command(
                label="Ascending", command=lambda: sort_data(1, data, False)
            )
            id_menu.add_command(
                label="Descending", command=lambda: sort_data(1, data, True)
            )

            connection = sqlite3.connect(
                "salestracker.db"
            )  # Replace with your actual database file
            cursor = connection.cursor()
            cursor.execute("SELECT statustype FROM status")
            status_options = [rows[0] for rows in cursor.fetchall()]
            # Add filtering options for Status
            status_menu = tk.Menu(filtermenu, tearoff=0)
            filtermenu.add_cascade(label="By Status", menu=status_menu)
            for option in status_options:
                status_menu.add_command(
                    label=option,
                    command=lambda opt=option: fetch_filter_data(
                        temp_from_date, temp_to_date, f"By Status: {opt}"
                    ),
                )

            # Fetch options for the "Assign" menu from the database
            cursor.execute("SELECT name FROM user WHERE id >= 2")
            assign_options = [rows[0] for rows in cursor.fetchall()]
            # Add filtering options for Assign
            assign_menu = tk.Menu(filtermenu, tearoff=0)
            filtermenu.add_cascade(label="By Assign", menu=assign_menu)
            for option in assign_options:
                assign_menu.add_command(
                    label=option,
                    command=lambda opt=option: fetch_filter_data(
                        temp_from_date, temp_to_date, f"By Assign: {opt}"
                    ),
                )

            self.filter_icon_copy = Image.open("asset/filter_icon/filtercopy.png")
            self.filter_icon_copy = self.filter_icon_copy.resize((30, 30))
            self.filter_icon_copy = ImageTk.PhotoImage(self.filter_icon_copy)

            filtermenu_button = tk.Button(
                short_box,
                image=self.filter_icon_copy,
                bg="white",
                borderwidth=0,
                padx=10,
                pady=6,
                command=lambda: show_menu(filtermenu, filtermenu_button),
            )
            filtermenu_button.grid(
                row=0,
                column=0,
                padx=15,
            )

            filterlable = tk.Label(
                short_box, text="Filter", bg="white", font=("Arial", 15)
            )
            filterlable.grid(row=1, column=0, padx=15, pady=2)
            self.tree = ttk.Treeview(
                filtered_data_window,
                columns=(1, 2, 3, 4, 5, 6),
                show="headings",
            )

            # Set column names
            self.tree.heading(1, text="Lead No")
            self.tree.heading(2, text="Date")
            self.tree.heading(3, text="Fullname")
            self.tree.heading(4, text="Address")
            self.tree.heading(5, text="Email")
            self.tree.heading(6, text="Status")

            # Set column width
            for i in range(1, 6):
                self.tree.column(i, width=50, anchor="center")

            # Insert data into the tree
            for row in data:
                self.tree.insert("", "end", values=row)

            self.tree.pack(fill="both", expand=True)

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
