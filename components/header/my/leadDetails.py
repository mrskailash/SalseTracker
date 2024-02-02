import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# import mysql.connector
from PIL import Image, ImageTk
from tkcalendar import DateEntry


class LeadDetails:
    delete_icon = None
    save_icon = None
    add_icon = None
    fetched_id = 0

    def __init__(self, parent):
        self.parent = parent

        def save_data(
            formatted_date,
            name_entry,
            address_entry,
            telephone_entry,
            email_entry,
            source_entry,
            assignto_entry,
            status_entry,
            ref_entry,
            product_entry,
            remark_entry,
            company_entry,
        ):
            global fetched_id
            # Connect to MySQL server
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Insert data into the database using the fetched ID and formatted date
            cursor.execute(
                "INSERT INTO leadlist (id, date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    fetched_id,
                    formatted_date,
                    name_entry,
                    address_entry,
                    telephone_entry,
                    email_entry,
                    source_entry,
                    assignto_entry,
                    status_entry,
                    ref_entry,
                    product_entry,
                    remark_entry,
                    company_entry,
                ),
            )

            # Commit changes and close the database connection
            conn.commit()
            conn.close()
            # Show a message box indicating successful data storage
            tk.messagebox.showinfo(
                "Success", "Data stored successfully for ID: {}".format(fetched_id)
            )

            # Reset fetched_id for the next entry
            fetched_id = 0
            clear_input_fields(
                self.date_entry,
                self.name_entry,
                self.address_entry,
                self.telephone_entry,
                self.email_entry,
                self.source_entry,
                self.assignto_entry,
                self.status_entry,
                self.ref_entry,
                self.product_entry,
                self.remark_entry,
                self.company_entry,
            )

        def clear_input_fields(
            date_entry,
            name_entry,
            address_entry,
            email_entry,
            source_entry,
            assignto_entry,
            status_entry,
            ref_entry,
            product_entry,
            remark_entry,
            company_entry,
        ):
            date_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            address_entry.delete("1.0", tk.END)
            email_entry.delete(0, tk.END)
            source_entry.delete(0, tk.END)
            assignto_entry.delete(0, tk.END)
            status_entry.delete(0, tk.END)
            ref_entry.delete(0, tk.END)
            product_entry.delete(0, tk.END)
            remark_entry.delete(0, tk.END)
            company_entry.delete(0, tk.END)

        def clear_entries():
            global fetched_id
            fetched_id = 0  # Reset fetched_id before clearing the fields
            self.name_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.telephone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.source_entry.delete(0, tk.END)
            self.assignto_entry.delete(0, tk.END)
            self.status_entry.delete(0, tk.END)
            self.ref_entry.delete(0, tk.END)
            self.product_entry.delete(0, tk.END)
            self.remark_entry.delete(0, tk.END)
            self.company_entry.delete(0, tk.END)

        def show_box(box_number):
            # Hide all containers
            details_container.place_forget()
            # product_container.place_forget()
            note_container.place_forget()

            details_btn.config(bg="lightgray" if box_number != 1 else "#0086B3")
            # product_btn.config(bg="lightgray" if box_number != 2 else "#0086B3")
            notes_btn.config(bg="lightgray" if box_number != 3 else "#0086B3")
            # Display the selected container
            if box_number == 1:
                details_container.place(x=0, y=40, height=600, width=1500)
            # elif box_number == 2:
            #     product_container.place(x=0, y=40, height=600, width=1500)
            elif box_number == 3:
                note_container.place(x=0, y=40, height=600, width=1500)

        def fetch_data(leadno_entry):
            # Connect to MySQL server
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()
            # Fetch data from different tables
            cursor.execute("SELECT Sourcename FROM source")
            sources = [rows[0] for rows in cursor.fetchall()]

            cursor.execute("SELECT name FROM user WHERE id >= 2")
            assign_names = [rows[0] for rows in cursor.fetchall()]

            cursor.execute("SELECT statustype FROM status")
            status_options = [rows[0] for rows in cursor.fetchall()]

            cursor.execute("SELECT productname FROM products")
            product_names = [rows[0] for rows in cursor.fetchall()]

            cursor.execute("SELECT MAX(id) FROM leadlist")
            max_id = cursor.fetchone()[0]
            fetched_id = max_id + 1 if max_id else 1
            # Close the database connection
            conn.commit()
            conn.close()

            leadno_entry.delete(0, tk.END)
            leadno_entry.insert(0, str(fetched_id))

            return sources, assign_names, status_options, product_names

        lead_heading = tk.Frame(parent, bg="white", width=1300, height=55)
        lead_heading.pack(side=tk.TOP, anchor=tk.NW)

        sepretor = tk.Frame(parent, bg="black", height=2, width=1510)
        sepretor.pack(pady=5)

        lead_heading_menu1 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu1.place(x=12, y=8)

        lead_heading_menu2 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu2.place(x=80, y=8)

        lead_heading_menu3 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu3.place(x=150, y=8)

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
            command=clear_entries,
        )
        add_button.grid(row=0, column=1, padx=5)

        add_text = tk.Label(
            lead_heading_menu1, text="new", fg="black", bg="white", font=("Arial", 12)
        )
        add_text.grid(row=1, column=1)

        self.save_icon = Image.open("asset/Lead_icon/diskette.png")
        self.save_icon = self.save_icon.resize((25, 25))
        self.save_icon = ImageTk.PhotoImage(self.save_icon)

        def save_data_wrapper():
            # Format the date using strftime
            formatted_date = self.date_entry.get_date().strftime("%Y-%m-%d")

            # Pass the formatted date and widget values to the save_data function
            save_data(
                formatted_date,
                self.name_entry.get(),
                self.address_entry.get("1.0", "end-1c"),
                self.telephone_entry.get(),
                self.email_entry.get(),
                self.source_entry.get(),
                self.assignto_entry.get(),
                self.status_entry.get(),
                self.ref_entry.get(),
                self.product_entry.get(),
                self.remark_entry.get("1.0", "end-1c"),
                self.company_entry.get(),
            )

        save_button = tk.Button(
            lead_heading_menu2,
            image=self.save_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            command=save_data_wrapper,
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

        lead_entry = tk.Frame(
            self.parent,
            borderwidth=0,
            relief=tk.GROOVE,
            highlightthickness=0,
            highlightbackground="white",
            highlightcolor="white",
            bg="white",
            height=500,
            width=1500,
        )
        lead_entry.pack(fill=tk.BOTH, expand=True, pady=5, padx=15)

        add_lead_btn_row = tk.Frame(lead_entry, height=50, width=50, bg="white")
        add_lead_btn_row.place(x=10, y=10)

        details_btn_clr = "#0086B3"
        details_btn = tk.Button(
            add_lead_btn_row,
            text="Details",
            bg=details_btn_clr,
            font=("Arial", 12),
            height=1,
            width=12,
            command=lambda: show_box(1),
        )
        details_btn.grid(row=0, column=1, padx=5)

        notes_btn = tk.Button(
            add_lead_btn_row,
            text="Notes",
            font=("Arial", 12),
            height=1,
            width=12,
            command=lambda: show_box(3),
        )
        notes_btn.grid(row=0, column=3, padx=2)

        details_container = tk.Frame(
            lead_entry,
            height=650,
            width=1500,
            bg="white",
            borderwidth=0,
            relief=tk.GROOVE,
            highlightthickness=-0,
        )
        details_container.place(x=0, y=40)

        info_container = tk.Frame(
            details_container,
            height=650,
            width=1500,
            bg="white",
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=-0,
        )
        info_container.pack(fill=tk.BOTH, expand=True)
        info_container.grid_propagate(False)

        leadNo_lable = tk.Label(
            info_container,
            text="Lead No",
            bg="white",
            fg="black",
            font=("Arial", 12),
        )
        leadNo_lable.place(x=10, y=10)

        leadNo_entry = tk.Entry(
            info_container, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE
        )
        leadNo_entry.place(x=120, y=12)

        fetch_data(leadNo_entry)
        leadNo_entry.bind("<KeyRelease>", lambda event: fetch_data(leadNo_entry))
        date_lable = tk.Label(
            info_container, text="Date", bg="white", fg="black", font=("Arial", 12)
        )
        date_lable.place(x=280, y=10)

        self.date_entry = DateEntry(
            info_container,
            selectedmode="day",
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
        )
        self.date_entry.place(x=330, y=12)

        name_lable = tk.Label(
            info_container, text="Full Name", bg="white", fg="black", font=("Arial", 13)
        )
        name_lable.place(x=12, y=50)

        self.name_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.name_entry.place(x=120, y=50)

        def on_text_focus_in(event):
            if self.address_entry.get("1.0", "end-1c") == address_placeholder:
                self.address_entry.delete("1.0", tk.END)
                self.address_entry.config(foreground="black")

        def on_text_focus_out(event):
            if not self.address_entry.get("1.0", "end-1c").strip():
                self.address_entry.insert("1.0", address_placeholder)
                self.address_entry.config(foreground="grey")

        address_lable = tk.Label(
            info_container,
            text="Address",
            bg="white",
            fg="black",
            font=("Arial", 13),
        )
        address_lable.place(x=12, y=90)

        address_placeholder = "Enter city or address"
        self.address_entry = tk.Text(
            info_container,
            width=41,
            height=5,
            wrap=tk.WORD,
            borderwidth=0,
            relief=tk.GROOVE,
            highlightthickness=2,
            highlightbackground="gray",
            highlightcolor="gray",
            bg="white",
        )
        self.address_entry.insert(
            "1.0",
            address_placeholder,
        )
        self.address_entry.place(x=120, y=90)

        self.address_entry.bind("<FocusIn>", on_text_focus_in)
        self.address_entry.bind("<FocusOut>", on_text_focus_out)

        telephone_lable = tk.Label(
            info_container, text="Mobile No", bg="white", fg="black", font=("Arial", 13)
        )
        telephone_lable.place(x=12, y=230)

        self.telephone_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.telephone_entry.place(x=120, y=230)

        email_lable = tk.Label(
            info_container, text="Email", bg="white", fg="black", font=("Arial", 13)
        )
        email_lable.place(x=12, y=270)

        self.email_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.email_entry.place(x=120, y=270)

        data_tuple = fetch_data(leadNo_entry)
        source_lable = tk.Label(
            info_container,
            text="Source ",
            bg="white",
            fg="black",
            font=("Arial", 13),
        )
        source_lable.place(x=12, y=310)

        self.source_entry = ttk.Combobox(
            info_container,
            values=data_tuple[0],
            width=52,
        )
        self.source_entry.place(x=120, y=310)

        assignto_lable = tk.Label(
            info_container,
            text="Assign To",
            bg="white",
            fg="black",
            font=("Arial", 13),
        )
        assignto_lable.place(x=12, y=350)

        self.assignto_entry = ttk.Combobox(
            info_container,
            values=data_tuple[1],
            width=52,
        )
        self.assignto_entry.place(x=120, y=350)

        status_lable = tk.Label(
            info_container,
            text="Status",
            bg="white",
            fg="black",
            font=("Arial", 13),
        )
        status_lable.place(x=12, y=390)

        self.status_entry = ttk.Combobox(
            info_container,
            values=data_tuple[2],
            width=52,
        )
        self.status_entry.place(x=120, y=390)

        ref_lable = tk.Label(
            info_container,
            text="Referance By",
            bg="white",
            fg="black",
            font=("Arial", 13),
        )
        ref_lable.place(x=12, y=430)

        self.ref_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.ref_entry.place(x=120, y=430)

        product_lable = tk.Label(
            info_container,
            text="Products",
            bg="white",
            fg="black",
            font=("Arial", 13),
        )
        product_lable.place(x=12, y=470)

        self.product_entry = ttk.Combobox(
            info_container,
            values=data_tuple[3],
            width=52,
        )
        self.product_entry.place(x=120, y=470)

        remark_lable = tk.Label(
            info_container,
            text="Remark",
            bg="white",
            fg="black",
            font=("Arial", 13),
        )
        remark_lable.place(x=12, y=510)

        self.remark_entry = tk.Text(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            height=3,
            width=42,
        )
        self.remark_entry.place(x=120, y=510)

        company_lable = tk.Label(
            info_container,
            text="company",
            bg="white",
            fg="black",
            font=("Arial", 13),
        )
        company_lable.place(x=12, y=580)

        self.company_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.company_entry.place(x=120, y=580)

        note_container = tk.Frame(
            lead_entry,
            height=600,
            width=1500,
            bg="white",
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=-0,
        )
        note_container.place(x=0, y=40)

        notes_text = tk.Label(note_container, text="Notes", bg="lightgray")
        notes_text.place(x=10, y=10)
        notes_entry = tk.Text(
            note_container,
            width=40,
            height=32,
            wrap=tk.WORD,
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=0,
            highlightbackground="gray",
            highlightcolor="gray",
            bg="white",
        )
        notes_entry.pack(fill=tk.X, expand=True)
        note_container.place_forget()
