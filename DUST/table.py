import tkinter as tk
from tkinter import ttk

class TableApp:
    def __init__(self, parent):
        self.parent = parent

        # Create a treeview widget
        self.tree = ttk.Treeview(parent, columns=("Product", "Quantity", "Rate", "Amount", "Description"), show="headings")

        # Define column headers
        self.tree.heading("Product", text="Product")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Rate", text="Rate")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Description", text="Description")

        # Add grid lines (thin white column between each data column)
        for col in ("Product", "Quantity", "Rate", "Amount"):
            self.tree.column(col, anchor="center", width=100, stretch=True)
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column("#0", width=1, stretch=False, minwidth=0)

        # Configure style for the treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#CCCCCC", foreground="black")
        style.configure("Treeview", font=("Arial", 9), rowheight=25, highlightthickness=0, bd=0, background="white", fieldbackground="white")
        style.map("Treeview", background=[('selected', 'black')])

        data = [
            ("Product A", 10, 5.0, 50.0, "Description 1"),
            ("Product B", 5, 8.0, 40.0, "Description 2"),
            # ... add more data here ...
        ]

        for _ in range(50):  # Add 50 rows of data
            for row in data:
                self.tree.insert("", "end", values=row)

        # Create vertical scrollbar
        yscrollbar = tk.Scrollbar(parent, orient="vertical", command=self.tree.yview)
        yscrollbar.pack(side="right", fill="y")

        # Create horizontal scrollbar
        xscrollbar = tk.Scrollbar(parent, orient="horizontal", command=self.tree.xview)
        xscrollbar.pack(side="bottom", fill="x")

        # Connect scrollbars to the treeview
        self.tree.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

        # Pack the treeview widget
        self.tree.pack(fill=tk.BOTH, expand=True)

def main():
    root = tk.Tk()
    root.title("Product Table")
    root.state('zoomed')
    product_container = tk.Frame(root, height=600, width=800, bg="lightgray", borderwidth=2,
                                 relief=tk.GROOVE, highlightthickness=0)
    product_container.place(x=0, y=40)

    product_details_text = tk.Label(product_container, text="Product Details", font=("Arial", 8))
    product_details_text.place(x=15, y=15)

    # Create an instance of TableApp and pass the product_container as the parent
    table_app = TableApp(product_container)

    root.mainloop()

if __name__ == "__main__":
    main()
