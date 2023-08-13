from datetime import datetime 
import tkinter  as tk 
from tkcalendar import DateEntry
my_w = tk.Tk()
my_w.geometry("415x250")  
def my_upd(*args): # triggered when value of string varaible changes    
	dt=sel.get()    # collect the selected date as string    
	if(len(dt)>5):        
	dt=dt + ":"+str(hr.get())+","+ str(mn.get())+","+str(sc.get())        
	str1=datetime.strptime(dt,'%m/%d/%y:%H,%M,%S')        
	str1=str1.strftime("%d-%b-%Y : %H:%M:%S") # display format         
	l1.config(text=str1)
	sel=tk.StringVar()
	cal=DateEntry(my_w,selectmode='day',textvariable=sel)
	cal.grid(row=1,column=0,padx=1,sticky='N')
	l1=tk.Label(my_w,bg='yellow',font=('Times',28,'normal'))# show date 
	l1.grid(row=0,column=0,padx=5,columnspan=4)
	l_hr=tk.Label(my_w,text='Hour')
	l_hr.grid(row=1,column=1,sticky='N')   
	hr = tk.Scale(my_w, from_=0, to=23,    orient='vertical',length=150,command=my_upd)
	hr.grid(row=2,column=1)
	l_mn=tk.Label(my_w,text='Mintue')
	l_mn.grid(row=1,column=2,sticky='N')
	mn = tk.Scale(my_w, from_=0, to=59,    orient='vertical',length=150,command=my_upd)
	mn.grid(row=2,column=2)
	l_sc=tk.Label(my_w,text='Second')
	l_sc.grid(row=1,column=3,sticky='N')
	sc = tk.Scale(my_w, from_=0, to=59,    orient='vertical',length=150,command=my_upd)
	sc.grid(row=2,column=3)
	sel.trace('w',my_upd) # on change of string variable my_upd() # Show the date and time while openingmy_w.mainloop()

my_w.mainloop()