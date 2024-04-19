from tkinter import *
from tkinter.font import *
from tkinter import messagebox


def login():
    print("I'm running!!!")
    entered_username = login_field.get()
    entered_password = login_password_field.get()
    if entered_username == "" or entered_password == "":
        status_label["text"] = "Error: No information entered!"
        messagebox.showwarning("Warning", "Missing username and/or password")
    elif entered_username == user[0] and entered_password == user[1]:
        status_label["text"] = "Status: Logged in!"
        messagebox.showinfo("Congrats!", "You are now logged in")
        login_panel.pack_forget()
    else:
        status_label["text"] = "Status: Username and/or password not valid!"
        messagebox.showerror("Error", "Incorrect information supplied.")


user = ("admin", "password")

window = Tk()
window.title("Intro GUI")
window.geometry("400x300")

font_label_setting = Font(window, size=25, family="Arial")

login_panel = Frame(window)

login_label = Label(login_panel, text="Username", font=font_label_setting)
login_label.pack()

login_field = Entry(login_panel, font=font_label_setting)
login_field.pack(padx=5)

login_password_label = Label(login_panel, text="Password", font=font_label_setting)
login_password_label.pack()

login_password_field = Entry(login_panel, show="*", font=font_label_setting)
login_password_field.pack(padx=5)

login_button = Button(login_panel, text="Submit", command=login, font=font_label_setting)
login_button.pack()

status_label = Label(login_panel, text="Status: Not logged in.", font=font_label_setting)
status_label.pack()

login_panel.pack()

window.mainloop()
