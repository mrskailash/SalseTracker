import sqlite3
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

from PIL import Image, ImageTk
from tkcalendar import DateEntry

last_filtered_data_window = None


class LeadHeader:
    search_icon = None
    date_filter_icon = None
    refresh_icon = None
    add_icon = None
    ok_icon = None
    close_icon = None
    filter_icon = None

    selected_lead_data = None

    followup1 = None
    followup2 = None
    followup3 = None
    followup4 = None
    followup5 = None
    followup6 = None

    def __init__(self, parent):
        self.parent = parent
        self.open_detail_windows = []

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
                    query = f"SELECT id, date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company FROM leadlist WHERE {selected_text_column} LIKE ?"
                    cursor.execute(query, (f"%{text_input}%",))
                elif selected_dropdown_column != "(none)" and selected_submenu_option:
                    # By Dropdown option
                    # Map the display names to database column names
                    column_mapping = {"Closure": "status", "Source": "source"}
                    mapped_column = column_mapping.get(
                        selected_dropdown_column, selected_dropdown_column
                    )
                    # Construct the SQL query based on the mapped column and submenu option
                    query = f"SELECT id, date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company FROM leadlist WHERE {mapped_column} LIKE ?"
                    cursor.execute(query, (f"%{selected_submenu_option}%",))
                elif len(name) >= 3:
                    # If neither By Text nor By Dropdown is selected, use the name for search
                    query = f"SELECT id, date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company FROM leadlist WHERE fullname LIKE ?"
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
            tree = ttk.Treeview(
                result_window,
                columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                show="headings",
            )

            # Set column names
            tree.heading(1, text="ID")
            tree.heading(2, text="Date")
            tree.heading(3, text="Fullname")
            tree.heading(4, text="Address")
            tree.heading(5, text="Mobile No")
            tree.heading(6, text="Email")
            tree.heading(7, text="Source")
            tree.heading(8, text="Assign To")
            tree.heading(9, text="Status")
            tree.heading(10, text="Ref By")
            tree.heading(11, text="Products")
            tree.heading(12, text="Remark")
            tree.heading(13, text="Company")

            # Set column width
            for i in range(1, 14):
                tree.column(i, width=50, anchor="center")

                # Insert data into the tree
            for row in data:
                tree.insert("", "end", values=row)

            tree.pack(fill="both", expand=True)

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
                query = f"SELECT id, date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company FROM leadlist WHERE date BETWEEN ? AND ?"
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

                    query = f"SELECT id, date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company FROM leadlist WHERE date BETWEEN ? AND ? AND status = ?"
                    cursor.execute(query, (from_date, to_date, status))
                elif filter_option.startswith("By Assign"):
                    # Extract the assignee from the filter option
                    assignee = filter_option.split(": ")[1]

                    query = f"SELECT id, date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company FROM leadlist WHERE date BETWEEN ? AND ? AND assignto = ?"
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

            self.filter_icon = Image.open("asset/filter_icon/filter.png")
            self.filter_icon = self.filter_icon.resize((30, 30))
            self.filter_icon = ImageTk.PhotoImage(self.filter_icon)

            filtermenu_button = tk.Button(
                short_box,
                image=self.filter_icon,
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
            tree = ttk.Treeview(
                filtered_data_window,
                columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                show="headings",
            )

            # Set column names
            tree.heading(1, text="ID")
            tree.heading(2, text="Date")
            tree.heading(3, text="Fullname")
            tree.heading(4, text="Address")
            tree.heading(5, text="Mobile No")
            tree.heading(6, text="Email")
            tree.heading(7, text="Source")
            tree.heading(8, text="Assign To")
            tree.heading(9, text="Status")
            tree.heading(10, text="Ref By")
            tree.heading(11, text="Products")
            tree.heading(12, text="Remark")
            tree.heading(13, text="Company")

            # Set column width
            for i in range(1, 14):
                tree.column(i, width=50, anchor="center")

            # Insert data into the tree
            for row in data:
                tree.insert("", "end", values=row)

            tree.pack(fill="both", expand=True)

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
            detail_window = tk.Toplevel(parent)
            detail_window.geometry(f"500x800+{1000}+{10}")
            detail_window.title("Custom Location Window")
            lead_no, name = selected_lead_data
            detail_window.title(f"Lead Details - Lead No: {lead_no}, Name: {name}")
            followup_menus = []

            def add_followup_context_menu(widget, followup_index):
                followup_menu = tk.Menu(detail_window, tearoff=0)

                # Fetch existing follow-up data from the database
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()
                cursor.execute(
                    f"SELECT followup{followup_index} FROM leadlist WHERE id=?",
                    (lead_no,),
                )
                followup_data = cursor.fetchone()
                conn.close()

                # Check if follow-up data exists and add "Edit" option accordingly
                if followup_data and followup_data[0]:
                    followup_menu.add_command(
                        label="Edit",
                        command=lambda: enable_edit(followup_index),
                    )
                followup_menu.add_command(label="Save", command=save_followup)
                widget.bind(
                    "<Button-3>",
                    lambda event: followup_menu.post(event.x_root, event.y_root),
                )

                followup_menus.append(followup_menu)

            def enable_edit(followup_index):
                followup_widget = [
                    followup1,
                    followup2,
                    followup3,
                    followup4,
                    followup5,
                    followup6,
                ]
                [followup_index - 1]
                followup_widget.config(state=tk.NORMAL)

            def close_detail_window():
                self.open_detail_windows.remove(detail_window)
                detail_window.destroy()

            def save_followup():
                followup_data = [
                    followup1.get("1.0", tk.END).strip(),
                    followup2.get("1.0", tk.END).strip(),
                    followup3.get("1.0", tk.END).strip(),
                    followup4.get("1.0", tk.END).strip(),
                    followup5.get("1.0", tk.END).strip(),
                    followup6.get("1.0", tk.END).strip(),
                ]

                # Save follow-up data to the database
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()
                lead_no, _ = selected_lead_data

                for i, followup in enumerate(followup_data, start=1):
                    column_name = f"followup{i}"
                    cursor.execute(
                        f"UPDATE leadlist SET {column_name} = ? WHERE id = ?",
                        (followup, lead_no),
                    )

                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Follow-up data saved successfully.")

            def fetch_followup():

                # Fetch existing follow-up data from the database
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT followup1, followup2, followup3, followup4, followup5, followup6 FROM leadlist WHERE id=?",
                    (lead_no,),
                )
                followup_data = cursor.fetchone()
                conn.close()

                # Update Text widgets with the fetched follow-up data
                followups = [
                    followup1,
                    followup2,
                    followup3,
                    followup4,
                    followup5,
                    followup6,
                ]
                for i, followup_widget in enumerate(followups):
                    followup_widget.insert(tk.END, followup_data[i])
                    if followup_data[i]:
                        followup_widget.config(state=tk.DISABLED)

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
                command=save_followup,
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

            add_followup_context_menu(followup1, 1)
            add_followup_context_menu(followup2, 2)
            add_followup_context_menu(followup3, 3)
            add_followup_context_menu(followup4, 4)
            add_followup_context_menu(followup5, 5)
            add_followup_context_menu(followup6, 6)
            fetch_followup()

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
        lead_heading_menu6.place(x=160, y=10)

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

        def delete_lead():
            items = self.tree.selection()
            if items:
                result = messagebox.askyesno(
                    "Delete Confirmation",
                    "Are you sure you want to delete the selected row(s)?",
                )
                if result:
                    conn = sqlite3.connect("salestracker.db")
                    cursor = conn.cursor()

                    for item in items:
                        lead_id = self.tree.item(item, "values")[0]

                        # Delete from the database
                        cursor.execute("DELETE FROM leadlist WHERE id=?", (lead_id,))

                        # Delete from the treeview
                        self.tree.delete(item)

                    # Renumber the remaining rows sequentially starting from 1
                    cursor.execute(
                        "UPDATE leadlist SET id = (SELECT ROW_NUMBER() OVER (ORDER BY id) FROM leadlist)"
                    )

                    conn.commit()
                    conn.close()

                    messagebox.showinfo(
                        "Success", "Lead data deleted successfully and IDs renumbered."
                    )

        def get_lead():
            items = self.tree.selection()
            if len(items) == 1:
                selected_lead_data = self.tree.item(items, "values")[:2]
                edit_lead(selected_lead_data)
            elif len(items) > 1:
                messagebox.showwarning(
                    "Multiple Rows Selected", "Select only one row to edit."
                )
            else:
                messagebox.showwarning("No Row Selected", "Select a row to edit.")

        def edit_lead(selected_lead_data):

            lead_no, name = selected_lead_data
            edit_window = tk.Toplevel(parent)
            edit_window.geometry("300x425+1200+90")
            edit_window.title("Edit Lead Window")
            edit_window.title(f"Edit Lead - Lead No: {lead_no}, Name: {name}")

            # Fetch the selected lead data from the database
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company FROM leadlist WHERE id=?",
                (lead_no,),
            )
            lead_data = cursor.fetchone()
            conn.close()
            # Populate the entry widgets with existing data
            entry_widgets = []
            labels = [
                "Date",
                "Fullname",
                "Address",
                "Mobile No",
                "Email",
                "Source",
                "Assign To",
                "Status",
                "Ref By",
                "Products",
                "Remark",
                "Company",
            ]

            for i, value in enumerate(lead_data):
                entry_label = tk.Label(edit_window, text=labels[i])
                entry_label.grid(row=i, column=0, padx=10, pady=5)
                entry_widget = tk.Entry(edit_window, width=30)
                entry_widget.grid(row=i, column=1, padx=10, pady=5)
                entry_widget.insert(
                    0, value
                )  # Populate the entry widget with existing data
                entry_widgets.append(entry_widget)

            def save_changes():
                # Get updated values from entry widgets
                updated_values = [entry.get() for entry in entry_widgets]
                # Update the database with the new values
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE leadlist SET date=?, fullname=?, address=?, mobileno=?, email=?, source=?, assignto=?, status=?, ref_by=?, products=?, remark=?, company=? WHERE id=?",
                    tuple(updated_values + [lead_no]),
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Lead data updated successfully.")
                edit_window.destroy()

            save_button = tk.Button(
                edit_window, text="Save Changes", command=save_changes
            )
            save_button.grid(row=len(lead_data), column=0, columnspan=2, pady=10)

        def open_context_menu(event):
            item = self.tree.selection()
            if item:
                menu.post(event.x_root, event.y_root)

        menu = tk.Menu(self.tree, tearoff=0)
        menu.add_command(label="Add", command=add_followup)
        menu.add_command(label="Edit", command=get_lead)
        menu.add_command(label="Delete", command=delete_lead)
        self.tree.bind("<Button-3>", open_context_menu)  # Right-click event

        # Fetch data and populate the table
        populate_treeview()
