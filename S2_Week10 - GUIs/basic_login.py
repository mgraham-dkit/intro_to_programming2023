from tkinter import *


def login():
    print("I'm broken!!!")
    entered_username = login_field.get()
    if entered_username == user[0]:
        status_label["text"] = "Status: Logged in!"


user = ("admin", "password")

window = Tk()
window.title("Intro GUI")
window.geometry("300x400")

login_label = Label(window, text="My name is????")
login_label.pack()

login_field = Entry(window)
login_field.pack()

login_button = Button(window, text="Submit", command=login)
login_button.pack()

status_label = Label(window, text="Status: Not logged in.")
status_label.pack()

window.mainloop()