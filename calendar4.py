import tkinter  as tk 
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta
#import relativedelta
from datetime import date, datetime


my_w = tk.Tk()
my_w.geometry("400x420") # width and height of window   
font1=['Times',56,'normal'] # font style to display output 

l1=tk.Label(my_w,text='data',bg='yellow',font=font1)  # display difference 
l1.grid(row=0,column=0,padx=10,pady=20,columnspan=3,sticky='ew')

cal1=DateEntry(my_w,selectmode='day')
cal1.grid(row=1,column=0,padx=20,pady=30)
cal2=DateEntry(my_w,selectmode='day')
cal2.grid(row=1,column=1,padx=20,pady=30)

b1=tk.Button(my_w,text='Diff in Days', bg='lightgreen',
        font=20,command=lambda:my_upd())
b1.grid(row=1,column=2)
def my_upd(): # triggered on Button Click
    diff_days=(cal2.get_date()-cal1.get_date()).days # difference in days 
    #print(diff_days)
    l1.config(text=str(diff_days)+' days') # read and display date

my_w.mainloop()