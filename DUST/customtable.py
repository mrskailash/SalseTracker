import tkinter as tk


class CustomTable(tk.Canvas):
    def __init__(self, parent, rows, columns, cell_width=100, cell_height=30, **kwargs):
        super().__init__(parent, **kwargs)
        self.rows = rows
        self.columns = columns
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.headers = []

        self.draw_table()

    def draw_table(self):
        # Draw grid lines
        for row in range(self.rows + 1):
            self.create_line(
                0,
                row * self.cell_height,
                self.columns * self.cell_width,
                row * self.cell_height,
                fill="black",
            )

        for col in range(self.columns + 1):
            self.create_line(
                col * self.cell_width,
                0,
                col * self.cell_width,
                self.rows * self.cell_height,
                fill="black",
            )

        # Draw column headers
        for col in range(self.columns):
            header_text = f"Header {col + 1}"
            header = self.create_text(
                col * self.cell_width + self.cell_width / 2, 10, text=header_text
            )
            self.headers.append(header)

        # Draw table cells
        for row in range(self.rows):
            for col in range(self.columns):
                cell_text = f"Row {row + 1}, Col {col + 1}"
                self.create_text(
                    col * self.cell_width + self.cell_width / 2,
                    (row + 1) * self.cell_height + self.cell_height / 2,
                    text=cell_text,
                )

        # Set the canvas size
        self.config(
            scrollregion=(
                0,
                0,
                self.columns * self.cell_width,
                (self.rows + 1) * self.cell_height,
            )
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Table Example")

    custom_table = CustomTable(
        root,
        rows=10,
        columns=5,
        width=600,
        height=300,
        bg="white",
        borderwidth=2,
        relief=tk.GROOVE,
    )
    custom_table.pack(padx=10, pady=10)

    root.mainloop()
