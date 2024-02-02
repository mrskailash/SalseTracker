import tkinter as tk
from tkinter import ttk

class leadlist:
    def __init__(self, parent):
        self.parent = parent

        lead_list = tk.Frame(self.parent,
                             borderwidth=2,
                             relief=tk.GROOVE,
                             highlightthickness=-0,
                             highlightbackground="gray",
                             highlightcolor="gray",
                             bg="lightgray",
                             height=200, width=1500)
        lead_list.pack(fill=tk.X)

        lead_list_text = tk.Label(lead_list, text="Lead List")
        lead_list_text.place(x=5, y=5)

        lead_list_table_container = tk.Frame(lead_list, height=170, width=1300)
        lead_list_table_container.place(x=5, y=20)

        lead_list_table = ttk.Treeview(lead_list_table_container, columns=("Lead No", "Date", "Name", "Contact Person", "Amount", "Assign To"), show="headings", height=10)

        lead_list_table.heading("Lead No", text="Lead No")
        lead_list_table.heading("Date", text="Date")
        lead_list_table.heading("Name", text="Name")
        lead_list_table.heading("Contact Person", text="Contact Person")
        lead_list_table.heading("Amount", text="Amount")
        lead_list_table.heading("Assign To", text="Assign To")

        # Create vertical scrollbar
        yscrollbar = tk.Scrollbar(lead_list_table_container, orient="vertical", command=lead_list_table.yview)
        yscrollbar.pack(side="right", fill="y")

        # Connect scrollbar to the treeview
        lead_list_table.configure(yscrollcommand=yscrollbar.set)

        lead_list_table.pack()
