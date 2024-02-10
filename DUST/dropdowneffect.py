import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk


class MyTreeViewApp:
    def __init__(self, parent):
        self.parent = parent
        self.selected_rows = []  # Store selected row indices

        def view_lead():
            items = self.tree.selection()
            if len(items) == 1:
                lead_id = self.tree.item(items[0], "values")[0]

                # Fetch the selected lead data from the database
                conn = sqlite3.connect("salestracker.db")
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company, follow_up1, follow_up2, follow_up3, follow_up4, follow_up5, follow_up6 FROM leadlist WHERE id=?",
                    (lead_id,),
                )
                lead_data = cursor.fetchone()
                conn.close()

                # Create a new window to display the lead data
                view_window = tk.Toplevel(self.parent)
                view_window.geometry("300x425+1200+90")
                view_window.title("View Lead Window")

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
                    "Follow Up 1",
                    "Follow Up 2",
                    "Follow Up 3",
                    "Follow Up 4",
                    "Follow Up 5",
                    "Follow Up 6",
                ]

                for i, value in enumerate(lead_data):
                    label = tk.Label(view_window, text=f"{labels[i]}: {value}")
                    label.pack(pady=5)

            else:
                messagebox.showwarning("No Row Selected", "Select a row to view.")

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

        def fetch_lead_data():
            conn = sqlite3.connect("salestracker.db")
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, date, fullname, address, mobileno, email, source, assignto, status, ref_by, products, remark, company FROM leadlist"
            )
            lead_data = cursor.fetchall()
            conn.close()
            return lead_data

        def populate_treeview():
            lead_data = fetch_lead_data()
            for lead_row in lead_data:
                self.tree.insert("", "end", values=lead_row)

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
            selectmode="extended",  # Allows multiple row selection
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

        for i, heading in enumerate(headings):
            self.tree.heading(i, text=heading, anchor="center")
            self.tree.column(heading, width=50, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=10, pady=45)

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
        menu.add_command(label="Edit", command=get_lead)
        menu.add_command(label="View", command=view_lead)
        menu.add_command(label="Delete", command=delete_lead)
        self.tree.bind("<Button-3>", open_context_menu)
        populate_treeview()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1515x815+1+6")
    app = MyTreeViewApp(root)
    root.mainloop()
