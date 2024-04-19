from tkinter import *
from tkinter.font import *
from tkinter import messagebox

'''
    EXERCISE:
        1) Amend this code to display "Status: Login failed" where the user
        attempts to log in and fails
        2) Amend the code to check if the text field actually contained text
        when the user tried to log in. Display "Error: You must enter a username"
        if nothing was entered.
        Hint: If there is text in the list, the string you get out of it
        will be longer than 0.
        3) Amend the GUI to contain a password entry field and corresponding label.
        Update your login() command function to check if both the username
        AND password entered match the credentials stored in the user tuple,
        not just the username.
'''

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
        login_button.pack_forget()
    else:
        status_label["text"] = "Status: Username and/or password not valid!"
        messagebox.showerror("Error", "Incorrect information supplied.")


user = ("admin", "password")

window = Tk()
window.title("Intro GUI")
window.geometry("400x300")

font_label_setting = Font(window, size=25, family="Arial")

login_label = Label(window, text="Username", font=font_label_setting)
login_label.pack()

login_field = Entry(window, font=font_label_setting)
login_field.pack(padx=5)

login_password_label = Label(window, text="Password", font=font_label_setting)
login_password_label.pack()

login_password_field = Entry(window, font=font_label_setting)
login_password_field.pack(padx=5)

login_button = Button(window, text="Submit", command=login, font=font_label_setting)
login_button.pack()

status_label = Label(window, text="Status: Not logged in.", font=font_label_setting)
status_label.pack()

window.mainloop()