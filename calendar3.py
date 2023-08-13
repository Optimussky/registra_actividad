from tkinter import *
from tkinter.ttk import *
from tkcalendar import DateEntry
import datetime

root = Tk()
root.geometry("500x200")

def getdate():
    if(doc_value.get()!=''):
        fecha_doc_cal.get_date()
        print(fecha_doc_cal.get_date())
    else:
        fecha_doc_cal.set_date(datetime.datetime.now())#datetime.date.min
        print(fecha_doc_cal.get_date())
    
    #Testing different date formats
    """
    if(doc_value.get()==''):
        fecha_doc_cal.set_date(datetime.datetime.now())
        print(fecha_doc_cal.get_date())
        return 0
    """

doc_value = StringVar()

#doc_en = Entry(root, textvariable=doc_value)
#doc_en.grid(row=12, column=4, padx=10, pady=5)

fecha_doc_cal = DateEntry(root,textvariable=doc_value,width=17,bg="darkblue",fg="white",year=2023)
fecha_doc_cal._set_text("Choose a Date")
fecha_doc_cal.grid(row=12, column=5, padx=10, pady=5)

send = Button(root, text="Send", command=getdate)
send.grid(row=18, column=0, padx=10, pady=5)

root.mainloop()