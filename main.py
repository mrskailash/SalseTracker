import tkinter as tk

from PIL import Image, ImageTk

from components.header.master.product import Product
from components.header.master.source import Source
from components.header.master.status import status
from components.header.master.user import Users
from components.header.my.closure import Closure
from components.header.my.followup import FollowUp
from components.header.my.leadDetails import LeadDetails
from components.header.my.leadlist import LeadHeader
from components.header.my.report import Report
from components.header.Org.assign import Assign

# from components.header.Org.lead import Lead


class SalesTracker:
    def __init__(self, master):
        self.master = master
        master.title("SalesTracker")
        master.resizable(False, False)

        def center_window(window, width, height):
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x_coordinate = int((screen_width - width) / 2)
            y_coordinate = int((screen_height - height) / 2)
            window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        def open_profile():
            profile_window = tk.Toplevel(self.master)
            profile_window.title("Small Window")
            profile_window.geometry("50x50")
            center_window(profile_window, 487, 400)
            profile_window.resizable(False, False)
            profile_window.title("Profile")

            close_img_path = "asset/check_icon/close.png"
            close_icon = Image.open(close_img_path)
            close_icon = close_icon.resize((25, 25))
            self.close_icon_photo = ImageTk.PhotoImage(close_icon)

            close_btn = tk.Button(
                profile_window,
                image=self.close_icon_photo,
                borderwidth=2,
                highlightthickness=0,
                relief="flat",
            )
            close_btn.pack(anchor="ne", padx=12, pady=7)

            close_label = tk.Label(profile_window, text="close")
            close_label.place(x=445, y=34)

            separator1 = tk.Frame(profile_window, height=2, width=490, bg="black")
            separator1.place(y=55)

            profile_type_lable = tk.Label(
                profile_window, text="Admin", font=("Arial", 20)
            )
            profile_type_lable.place(y=85, x=15)

            btn_clr = "#0086B3"
            general_lable = tk.Label(
                profile_window,
                text="general",
                font=("Arial", 15),
                bg=btn_clr,
                padx=2,  # Adjust the padding on the x-axis
                pady=2,  # Adjust the padding on the y-axis
            )
            general_lable.place(y=120, x=17)

            userinfo = tk.Frame(
                profile_window,
                width=1500,
                height=300,
                bg="white",
                borderwidth=0,
                relief=tk.GROOVE,
                highlightthickness=-0,
            )
            userinfo.pack(pady=100, padx=15)
            userinfo.grid_propagate(False)

            user_type_lable = tk.Label(userinfo, text="User type", font=("Arial,30"))
            user_type_lable.grid(row=0, column=0, padx=15, pady=15)

            user_type_entry_lable = tk.Entry(userinfo, width=50)
            user_type_entry_lable.grid(row=0, column=1)

            email_lable = tk.Label(userinfo, text="Email", font=("Arial,30"))
            email_lable.grid(row=1, column=0, padx=15, pady=15)

            email_entry_lable = tk.Entry(userinfo, width=50)
            email_entry_lable.grid(row=1, column=1)

            mobile_lable = tk.Label(userinfo, text="Mobile", font=("Arial,30"))
            mobile_lable.grid(row=3, column=0, padx=15, pady=15)

            mobile_entry_lable = tk.Entry(userinfo, width=50)
            mobile_entry_lable.grid(row=3, column=1)

        def close_window(event=None):
            root.destroy()

        def show_menu(menu, button):
            menu.post(
                button.winfo_rootx(), button.winfo_rooty() + button.winfo_height()
            )

        def show_page(page_type):
            containers = [
                self.lead_list_container,
                self.lead_details_container,
                self.follow_up_container,
                self.closure_container,
                self.report_container,
                self.lead_container,
                self.assign_container,
                self.employee_container,
                self.product_container,
                self.parameter_container,
                self.status_container,
            ]

            for container in containers:
                container.pack_forget()

            if page_type == "list":
                self.lead_list_container.pack(fill=tk.BOTH, expand=True)
            elif page_type == "details":
                self.lead_details_container.pack(fill=tk.BOTH, expand=True)
            elif page_type == "followup":
                self.follow_up_container.pack(fill=tk.BOTH, expand=True)
            elif page_type == "closure":
                self.closure_container.pack(fill=tk.BOTH, expand=True)
            elif page_type == "smart report":
                self.report_container.pack(fill=tk.BOTH, expand=True)
            # elif page_type == "leads":
            #     self.lead_container.pack(fill=tk.BOTH, expand=True)
            elif page_type == "assign":
                self.assign_container.pack(fill=tk.BOTH, expand=True)
            elif page_type == "employee":
                self.employee_container.pack(fill=tk.BOTH, expand=True)
            elif page_type == "products":
                self.product_container.pack(fill=tk.BOTH, expand=True)
            elif page_type == "parameter":
                self.parameter_container.pack(fill=tk.BOTH, expand=True)
            elif page_type == "status":
                self.status_container.pack(fill=tk.BOTH, expand=True)

        def close_page():
            self.lead_list_container.pack_forget()
            self.lead_details_container.pack_forget()

        header_frame = tk.Frame(self.master, bg="lightgray", height=40)
        header_frame.pack(fill=tk.X, side=tk.TOP)

        # my menu
        menu_font = ("Arial", 12)
        my_menu = tk.Menu(header_frame, tearoff=0, font=menu_font)
        lead_menu = tk.Menu(my_menu, tearoff=0, font=menu_font)
        lead_menu.add_command(label="All Lead", command=lambda: show_page("list"))
        lead_menu.add_command(
            label="Add New Lead", command=lambda: show_page("details")
        )
        my_menu.add_cascade(label="Lead", menu=lead_menu)
        my_menu.add_command(label="Follow Up", command=lambda: show_page("followup"))
        my_menu.add_command(label="Closure", command=lambda: show_page("closure"))
        my_menu.add_command(label="My Profile", command=open_profile)
        report_menu = tk.Menu(my_menu, tearoff=0, font=menu_font)
        report_menu.add_command(
            label="Smart Report", command=lambda: show_page("smart report")
        )
        my_menu.add_cascade(label="Report", menu=report_menu)

        my_menu_button = tk.Button(
            header_frame,
            text="My",
            font="Arial 12",
            bg="gray",
            borderwidth=0,
            padx=10,
            pady=6,
            command=lambda: show_menu(my_menu, my_menu_button),
        )
        my_menu_button.pack(side=tk.LEFT)

        # organization menu
        org_menu = tk.Menu(header_frame, tearoff=0, font=menu_font)
        home_menu = tk.Menu(my_menu, tearoff=0, font=menu_font)
        home_menu.add_command(
            label="Dashboard",
        )
        # org_menu.add_command(label="Leads", command=lambda: show_page("leads"))
        org_menu.add_command(label="Assign", command=lambda: show_page("assign"))
        org_menu.add_cascade(label="Home", menu=home_menu)

        org_menu_button = tk.Button(
            header_frame,
            text="Organization",
            font="Arial 12",
            bg="gray",
            borderwidth=0,
            padx=10,
            pady=6,
            command=lambda: show_menu(org_menu, org_menu_button),
        )
        org_menu_button.pack(side=tk.LEFT)

        # master menu
        master_menu = tk.Menu(header_frame, tearoff=0, font=menu_font)
        master_menu.add_command(label="User", command=lambda: show_page("employee"))
        master_menu.add_command(label="Product", command=lambda: show_page("products"))
        master_menu.add_command(label="Source", command=lambda: show_page("parameter"))
        master_menu.add_command(label="Status", command=lambda: show_page("status"))

        # admin menu
        admin_menu = tk.Menu(header_frame, tearoff=0, font=menu_font)
        setting_menu = tk.Menu(my_menu, tearoff=0, font=menu_font)
        setting_menu.add_command(
            label="License",
        )
        setting_menu.add_command(
            label="DB Setting",
        )
        setting_menu.add_command(
            label="Control Panel",
        )
        admin_menu.add_cascade(label="Setting", menu=setting_menu)

        data_menu = tk.Menu(my_menu, tearoff=0, font=menu_font)
        data_menu.add_command(
            label="Restore",
        )
        data_menu.add_command(
            label="Backup",
        )
        admin_menu.add_cascade(label="Data", menu=data_menu)
        master_menu_button = tk.Button(
            header_frame,
            text="Master",
            font="Arial 12",
            bg="gray",
            borderwidth=0,
            padx=10,
            pady=6,
            command=lambda: show_menu(master_menu, master_menu_button),
        )
        master_menu_button.pack(side=tk.LEFT)

        admin_menu_button = tk.Button(
            header_frame,
            text="Admin",
            font="Arial 12",
            bg="gray",
            borderwidth=0,
            padx=10,
            pady=6,
            command=lambda: show_menu(admin_menu, admin_menu_button),
        )
        admin_menu_button.pack(side=tk.LEFT)

        self.lead_list_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.lead_list_container.pack(fill=tk.BOTH, expand=True)
        self.lead_list_container.pack_forget()

        self.lead_details_container = tk.Frame(
            master, bg="white", bd=1, relief=tk.SOLID
        )
        self.lead_details_container.pack(fill=tk.BOTH, expand=True)
        self.lead_details_container.pack_forget()

        self.follow_up_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.follow_up_container.pack(fill=tk.BOTH, expand=True)
        self.follow_up_container.pack_forget()

        self.closure_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.closure_container.pack(fill=tk.BOTH, expand=True)
        self.closure_container.pack_forget()

        self.report_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.report_container.pack(fill=tk.BOTH, expand=True)
        self.report_container.pack_forget()

        self.lead_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.lead_container.pack(fill=tk.BOTH, expand=True)
        self.lead_container.pack_forget()

        self.assign_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.assign_container.pack(fill=tk.BOTH, expand=True)
        self.assign_container.pack_forget()

        self.employee_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.employee_container.pack(fill=tk.BOTH, expand=True)
        self.employee_container.pack_forget()

        self.product_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.product_container.pack(fill=tk.BOTH, expand=True)
        self.product_container.pack_forget()

        self.parameter_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.parameter_container.pack(fill=tk.BOTH, expand=True)
        self.parameter_container.pack_forget()

        self.status_container = tk.Frame(master, bg="white", bd=1, relief=tk.SOLID)
        self.status_container.pack(fill=tk.BOTH, expand=True)
        self.status_container.pack_forget()

        close_image = Image.open("close.png").resize((25, 25))
        close_icon = ImageTk.PhotoImage(close_image)

        close_list = tk.Button(
            self.lead_details_container,
            image=close_icon,
            bg="white",
            borderwidth=0,
            command=close_page,
            height=35,
            width=35,
        )
        close_list.photo = close_icon
        close_list.place(x=1470, y=10)

        self.leadlist = LeadHeader(self.lead_list_container)
        self.leaddetails = LeadDetails(self.lead_details_container)
        self.follow_up = FollowUp(self.follow_up_container)
        self.closure = Closure(self.closure_container)
        self.report = Report(self.report_container)
        # # self.lead = Lead(self.lead_container)
        self.assign = Assign(self.assign_container)
        self.employee = Users(self.employee_container)
        self.product = Product(self.product_container)
        self.parameter = Source(self.parameter_container)
        self.status = status(self.status_container)
        root.bind("<Alt-x>", close_window)


def open_new_window(event=None):
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    label = tk.Label(new_window, text="This is a new window!")
    label.pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1515x815+1+6")

    # Bind Alt+F to open_new_window function
    root.bind("<Control-f>", open_new_window)

    app = SalesTracker(root)
    root.mainloop()
