import tkinter as tk
from tkinter import ttk

import mysql.connector
from PIL import Image, ImageTk
from tkcalendar import DateEntry


class leadentry:
    fetched_id = 0

    def __init__(self, parent):
        self.parent = parent

        # def clear_entries():
        #     name_entry.delete(0, tk.END)
        #     sales_person_entry.delete(0, tk.END)
        #     address_entry.delete("1.0", tk.END)
        #     email_entry.delete(0, tk.END)
        #     source_entry.delete(0, tk.END)
        #     assignto_entry.delete(0, tk.END)
        #     status_entry.delete(0, tk.END)

        def show_box(box_number):
            # Hide all containers
            details_container.place_forget()
            product_container.place_forget()
            note_container.place_forget()

            details_btn.config(bg="lightgray" if box_number != 1 else "#0086B3")
            product_btn.config(bg="lightgray" if box_number != 2 else "#0086B3")
            notes_btn.config(bg="lightgray" if box_number != 3 else "#0086B3")
            # Display the selected container
            if box_number == 1:
                details_container.place(x=0, y=40, height=475, width=1528)
            elif box_number == 2:
                product_container.place(x=0, y=40, height=475, width=1528)
            elif box_number == 3:
                note_container.place(x=0, y=40, height=475, width=1528)

        def fetch_next_id(leadNo_entry):
            global fetched_id
            # Connect to MySQL server
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="salestracker"
            )

            # Create a cursor object
            cursor= db_connection.cursor()

            # Fetch the next available ID from the database
            cursor.execute("SELECT MAX(id) FROM leadlist")
            max_id = cursor.fetchone()[0]
            fetched_id = max_id + 1 if max_id else 1

            # Close the database connection
            cursor.close()
            db_connection.close()

            # Update leadNo_entry with the fetched ID
            leadNo_entry.delete(0, tk.END)
            leadNo_entry.insert(0, str(fetched_id))

        def show_product_menu(menu, button, x_offset=1275, y_offset=40):
            menu.post(
                button.winfo_rootx() + x_offset,
                button.winfo_rooty() + button.winfo_height() + y_offset,
            )

        def center_window(window, width, height):
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()

            x_coordinate = int((screen_width - width) / 2)
            y_coordinate = int((screen_height - height) / 2)

            window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        def open_add_product():
            def fetch_product_names():
                # Connect to MySQL server
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",  # Provide your MySQL password if set
                    database="salestracker"
                )

            # Create a cursor object
                cursor = connection.cursor()

            # Fetch product names from the database
                cursor.execute("SELECT productname FROM products")  # Replace 'your_table_name' with the actual table name
                product_names = [row[0] for row in cursor.fetchall()]

            # Close the database connection
                cursor.close()
                connection.close()

                return product_names

            product_window = tk.Toplevel(parent)
            product_window.title("Small Window")
            product_window.geometry("50x50")
            center_window(product_window, 487, 348)
            product_window.resizable(False, False)
            product_window.title("product Details")

            product_window.grab_set()

            check_img_path = "check.png"
            check_icon = Image.open(check_img_path)
            check_icon = check_icon.resize((30, 30))
            check_icon_photo = ImageTk.PhotoImage(check_icon)

            btn_bg = "#f0f0f0"
            ok_btn = tk.Button(
                product_window,
                image=check_icon_photo,
                bg=btn_bg,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
            )
            ok_btn.place(x=15, y=8)

            ok_lable = tk.Label(product_window, text="ok")
            ok_lable.place(x=15, y=35)

            separator1 = tk.Frame(product_window, height=2, width=490, bg="black")
            separator1.place(y=55)

            check_img_path = "check.png"
            check_icon = Image.open(check_img_path)
            check_icon = check_icon.resize((30, 30))
            check_icon_photo = ImageTk.PhotoImage(check_icon)

            btn_bg = "#f0f0f0"
            ok_btn = tk.Button(
                product_window,
                image=check_icon_photo,
                bg=btn_bg,
                borderwidth=0,
                highlightthickness=0,
                relief="flat",
            )
            ok_btn.place(x=15, y=8)

            ok_label = tk.Label(product_window, text="ok")
            ok_label.place(x=15, y=35)

            separator1 = tk.Frame(product_window, height=2, width=490, bg="black")
            separator1.place(y=55)

            product_label = tk.Label(product_window, text="Product*")
            product_label.place(x=15, y=80)

            # product_options = fetch_product_names()
            product_entry = ttk.Combobox(product_window, width=40)
            # values=product_options
            product_entry.pack(padx=15, pady=80)
            # product_entry.set(product_options[0])  # Set the default value

            quantity_label = tk.Label(product_window, text="Qty*")
            quantity_label.place(x=15, y=120)

            quantity_entry = tk.Entry(product_window, width=53)
            quantity_entry.place(x=112, y=120)

            rate_label = tk.Label(product_window, text="Rate*")
            rate_label.place(x=15, y=160)

            rate_entry = tk.Entry(product_window, width=53)
            rate_entry.place(x=112, y=160)

            amount_label = tk.Label(product_window, text="Amount")
            amount_label.place(x=15, y=200)

            amount_entry = tk.Entry(product_window, width=53)
            amount_entry.place(x=112, y=200)

            description_label = tk.Label(product_window, text="description")
            description_label.place(x=15, y=240)

            description_entry = tk.Text(
                product_window, width=40, height=5, wrap=tk.WORD
            )
            description_entry.place(x=112, y=240)

            product_window.wait_window()

        lead_entry = tk.Frame(
            self.parent,
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=0,
            highlightbackground="gray",
            highlightcolor="gray",
            bg="lightgray",
            height=500,
            width=1500,
        )
        lead_entry.pack(fill=tk.BOTH, expand=True, pady=5)

        add_lead_btn_row = tk.Frame(lead_entry, height=50, width=50, bg="lightgray")
        add_lead_btn_row.place(x=10, y=10)

        details_btn_clr = "#0086B3"
        details_btn = tk.Button(
            add_lead_btn_row,
            text="Details",
            bg=details_btn_clr,
            font=("Arial", 12),
            height=1,
            width=12,
            # command=lambda: show_box(1),
        )
        details_btn.grid(row=0, column=1, padx=5)

        product_btn = tk.Button(
            add_lead_btn_row,
            text="Products",
            font=("Arial", 12),
            height=1,
            width=12,
            # command=lambda: show_box(2),
        )
        product_btn.grid(row=0, column=2, padx=5)

        notes_btn = tk.Button(
            add_lead_btn_row,
            text="Notes",
            font=("Arial", 12),
            height=1,
            width=12,
            # command=lambda: show_box(3),
        )
        notes_btn.grid(row=0, column=3, padx=2)

        details_container = tk.Frame(
            lead_entry,
            height=475,
            width=1528,
            bg="lightgray",
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=-0,
        )
        details_container.place(x=0, y=40)

        info_container = tk.Frame(
            details_container,
            height=475,
            width=1528,
            bg="lightgray",
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=-0,
        )
        info_container.pack(fill=tk.BOTH, expand=True)
        info_container.grid_propagate(False)

        leadNo_lable = tk.Label(
            info_container,
            text="Lead No",
            bg="lightgray",
            fg="black",
            font=("Arial", 12),
        )
        leadNo_lable.place(x=10, y=10)

        leadNo_entry = tk.Entry(
            info_container, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE
        )
        leadNo_entry.place(x=120, y=12)

        # fetch_next_id(leadNo_entry)
        # leadNo_entry.bind("<KeyRelease>", lambda event: fetch_next_id(leadNo_entry))
        date_lable = tk.Label(
            info_container, text="Date", bg="lightgray", fg="black", font=("Arial", 12)
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
            info_container, text="Name", bg="lightgray", fg="black", font=("Arial", 13)
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

        sales_person_lable = tk.Label(
            info_container,
            text="Sales Person",
            bg="lightgray",
            fg="black",
            font=("Arial", 13),
        )
        sales_person_lable.place(x=12, y=90)

        self.sales_person_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.sales_person_entry.place(x=120, y=90)

        address_lable = tk.Label(
            info_container,
            text="Address",
            bg="lightgray",
            fg="black",
            font=("Arial", 13),
        )
        address_lable.place(x=12, y=130)

        self.address_entry = tk.Text(info_container, width=40, height=5, wrap=tk.WORD)
        self.address_entry.place(x=120, y=130)

        email_lable = tk.Label(
            info_container, text="Email", bg="lightgray", fg="black", font=("Arial", 13)
        )
        email_lable.place(x=12, y=230)

        self.email_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.email_entry.place(x=120, y=230)

        source_lable = tk.Label(
            info_container,
            text="Source ",
            bg="lightgray",
            fg="black",
            font=("Arial", 13),
        )
        source_lable.place(x=12, y=270)

        self.source_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.source_entry.place(x=120, y=270)

        assignto_lable = tk.Label(
            info_container,
            text="Assign To",
            bg="lightgray",
            fg="black",
            font=("Arial", 13),
        )
        assignto_lable.place(x=12, y=310)

        self.assignto_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.assignto_entry.place(x=120, y=310)

        status_lable = tk.Label(
            info_container,
            text="Status",
            bg="lightgray",
            fg="black",
            font=("Arial", 13),
        )
        status_lable.place(x=12, y=350)

        self.status_entry = tk.Entry(
            info_container,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=55,
        )
        self.status_entry.place(x=120, y=350)

        product_container = tk.Frame(
            lead_entry,
            height=475,
            width=1528,
            bg="lightgray",
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=-0,
        )
        product_container.place(x=0, y=40)
        product_container.place_forget()

        product_details_text = tk.Label(
            product_container, text="Product Details", font=("Arial,8")
        )
        product_details_text.place(x=15, y=15)

        self.tree = ttk.Treeview(
            product_container,
            columns=("Product", "Quantity", "Rate", "Amount", "Description"),
            show="headings",
        )

        self.tree.heading("Product", text="Product")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Rate", text="Rate")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Description", text="Description")

        # Configure style for the treeview
        style = ttk.Style()
        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold"),
            background="#CCCCCC",
            foreground="black",
        )
        style.configure(
            "Treeview",
            font=("Arial", 9),
            rowheight=25,
            highlightthickness=0,
            bd=0,
            background="white",
            fieldbackground="white",
        )
        style.map("Treeview", background=[("selected", "#3b3a3a")])

        # Add grid lines for the data area
        style.layout(
            "Treeview",
            [
                (
                    "Treeview.treearea",
                    {
                        "sticky": "nswe",
                        "children": [
                            (
                                "Treeitem.row",
                                {
                                    "sticky": "nswe",
                                    "children": [("Treeitem.cell", {"sticky": "nswe"})],
                                },
                            )
                        ],
                    },
                )
            ],
        )

        data = [
            ("Product A", 10, 5.0, 50.0, "Description 1"),
        ]

        for row in data:
            self.tree.insert("", "end", values=row)

        # Create vertical scrollbar
        yscrollbar = tk.Scrollbar(parent, orient="vertical", command=self.tree.yview)
        yscrollbar.pack(side="right", fill="y")

        # Create horizontal scrollbar
        xscrollbar = tk.Scrollbar(parent, orient="horizontal", command=self.tree.xview)
        xscrollbar.pack(side="bottom", fill="x")

        # Connect scrollbars to the treeview
        self.tree.configure(
            yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set
        )

        # Pack the treeview widget
        self.tree.place(x=15, y=50)

        menu_font = ("Arial", 12)
        product_menu = tk.Menu(product_container, tearoff=0, font=menu_font)
        product_menu.add_command(label="Add", command=open_add_product)
        product_menu.add_command(label="Delete")
        product_menu.add_command(label="Edit")

        add_product = tk.Button(
            product_container,
            text="Add Product",
            command=lambda: show_product_menu(product_menu, product_btn),
        )
        add_product.place(x=1410, y=15)

        note_container = tk.Frame(
            lead_entry,
            height=475,
            width=1528,
            bg="lightgray",
            borderwidth=2,
            relief=tk.GROOVE,
            highlightthickness=-0,
        )
        note_container.place(x=0, y=40)

        notes_text = tk.Label(note_container, text="Notes", bg="lightgray")
        notes_text.place(x=10, y=10)
        notes_entry = tk.Text(note_container, width=40, height=25, wrap=tk.WORD)
        notes_entry.pack(fill=tk.X, expand=True)
        note_container.place_forget()
