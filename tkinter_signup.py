import tkinter as tk
from tkinter import Entry, Label, PhotoImage, Button, messagebox
import os

class LoginFrame:
    def __init__(self, root):
        self.root = root
        self.root.title("Elite Bakers")
        self.root.geometry("1000x700+500+400")

       # Background image
        img = PhotoImage(file="EliteBakers.pgm")
        self.root.label = Label(self.root, image=img)
        self.root.label.image = img  
        self.root.label.place(relwidth=1, relheight=1)

        # Welcome message and buttons
        frame1 = tk.Frame(root, width=400, height=530, bg="#71a6d2")
        frame1.place(x=100, y=100)

        welcome_label = tk.Label(frame1, text="WELCOME!", bg="#71a6d2", fg="white", font=("Times", 30, "bold"))
        welcome_label.place(relx=0.2, rely=0.2)

        elite_label = tk.Label(frame1, text="\nto ELITE BAKERS! \n to get elite taste at your doorsteps.", bg="#71a6d2", fg="white", font=("Times", 15, "bold"))
        elite_label.place(relx=0.1, rely=0.3)

        login_button = Button(frame1, width=10, pady=7, text="Login", font=("Times", 10), bg="white", fg="black", border=0, command=self.show_login_frame)
        login_button.place(relx=0.2, rely=0.7)

        signup_button = Button(frame1, width=10, pady=7, text="Sign Up", font=("Times", 10), bg="white", fg="black", border=0, command=self.show_signup_frame)
        signup_button.place(relx=0.4, rely=0.7)

        exit_button = Button(frame1, width=10, pady=7, text="Exit", font=("Times", 10), bg="white", fg="black", border=0, command=self.exit)
        exit_button.place(relx=0.6, rely=0.7)

        
    def show_login_frame(self):
        login_frame = tk.Frame(self.root, width=400, height=530, bg="white")
        login_frame.place(x=500, y=100)

        login_heading = tk.Label(login_frame, text=" Log in ", bg="white", font=("Times", 25, "bold"))
        login_heading.place(x=120, y=20)

        email_label = tk.Label(login_frame, text="Email Address:", bg="white", font=("Times", 15))
        email_label.place(x=70, y=80)

        self.email_var = tk.StringVar()
        email_entry = tk.Entry(login_frame, textvariable=self.email_var, width=25, fg="black", border=0, bg="white", font=("Times", 15))
        email_entry.place(x=70, y=110)

        password_label = tk.Label(login_frame, text="Password:", bg="white", font=("Times", 15))
        password_label.place(x=70, y=150)

        self.password_var = tk.StringVar()
        password_entry = tk.Entry(login_frame, textvariable=self.password_var, width=25, fg="black", border=0, bg="white", font=("Times", 15), show="*")
        password_entry.place(x=70, y=180)

        login_button = tk.Button(login_frame, width=39, pady=7, text="Sign in", bg="#71a6d2", fg="black", border=0, command=self.login)
        login_button.place(x=70, y=220)
        


    def login(self):
        email = self.email_var.get()
        password = self.password_var.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        elif "@" not in email:
            messagebox.showerror("Error", "Your email address must have '@' in it\nPlease write your email address again: ", parent=self.root)
        elif len(email) <= 6:
            messagebox.showerror("Error", "Your email address is too short\nPlease write your email address again: ", parent=self.root)
        elif "." not in email:
            messagebox.showerror("Error", "Your email address must have '.com' in it\nPlease write your email address again: ", parent=self.root)
        elif len(password) <= 8:
            messagebox.showerror("Error", "Please re-enter your password \nIt must be at least 8 characters long", parent=self.root)
        elif len(password) > 12:
            messagebox.showerror("Error", "Please re-enter your password \nIt must be at least 8 characters long", parent=self.root)
        else:
            os.system("menu2.py")

    def show_signup_frame(self):
        signup_frame = tk.Frame(root, width=400, height=530, bg="white")
        signup_frame.place(x=500, y=100)

        name1_label = tk.Label(signup_frame, text="First Name:", bg="white", font=("Times", 13, "bold"))
        name1_label.place(x=70, y=50)

        self.name1_var = tk.StringVar()
        name1_entry = tk.Entry(signup_frame, textvariable=self.name1_var, width=25, fg="black", border=0, bg="white", font=("Times", 15))
        name1_entry.place(x=70, y=80)

        name2_label = tk.Label(signup_frame, text="Last Name:", bg="white", font=("Times", 13, "bold"))
        name2_label.place(x=70, y=110)

        self.name2_var = tk.StringVar()
        name2_entry = tk.Entry(signup_frame, textvariable=self.name2_var, width=25, fg="black", border=0, bg="white", font=("Times", 15))
        name2_entry.place(x=70, y=140)

        email_label = tk.Label(signup_frame, text="Email Address:", bg="white", font=("Times", 13, "bold"))
        email_label.place(x=70, y=170)

        self.email_var = tk.StringVar()
        email_entry = Entry(signup_frame, textvariable=self.email_var, width=25, fg="black", border=0, bg="white", font=("Times", 15))
        email_entry.place(x=70, y=200)

        password_label = tk.Label(signup_frame, text="Password:", bg="white", font=("Times", 13, "bold"))
        password_label.place(x=70, y=230)

        self.password_var = tk.StringVar()
        password_entry = tk.Entry(signup_frame, textvariable=self.password_var, width=25, fg="black", border=0, bg="white", font=("Times", 15,), show="*")
        password_entry.place(x=70, y=260)

        city_label = tk.Label(signup_frame, text="City:", bg="white", font=("Times", 13, "bold"))
        city_label.place(x=70, y=290)

        self.city_var = tk.StringVar()
        city_entry = Entry(signup_frame, textvariable=self.city_var, width=25, fg="black", border=0, bg="white", font=("Times", 15))
        city_entry.place(x=70, y=320)

        phone_label = tk.Label(signup_frame, text="Phone Number:", bg="white", font=("Times", 13, "bold"))
        phone_label.place(x=70, y=350)

        self.phone_var = tk.StringVar()
        phone_entry = tk.Entry(signup_frame, textvariable=self.phone_var, width=25, fg="black", border=0, bg="white", font=("Times", 15))
        phone_entry.place(x=70, y=380)

        signup_button = Button(signup_frame, width=39, pady=7, text="Sign up", bg="#71a6d2", fg="black", border=0, command=self.register_data)
        signup_button.place(x=70, y=410)

    def register_data(self):
        name1 = self.name1_var.get()
        name2 = self.name2_var.get()
        email = self.email_var.get()
        password = self.password_var.get()
        city = self.city_var.get()
        phone = self.phone_var.get()
        invalid_characters = "!#$%^&*()_.,:/\\|:;><?"


    

        error_flag = False 
        if "@" not in email:
             messagebox.showerror("Error", "Your email address must have '@' in it\nPlease write your email address again: ", parent=self.root)
             error_flag = True
        elif len(email) <= 6:
             messagebox.showerror("Error", "Your email address is too short\nPlease write your email address again: ", parent=self.root)
             error_flag = True
        elif ".com" not in email:
             messagebox.showerror("Error", "Your email address must have '.' in it\nPlease write your email address again: ", parent=self.root)
             error_flag = True
        elif len(password) <= 8:
             messagebox.showerror("Error", "Please re-enter your password \nIt must be at least 8 characters long", parent=self.root)
             error_flag = True
        elif len(password) > 12:
            messagebox.showerror("Error", "Please re-enter your password \nIt must be at least 8 characters long", parent=self.root)
            error_flag = True
        if any(char in invalid_characters for char in city):
             messagebox.showerror("Error", "Please re-enter your city", parent=self.root)
             error_flag = True
        if any(char in invalid_characters for char in name1 ):
             messagebox.showerror("Error", "Please re-enter your name", parent=self.root)
             error_flag = True  


        num = phone.split("-") 
        area = num[0]
        if not area.isdigit() or len(phone) != 11:
   
              messagebox.showerror("Error", "Please enter a valid 11-digit phone number", parent=self.root)

              num = phone.split("-")
              area = num[0]
        

        if (
               name1 == ""
               or name2 == ""
               or phone == ""
               or password == ""
               or city == ""
               or email == ""
              ):
             messagebox.showerror("Error", "All Fields are Required", parent=self.root)

    

        if not error_flag:
            os.system("menu2.py")
    



    def exit(self):
        self.root.destroy()


# Create the main screen
root = tk.Tk()
obj = LoginFrame(root)
root.mainloop()
