from tkinter import *

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