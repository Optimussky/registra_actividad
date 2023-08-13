import tkinter  as tk 
from tkcalendar import DateEntry
from  datetime import date


my_w = tk.Tk()
my_w.geometry("380x220")  
cal=DateEntry(my_w,selectmode='day')
cal.grid(row=1,column=1,padx=15)
dt=date(2021,8,19) # specific date Year, month , daycal.set_date(dt) 
# Set the selected date #cal.set_date('8/16/2021') 
# Set the local calendar format my_w.mainloop()


sel=tk.StringVar() # declaring string variable 
cal=DateEntry(my_w,selectmode='day',textvariable=sel)
cal.grid(row=1,column=1,padx=20)
def my_upd(*args): # triggered when value of string varaible changes    l1.config(text=sel.get()) # read and display datel1=tk.Label(my_w,bg='yellow')  # Label to display date l1.grid(row=1,column=2)
	sel.trace('w',my_upd) # on change of string variable my_w.mainloop()


my_w.mainloop()