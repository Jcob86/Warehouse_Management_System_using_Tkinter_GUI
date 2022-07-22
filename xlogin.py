# PANEL LOGOWANIA, OKNO LOGIN, OKNO HASLO NA SRODKU, PRZYCISK ZALOGUJ POD TYM(JAK DA RADE TO NA ENTER), PO ZALOGOWANIU: 
# STAN MAGAZYNOWY, DODAJ PRZEDMIOTY(DOSTAWA), USUN PRZEDMIOTY(SPRZEDAZ), PRACOWNICY AKTUALNIE PRACUJACY Z DODWANIEM GODZIN ICH PRACY
# ZAPLANOWANIE SPOTKAŃ/DOSTAW ITD., ZAKLADKA Z NIEOPLACONYMI FAKTURAMI
from tkinter import *

root = Tk()
root.title('Login')
root.geometry('300x300')

username_verify = StringVar()
password_verify = StringVar()

def login_verify():
    username = username_verify.get()
    password = password_verify.get()
    login_enter.delete(0, END)
    password_enter.delete(0, END)
    users_info = {}
    with open('userInfos.txt', 'r') as file:
        for line in file:
            line = line.split()
            users_info.update({line[0]: line[1]})
    while True:
        if username not in users_info:
            not_registered = Label(root, bg='red', text='Not registered!', width=40)
            not_registered.place(x=7, y=245)
            root.after(2000, lambda: not_registered.destroy())
            login_enter.delete(0, END)
            password_enter.delete(0, END)
            return
        else:
            break
    while True:
        if password == users_info[username]:
            menu()
        else:
            incorrect_password = Label(root, bg='red', text='Incorrect password!', width=40)
            incorrect_password.place(x=7, y=245)
            root.after(2000, lambda: incorrect_password.destroy())
            login_enter.delete(0, END)
            password_enter.delete(0, END)
            return

def menu():
    root.destroy()
    import xmenu

def back_to_registration():
    root.destroy()
    import xregister

login_info = Label(root, text = 'Login:', bg='grey').place(x=20, y=29)
login_enter = Entry(root, width = 40, borderwidth = 5, textvariable= username_verify)
login_enter.place(x=20, y=50)

password_info = Label(root, text='Password:', bg='grey').place(x=20, y=99)
password_enter = Entry(root, width= 40, borderwidth= 5, show='*', textvariable= password_verify)
password_enter.place(x=20, y=120)

button_enter = Button(root, text='Log in', width=34, borderwidth= 5, command= login_verify).place(x=20, y=160)
button_back = Button(root, text='Back To Registration', width=34, borderwidth= 5, command= back_to_registration).place(x=20, y=195)

root.mainloop()