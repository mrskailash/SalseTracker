import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk


class Users:
    search_icon = None
    date_filter_icon = None
    refresh_icon = None
    add_icon = None

    def __init__(self, parent):
        self.parent = parent

        def fetch_employe_data():
            # Connect to MySQL server
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()
            # Fetch data from the leadlist table
            cursor.execute("SELECT id,Uname, name, type FROM user")
            lead_data = cursor.fetchall()

            # Close the database connection
            conn.commit()
            conn.close()

            # Clear existing data in the treeview
            self.tree.delete(*self.tree.get_children())

            # Insert fetched data into the treeview
            for leadrow in lead_data:
                (id, uname, name, employee_type) = leadrow
                self.tree.insert("", "end", values=(id, uname, name, employee_type))

        def delete_lead():
            items = self.tree.selection()
            if not items:
                messagebox.showwarning("No Row Selected", "Select a row to delete.")
                return

            confirm = messagebox.askyesno(
                "Confirm Deletion", "Are you sure you want to delete the selected row?"
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
                cursor.execute("DELETE FROM user WHERE id=?", (lead_id,))

            # Commit the changes
            conn.commit()

            # Close the connection
            conn.close()

            # Reset the ID sequence in sqlite_sequence table
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE user SET id=0 WHERE name='user'")
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Row(s) deleted successfully.")

            # Refresh the table after deletion
            fetch_employe_data()

        def save_data():
            # Get data from entry widgets
            uname = self.name_entry.get()
            name = self.profile_entry.get()
            profile_type = self.profile_type.get()

            # Check if any of the entry fields is empty
            if not uname or not name or not profile_type:
                messagebox.showerror("Error", "Please fill in all the fields.")
                return

            # Connect to the database
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()

            # Insert data into the 'user' table
            cursor.execute(
                "INSERT INTO user (uname, name, type) VALUES (?, ?, ?)",
                (uname, name, profile_type),
            )

            # Commit the changes and close the connection
            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Data saved successfully.")

            self.name_entry.delete(0, tk.END)
            self.profile_entry.delete(0, tk.END)
            self.profile_type.set(" ")

        lead_heading = tk.Frame(parent, bg="white", width=1300, height=55)
        lead_heading.pack(side=tk.TOP, anchor=tk.NW)

        separator = tk.Frame(parent, bg="black", height=2, width=1510)
        separator.pack(pady=5)

        lead_heading_menu4 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu4.place(x=12, y=10)

        lead_heading_menu5 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu5.place(x=80, y=10)

        lead_heading_menu6 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu6.place(x=125, y=10)

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
            command=fetch_employe_data,
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

        def clear_entries():
            self.name_entry.delete(0, tk.END)
            self.profile_entry.delete(0, tk.END)
            self.profile_type.set(" ")  # Correct the attribute name

        self.add_icon = Image.open("asset/Lead_icon/plus.png")
        self.add_icon = self.add_icon.resize((25, 25))
        self.add_icon = ImageTk.PhotoImage(self.add_icon)

        add_button = tk.Button(
            lead_heading_menu5,
            image=self.add_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            command=clear_entries,
        )
        add_button.grid(row=0, column=1)

        add_text = tk.Label(
            lead_heading_menu5, text="new", fg="black", bg="white", font=("Arial", 12)
        )
        add_text.grid(row=1, column=1)

        self.save_icon = Image.open("asset/Lead_icon/diskette.png")
        self.save_icon = self.save_icon.resize((25, 25))
        self.save_icon = ImageTk.PhotoImage(self.save_icon)

        save_button = tk.Button(
            lead_heading_menu6,
            image=self.save_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            command=save_data,
        )
        save_button.grid(row=0, column=1)

        save_text = tk.Label(
            lead_heading_menu6, text="save", fg="black", bg="white", font=("Arial", 12)
        )
        save_text.grid(row=1, column=1)

        lead_list_text = tk.Label(parent, text="User List", font=("Arial", 16))
        lead_list_text.place(x=15, y=80)

        self.tree = ttk.Treeview(
            parent,
            columns=("id", "name", "Profile Name", "Profile type"),
            show="headings",
            height=10,
        )
        headings = ["id", "name", "Profile Name", "Profile type"]
        for i, headings in enumerate(headings):
            self.tree.heading(i, text=headings, anchor="center")

        self.tree.column("id", anchor="center", width=10)
        self.tree.column(
            "name",
            anchor="center",
        )
        self.tree.column(
            "Profile Name",
            anchor="center",
        )
        self.tree.column(
            "Profile type",
            anchor="center",
        )

        self.tree.pack(fill="y", side=tk.LEFT, padx=10, pady=45)

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
            edit_window.title(f"Edit Lead - Name: {lead_no}, Name: {name}")

            # Fetch the selected lead data from the database
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT Uname, name, type FROM user WHERE id=?",
                (lead_no,),
            )
            lead_data = cursor.fetchone()
            conn.close()
            # Populate the entry widgets with existing data
            entry_widgets = []
            labels = [
                "name",
                "profile_name",
                "profile_type",
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
                    "UPDATE user SET uname=?,name=?, type=? WHERE id=?",
                    tuple(updated_values + [lead_no]),
                )
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "user is  updated successfully.")
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
        menu.add_command(label="Edit", command=get_lead)
        menu.add_command(label="Delete", command=delete_lead)
        self.tree.bind("<Button-3>", open_context_menu)
        userentry = tk.Frame(
            parent, relief="solid", borderwidth=2, bg="white", height=600, width=750
        )
        userentry.place(x=615, y=112)
        userentry.grid_propagate(False)

        name = tk.Label(userentry, text="Name", font=("Arial", 12), bg="white")
        name.grid(column=0, row=0, padx=15, pady=12)

        self.name_entry = tk.Entry(
            userentry, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=50
        )
        self.name_entry.grid(column=1, row=0, padx=15, pady=12)

        profile = tk.Label(
            userentry, text="Profile name", font=("Arial", 12), bg="white"
        )
        profile.grid(column=0, row=1, padx=15, pady=12)

        self.profile_entry = tk.Entry(
            userentry, borderwidth=2, highlightthickness=-0, relief=tk.GROOVE, width=50
        )
        self.profile_entry.grid(column=1, row=1, padx=15, pady=12)

        Profile_type = tk.Label(
            userentry, text="Profile_type", font=("Arial", 12), bg="white"
        )
        Profile_type.grid(column=0, row=2, padx=15, pady=12)

        Profile_type_value = ["Sales"]
        self.profile_type = ttk.Combobox(userentry, values=Profile_type_value, width=45)
        self.profile_type.grid(column=1, row=2, padx=15, pady=12)

        save_button = tk.Button(userentry, text="Save", width=10, command=save_data)
        save_button.grid(column=0, row=3, pady=10)
        # Fetch data and populate the table
        fetch_employe_data()
