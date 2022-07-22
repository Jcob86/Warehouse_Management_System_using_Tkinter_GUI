# PANEL LOGOWANIA, OKNO LOGIN, OKNO HASLO NA SRODKU, PRZYCISK ZALOGUJ POD TYM(JAK DA RADE TO NA ENTER), PO ZALOGOWANIU: 
# STAN MAGAZYNOWY, DODAJ PRZEDMIOTY(DOSTAWA), USUN PRZEDMIOTY(SPRZEDAZ), PRACOWNICY AKTUALNIE PRACUJACY Z DODWANIEM GODZIN ICH PRACY
# ZAPLANOWANIE SPOTKAŃ/DOSTAW ITD., ZAKLADKA Z NIEOPLACONYMI FAKTURAMI
from tkinter import *

root = Tk()
root.title('Management System')
root.geometry('280x340')

def availability():
    root.destroy()
    import xavailability

def xdelivery():
    root.destroy()
    import xdelivery

def xsold():
    root.destroy()
    import xsold

def xemployees():
    root.destroy()
    import xemployees

def xcalendar():
    root.destroy()
    import xcalendar

def bills():
    root.destroy()
    import xbills

stock_availability = Button(root, width=11, height=5,bg= 'grey', text='Stock' + '\n' + 'Availability', command= availability)
stock_availability.place(x=40, y=30)

delivery = Button(root, width=11, height=5,bg= 'grey', text='Delivery', command= xdelivery)
delivery.place(x=140, y=30)

sold = Button(root, width=11, height=5,bg= 'grey', text='Sold', command= xsold)
sold.place(x=40, y=130)

employees = Button(root, width=11, height=5,bg= 'grey', text='Employees', command= xemployees)
employees.place(x=140, y=130)

calendar = Button(root, width=11, height=5,bg= 'grey', text='Calendar', command= xcalendar)
calendar.place(x=40, y=230)

unpaid_bills = Button(root, width=11, height=5,bg= 'grey', text='Unpaid' + '\n' + 'bills', command= bills)
unpaid_bills.place(x=140, y=230)


root.mainloop()