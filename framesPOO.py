#framesPOO.py
#import tkinter as tk
from tkinter import Tk,Frame,Button,Label

class Application(Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		self.print_labels()

	def create_widgets(self):
		self.hi_there = Button(self)
		self.hi_there["text"] = "Hello World\n (click me)"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")

		self.quit = Button(self, text="QUIT", fg="red",
							command=self.master.destroy)
		self.quit.pack(side="bottom")

	def print_labels(self):
		self.show_here = Label(self)
		self.show_here["text"] = "Introduce algo: "
		self.show_here.pack()



	def say_hi(self):
		print("Hi there, everyone!")

root = Tk()
app = Application(master=root)

app.mainloop()