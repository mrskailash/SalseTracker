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
    save_icon = None
    cancle_icon = None

    def __init__(self, parent):
        self.parent = parent
        self.opened_windows = []

        def followup_data():
            selected_item = self.tree.selection()
            if selected_item:
                selected_data = self.tree.item(selected_item, "values")
                followup_window(selected_data)
            else:
                tk.messagebox.showinfo("Info", "Please select a row.")

        def followup_window(selected_data):

            followup_window = tk.Toplevel(self.parent)
            followup_window.title("Search Window")
            followup_window.configure(bg="white")
            followup_window.geometry("600x500+900+100")
            followup_window.resizable(False, False)

            self.opened_windows.append(followup_window)

            def on_window_close(self, window):
                # Remove the closed window from the list
                self.opened_windows.remove(window)

            def show_box(box_number, selected_data):
                # Hide all containers
                followup_container.place_forget()
                history_container.place_forget()

                followupbtn.config(bg="lightgray" if box_number != 1 else "#0086B3")
                historybtn.config(bg="lightgray" if box_number != 2 else "#0086B3")

                # Display the selected container
                if box_number == 1:
                    followup_container.place(x=12, y=67, height=433, width=588)
                elif box_number == 2:
                    history_container.place(x=12, y=67, height=433, width=588)
                    followuphis(selected_data)

            self.save_icon = Image.open("asset/check_icon/check.png")
            self.save_icon = self.save_icon.resize((25, 25))
            self.save_icon = ImageTk.PhotoImage(self.save_icon)

            def save_followup():
                # Get the follow-up data from the text boxes
                followup_data = (
                    folluptext1.get("1.0", tk.END).strip(),
                    folluptext2.get("1.0", tk.END).strip(),
                    folluptext3.get("1.0", tk.END).strip(),
                    folluptext4.get("1.0", tk.END).strip(),
                    folluptext5.get("1.0", tk.END).strip(),
                    folluptext6.get("1.0", tk.END).strip(),
                )

                # Update or insert the follow-up data into the database
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM leadlist WHERE id=?", (selected_data[0],))
                existing_data = cursor.fetchone()

                if existing_data:
                    # Update existing record
                    cursor.execute(
                        "UPDATE leadlist SET followup1=?, followup2=?, followup3=?, followup4=?, followup5=?, followup6=? WHERE id=?",
                        followup_data + (selected_data[0],),
                    )
                else:
                    # Insert new record
                    cursor.execute(
                        "INSERT INTO leadlist (id, followup1, followup2, followup3, followup4, followup5, followup6) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (selected_data[0],) + followup_data,
                    )

                conn.commit()
                conn.close()

                tk.messagebox.showinfo("Success", "Follow-up data saved successfully!")

            save_button = tk.Button(
                followup_window,
                image=self.save_icon,
                borderwidth=0,
                highlightthickness=0,
                bg="white",
                height=25,
                width=25,
                command=save_followup,
            )
            save_button.place(y=15, x=20)
            save_text = tk.Label(
                followup_window,
                text="Save",
                fg="black",
                bg="white",
                font=("Arial", 12),
            )
            save_text.place(y=40, x=10)

            self.cancle_icon = Image.open("asset/check_icon/close.png")
            self.cancle_icon = self.cancle_icon.resize((25, 25))
            self.cancle_icon = ImageTk.PhotoImage(self.cancle_icon)

            cancle_button = tk.Button(
                followup_window,
                image=self.cancle_icon,
                borderwidth=0,
                highlightthickness=0,
                bg="white",
                height=25,
                width=25,
                command=on_window_close,
            )
            cancle_button.place(y=15, x=560)

            cancle_text = tk.Label(
                followup_window,
                text="Cancle",
                fg="black",
                bg="white",
                font=("Arial", 12),
            )
            cancle_text.place(y=40, x=545)

            separator = tk.Frame(followup_window, height=3, width=600, bg="black")
            separator.place(y=65)

            data_container = tk.Frame(followup_window, height=450, width=600)
            data_container.place(y=70)
            clicked_data_lable_name = tk.Label(
                data_container, text=selected_data[2], font=("arial", 15)
            )
            clicked_data_lable_name.place(x=10, y=10)

            data_btn_clr = "#0086B3"
            followupbtn = tk.Button(
                data_container,
                text="Follow Up",
                bg=data_btn_clr,
                command=lambda: show_box(1),
            )
            followupbtn.place(y=40, x=10)

            def followuphis(selected_data):
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT followup1, followup2, followup3, followup4, followup5, followup6 FROM leadlist WHERE id=?",
                    (selected_data[0],),
                )
                followup_data = cursor.fetchone()
                conn.close()

                # Display follow-up data in the text boxes
                folluptext1.delete("1.0", tk.END)
                folluptext2.delete("1.0", tk.END)
                folluptext3.delete("1.0", tk.END)
                folluptext4.delete("1.0", tk.END)
                folluptext5.delete("1.0", tk.END)
                folluptext6.delete("1.0", tk.END)

                folluptext1.insert(tk.END, followup_data[0])  # followup1
                folluptext2.insert(tk.END, followup_data[1])  # followup2
                folluptext3.insert(tk.END, followup_data[2])  # followup3
                folluptext4.insert(tk.END, followup_data[3])  # followup4
                folluptext5.insert(tk.END, followup_data[4])  # followup5
                folluptext6.insert(tk.END, followup_data[5])  # followup6

            historybtn = tk.Button(
                data_container,
                text="history",
                command=lambda: show_box(2, selected_data),
            )
            historybtn.place(y=40, x=80)

            followup_container = tk.Frame(
                data_container,
                height=433,
                width=588,
                bg="lightgray",
                borderwidth=2,
                relief=tk.GROOVE,
                highlightthickness=-0,
            )
            followup_container.place(x=12, y=67)

            date_lable = tk.Label(
                followup_container,
                text="Date",
            )
            date_lable.place(x=5, y=5)

            date_entry = DateEntry(followup_container)
            date_entry.place(x=75, y=5)

            followups_lable = tk.Label(
                followup_container,
                text="Follow Ups",
            )
            followups_lable.place(x=5, y=35)

            def update_notes_entry(event):
                selected_followup = followups_entry.get()

                # Retrieve the corresponding follow-up text data
                followup_text_data = {
                    "Follow Up 1": folluptext1.get("1.0", tk.END).strip(),
                    "Follow Up 2": folluptext2.get("1.0", tk.END).strip(),
                    "Follow Up 3": folluptext3.get("1.0", tk.END).strip(),
                    "Follow Up 4": folluptext4.get("1.0", tk.END).strip(),
                    "Follow Up 5": folluptext5.get("1.0", tk.END).strip(),
                    "Follow Up 6": folluptext6.get("1.0", tk.END).strip(),
                }

                # Set the notes_entry based on the selected follow-up
                notes_entry.delete("1.0", tk.END)
                notes_entry.insert(tk.END, followup_text_data[selected_followup])

            followup_options = [
                "Follow Up 1",
                "Follow Up 2",
                "Follow Up 3",
                "Follow Up 4",
                "Follow Up 5",
                "Follow Up 6",
            ]
            followups_entry = ttk.Combobox(followup_container)
            followups_entry["values"] = followup_options
            followups_entry.place(x=75, y=35)
            followups_entry.bind("<<ComboboxSelected>>", update_notes_entry)
            notes_lable = tk.Label(
                followup_container,
                text="Notes",
            )
            notes_lable.place(x=5, y=65)

            notes_entry = tk.Text(followup_container, height=10, width=55)
            notes_entry.place(x=75, y=65)

            history_container = tk.Frame(
                data_container,
                height=433,
                width=588,
                bg="gray",
                borderwidth=2,
                relief=tk.GROOVE,
                highlightthickness=-0,
            )
            history_container.place(x=12, y=67)

            followupbox1 = tk.Frame(history_container, height=355, width=290)
            followupbox1.place(x=0, y=0)

            follup1 = tk.Label(followupbox1, text="follow up1")
            follup1.place(x=0, y=0)

            folluptext1 = tk.Text(followupbox1, height=5, width=35)
            folluptext1.place(y=20)

            follup2 = tk.Label(followupbox1, text="follow up2")
            follup2.place(x=0, y=110)

            folluptext2 = tk.Text(followupbox1, height=5, width=35)
            folluptext2.place(y=130)

            follup3 = tk.Label(followupbox1, text="follow up3")
            follup3.place(x=0, y=220)

            folluptext3 = tk.Text(followupbox1, height=5, width=35)
            folluptext3.place(y=240)

            followupbox2 = tk.Frame(history_container, height=355, width=290)
            followupbox2.place(x=294, y=0)

            follup4 = tk.Label(followupbox2, text="follow up4")
            follup4.place(x=0, y=0)

            folluptext4 = tk.Text(followupbox2, height=5, width=35)
            folluptext4.place(y=20)

            follup5 = tk.Label(followupbox2, text="follow up5")
            follup5.place(x=0, y=110)

            folluptext5 = tk.Text(followupbox2, height=5, width=35)
            folluptext5.place(y=130)

            follup6 = tk.Label(followupbox2, text="follow up6")
            follup6.place(x=0, y=220)

            folluptext6 = tk.Text(followupbox2, height=5, width=35)
            folluptext6.place(y=240)

            history_container.place_forget()

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
            # Connect to SQLite database
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Fetch data from the leadlist table, including follow-up columns 1 to 6
            cursor.execute(
                "SELECT id, date, fullname, address, followup1, followup2, followup3, followup4, followup5, followup6 FROM leadlist"
            )

            lead_data = cursor.fetchall()

            # Close the database connection
            conn.close()

            return lead_data

        def populate_treeview():
            # Clear existing items in the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            lead_data = fetch_lead_data()

            for lead_row in lead_data:
                (
                    lead_no,
                    date,
                    name,
                    address,
                    follow_up_1,
                    follow_up_2,
                    follow_up_3,
                    follow_up_4,
                    follow_up_5,
                    follow_up_6,
                ) = lead_row

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        lead_no,
                        date,
                        name,
                        address,
                        follow_up_1,
                        follow_up_2,
                        follow_up_3,
                        follow_up_4,
                        follow_up_5,
                        follow_up_6,
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

        lead_heading_menu4 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu4.place(x=80, y=10)

        lead_heading_menu5 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu5.place(x=150, y=10)

        lead_heading_menu6 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu6.place(x=220, y=10)

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
            command=followup_data,
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

        def open_context_menu(event):
            item = self.tree.selection()
            if item:
                menu.post(event.x_root, event.y_root)

        menu = tk.Menu(self.tree, tearoff=0)
        menu.add_command(label="follow up", command=followup_data)
        menu.add_command(
            label="view",
        )
        self.tree.bind("<Button-3>", open_context_menu)
        populate_treeview()
