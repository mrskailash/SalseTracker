import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk


class FollowUp:
    followup_icon = None
    view_icon = None
    search_icon = None
    date_filter_icon = None
    refresh_icon = None

    def __init__(self, parent):
        self.parent = parent

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

            def on_text_change(event, text_widget, char_count_label, limit):
                char_count = len(text_widget.get("1.0", "end-1c").replace("\n", ""))
                char_count_label.config(text=f"{char_count}/{limit}")

            def validate_input(char, text_widget, char_count_label, limit):
                char_count = len(text_widget.get("1.0", "end-1c").replace("\n", ""))
                if char_count >= limit:
                    return False
                char_count_label.config(text=f"{char_count}/{limit}")
                return True

            def bind_text_widget_events(text_widget, char_count_label, limit):
                text_widget.bind(
                    "<Key>",
                    lambda event: on_text_change(
                        event, text_widget, char_count_label, limit
                    ),
                )
                text_widget.bind(
                    "<Key>",
                    lambda event: validate_input(
                        event.char, text_widget, char_count_label, limit
                    ),
                )

            # def show_box(box_number):
            #     # Hide all containers
            #     details_container.place_forget()
            #     # product_container.place_forget()
            #     # note_container.place_forget()

            #     history_btn.config(bg="lightgray" if box_number != 1 else "#0086B3")
            #     # product_btn.config(bg="lightgray" if box_number != 2 else "#0086B3")
            #     # notes_btn.config(bg="lightgray" if box_number != 3 else "#0086B3")
            #     # Display the selected container
            #     if box_number == 1:
            #         details_container.place(height=450, width=500)
            #     # elif box_number == 3:
            #     #     note_container.place(height=450, width=500)
            #     # elif box_number == 2:
            #     #     product_container.place(x=0, y=40, height=600, width=1500)

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
                # command=lambda: show_box(1),
            )
            history_btn.pack(side=tk.LEFT, anchor="n")

            # notes_btn = tk.Button(
            #     detail_window,
            #     text="Notes",
            #     font=("Arial", 12),
            #     height=1,
            #     width=12,
            #     command=lambda: show_box(3),
            # )
            # notes_btn.pack(side=tk.LEFT, anchor="n")

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

            # note_container = tk.Frame(
            #     lead_entry,
            #     height=450,
            #     width=500,
            #     bg="black",
            #     borderwidth=2,
            #     relief=tk.GROOVE,
            #     highlightthickness=-0,
            # )
            # note_container.place(x=0)
            # note_container.place_forget()

        lead_heading = tk.Frame(parent, bg="white", width=1505, height=55)
        lead_heading.pack(side=tk.TOP, anchor=tk.NW)

        separator = tk.Frame(parent, bg="black", height=2, width=1510)
        separator.pack(pady=5)

        lead_heading_menu2 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu2.place(x=12, y=10)

        lead_heading_menu3 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu3.place(x=80, y=10)

        lead_heading_menu4 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu4.place(x=150, y=10)

        lead_heading_menu5 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu5.place(x=220, y=10)

        lead_heading_menu6 = tk.Frame(lead_heading, bg="white", height=45, width=55)
        lead_heading_menu6.place(x=300, y=10)

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
            # command=fetch_lead_data,
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

        self.view_icon = Image.open("asset/followup/view.png")
        self.view_icon = self.view_icon.resize((25, 25))
        self.view_icon = ImageTk.PhotoImage(self.view_icon)

        view_button = tk.Button(
            lead_heading_menu3,
            image=self.view_icon,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
            height=25,
            width=25,
            # command=open_detail_window,
        )
        view_button.grid(row=0, column=1, padx=5)

        view_text = tk.Label(
            lead_heading_menu3,
            text="View",
            fg="black",
            bg="white",
            font=("Arial", 12),
        )
        view_text.grid(row=1, column=1)

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
            # command=fetch_lead_data,
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
            # command=search_window,
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
                "Name",
                "Date",
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
            "Name",
            "Date",
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
        self.tree.column("Name", width=50, anchor="center")
        self.tree.column("Date", width=50, anchor="center")
        self.tree.column("Location", width=50, anchor="center")
        self.tree.column("Follow up 1", width=50, anchor="center")
        self.tree.column("Follow up 2", width=50, anchor="center")
        self.tree.column("Follow up 3", width=50, anchor="center")
        self.tree.column("Follow up 4", width=50, anchor="center")
        self.tree.column("Follow up 5", width=50, anchor="center")
        self.tree.column("Follow up 6", width=50, anchor="center")
        self.tree.bind("<Double-1>", on_double_click)
        self.tree.pack(fill="both", expand=True, padx=10, pady=45)

        example_data = [
            (
                "1",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
            (
                "2",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
            (
                "3",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
            (
                "4",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
            (
                "5",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
            (
                "6",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
            (
                "7",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
            (
                "8",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
            (
                "9",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
            (
                "10",
                "John Doe",
                "2023-01-23",
                "usa",
            ),
        ]

        for data in example_data:
            self.tree.insert("", "end", values=data)
