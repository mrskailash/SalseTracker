# main.py

import tkinter as tk

from btn_file import BtnFile
from entry_file import EntryFile


class MainApp:
    def __init__(self, master):
        self.main_frame = tk.Frame(master, width=200, height=200, bg="black")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create an instance of EntryFile
        self.entry_file = EntryFile(self.main_frame)
        BtnFile.create_button(self.main_frame, self.clear_entries)

    def clear_entries(self):
        # The callback will be called from BtnFile
        BtnFile.clear_entries(self.entry_file)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = MainApp(root)
    root.mainloop()
