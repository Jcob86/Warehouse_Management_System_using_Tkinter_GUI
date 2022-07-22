from os import remove
from tkinter import *
import time
from tkinter.font import names

root = Tk()
root.title('Registration')
root.geometry('300x350')

userName = StringVar()
Password = StringVar()
Password_confirm = StringVar()

def register_user():
    username_info = userName.get()
    password1_info = Password.get()
    password2_info = Password_confirm.get()
    
    if password1_info == password2_info:
        if username_info != '' and password1_info != '':
            addUserInfo([username_info, password1_info])
            login_enter.delete(0, END)
            password_enter.delete(0, END)
            password2_enter.delete(0, END)
            register_success = Label(root, bg= 'green', width=40, text='Registered successfully!')
            register_success.place(x=9, y=300)
            root.after(2500, lambda: register_success.destroy())
        else:
            information = Label(root, bg= 'red', width= 40, text= 'No login or password, try again!')
            information.place(x=9, y=300)
            root.after(2000, lambda: information.destroy())
            login_enter.delete(0, END)
            password_enter.delete(0, END)
            password2_enter.delete(0, END)
    
    if password1_info != password2_info:
        password_match = Label(root, bg='red', width=40, text='Your passwords does not match!')
        password_match.place(x =9, y=300)
        root.after(2000, lambda: password_match.destroy())
        login_enter.delete(0, END)
        password_enter.delete(0, END)
        password2_enter.delete(0, END)
    
def addUserInfo(userInfo: list):
    with open('userInfos.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')

def UserAlreadyExist():
    return

def login_system():
    root.destroy()
    import xlogin

login_info = Label(root, text = 'Login:', bg= 'grey').place(x=20, y=9)
login_enter = Entry(root, width = 40, borderwidth = 5, textvariable= userName)
login_enter.place(x=20, y=30)

password_info = Label(root, text='Password:', bg='grey').place(x=20, y=79)
password_enter = Entry(root, width= 40, borderwidth= 5, textvariable= Password, show='*')
password_enter.place(x=20, y=100)

confirm_password = Label(root, text='Confirm Password:', bg= 'grey').place(x=20, y=149)
password2_enter = Entry(root, width= 40, borderwidth= 5, textvariable= Password_confirm, show='*')
password2_enter.place(x=20, y=170)

button_register = Button(root, text='Register', width=34, borderwidth= 5, command= register_user).place(x=20, y=210)
button_login = Button(root, text='Go to Log In page', width=34, borderwidth= 5, command= login_system).place(x=20, y=245)

root.mainloop()