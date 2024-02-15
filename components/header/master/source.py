import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class Source:
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

        def fetch_source_data():
            # Connect to MySQL server
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Fetch data from the leadlist table
            cursor.execute("SELECT id, sourcename FROM source")
            lead_data = cursor.fetchall()

            # Close the database connection
            conn.commit()
            conn.close()

            # Clear existing data in the treeview
            self.tree.delete(*self.tree.get_children())

            # Insert fetched data into the treeview
            for leadrow in lead_data:
                (id, sourcename) = leadrow
                self.tree.insert("", "end", values=(id, sourcename))

        def delete_source():
            items = self.tree.selection()
            if not items:
                messagebox.showwarning("No Row Selected", "Select a row to delete.")
                return

            confirm = messagebox.askyesno(
                "Confirm Deletion",
                "Are you sure you want to delete the selected row(s)?",
            )
            if not confirm:
                return

            # Get the IDs of the selected rows
            selected_ids = [self.tree.item(item, "values")[0] for item in items]

            # Connect to the database
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Delete the selected rows
            for lead_id in selected_ids:
                cursor.execute("DELETE FROM source WHERE id=?", (lead_id,))

            # Commit the changes
            conn.commit()

            # Vacuum to reset autoincrement counter
            cursor.execute("VACUUM")
            conn.commit()
            fetch_source_data()

        def save_data():
            # Get data from entry widgets
            name = self.name_entry.get()

            # Check if any of the entry fields is empty
            if not name:
                messagebox.showerror("Error", "Please fill in name fields.")
                return

            # Connect to the database
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Insert data into the 'user' table
            cursor.execute(
                "INSERT INTO source (sourcename) VALUES (?)",
                (name,),
            )

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Data saved successfully.")

            self.name_entry.delete(0, tk.END)
            fetch_source_data()

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
            edit_window.title(f"Edit Lead - id: {lead_no}, status: {name}")

            # Fetch the selected lead data from the database
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT sourcename FROM source WHERE id=?",
                (lead_no,),
            )
            lead_data = cursor.fetchone()
            conn.close()

            # Populate the entry widgets with existing data
            entry_widgets = []
            labels = [
                "Source name",
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
                updated_values = [
                    entry.get("1.0", tk.END).strip() if i == 1 else entry.get()
                    for i, entry in enumerate(entry_widgets)
                ]
                # Update the database with the new values
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE source SET sourcename=? WHERE id=?",
                    tuple(updated_values + [lead_no]),
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "source is updated successfully.")
                edit_window.destroy()
                fetch_source_data()

            save_button = tk.Button(
                edit_window, text="Save Changes", command=save_changes
            )
            save_button.grid(row=len(lead_data), column=0, columnspan=2, pady=10)

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

        def clear_entries():
            self.name_entry.delete(0, tk.END)

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

        save_button = tk.Button(
            lead_heading_menu2,
            image=self.save_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            command=save_data,
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
            command=delete_source,
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
            command=fetch_source_data,
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

        lead_list_text = tk.Label(
            parent, text="Source List", bg="white", font=("Arial", 16)
        )
        lead_list_text.place(x=5, y=70)

        sourcentry = tk.Frame(
            parent, relief="solid", borderwidth=2, bg="white", height=350, width=750
        )
        sourcentry.place(x=10, y=350)
        sourcentry.grid_propagate(False)
        sourcename = tk.Label(
            sourcentry, text="Source Name", font=("Arial", 12), bg="white"
        )
        sourcename.grid(column=0, row=0, padx=15, pady=12)

        self.name_entry = tk.Entry(
            sourcentry,
            borderwidth=2,
            highlightthickness=-0,
            relief=tk.GROOVE,
            width=50,
        )
        self.name_entry.grid(column=1, row=0, padx=15, pady=12)

        save_button = tk.Button(sourcentry, text="Save", width=10, command=save_data)
        save_button.grid(column=0, row=1, padx=5)

        self.tree = ttk.Treeview(
            parent,
            columns=("id", "Source Name"),  # Change "Name" to "Source Name"
            show="headings",
        )
        headings = ["id", "Source Name"]  # Change "Name" to "Source Name"
        for i, heading in enumerate(headings):
            self.tree.heading(i, text=heading, anchor="center")
            self.tree.column(
                heading, anchor="center"
            )  # Use the heading as the column identifier

        def open_context_menu(event):
            item = self.tree.selection()
            if item:
                menu.post(event.x_root, event.y_root)

        menu = tk.Menu(self.tree, tearoff=0)
        menu.add_command(label="Edit", command=get_lead)
        menu.add_command(label="Delete", command=delete_source)
        self.tree.bind("<Button-3>", open_context_menu)
        self.tree.pack(side=tk.LEFT, anchor="n", padx=10, pady=45)

        fetch_source_data()
