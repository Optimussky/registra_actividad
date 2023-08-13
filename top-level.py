#top-level.py
from tkinter import Tk,Label,Button, Toplevel
import tkinter as tk
from os import system




def hide_window():
	try:
		top_level.withdraw() # hide the top level window
	except:
		pass

def sistema():
	algo = system('ipconfig /all|FINDSTR "10.13."')
	l =label2.grid()
	return l,algo



def show_window():
	try:

		top_level.deiconify()#  show the top leven window again
		top_level.geometry("400x300")
		label1.grid()
		sistema()
	except:
		pass


root = Tk()
root.geometry("400x300")
root.title("The Principal")

#crete top level window
top_level = Toplevel(root)

top_level.title("Top Level Window")
label1 = Label(top_level,text="Surprise!")
label2 = Label(top_level,command=sistema(label))

#add a button to the main window
button = Button(root, text="Hide Window",command=hide_window)
button.pack(pady=20)

# add button to show the top level window again
show_button = Button(root, text="Show Window",command=show_window)
show_button.pack(pady=20)


root.mainloop()