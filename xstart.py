from tkinter import *

root = Tk()
root.title('Warehouse Management System')
root.geometry('345x250')

def login():
    root.destroy()
    import xlogin

def register():
    root.destroy()
    import xregister

button_login = Button(root, width= 38, borderwidth= 5, text= 'Login', command= login).place(x=20, y= 78)
button_register = Button(root, width= 38, borderwidth= 5, text= 'Register', command= register).place(x=20, y= 119)


root.mainloop()