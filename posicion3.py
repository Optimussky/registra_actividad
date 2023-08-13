#posicion3.py
#usando clases con el codigo de posicion1.py

#posicion.py
""" Ejemplo de uso de place para posicionar elementos en la ventana
"""
from tkinter import Tk,Label,Button, Entry, Frame, Messabox


## Creando la clase

class MyVentana(Frame):

	def __init__(self, master=None):
		super().__init__(master, width=320,height=170)
		self.master = master
		self.pack()
		self.create_widgets()

	def fnSuma(self):
		try:
			n1 = self.txt1_entry.get()
			n2 = self.txt2_entry.get()
			r = float(n1) + float(n2)
			self.txt3_entry.delete(0,'end')
			self.txt3_entry.insert(0,r)
		except:
			f"Introduzca datos validos"


	def create_widgets(self):
		# Labels
		self.label1 = Label(self, text="Primer número", bg="yellow")
		self.label1.place(x=10,y=10,width=100,height=30)
		# Entry
		self.txt1_entry = Entry(self, bg="orange")
		self.txt1_entry.place(x=120,y=10, width=100, height=30)
		# Labels
		self.label1 = Label(self, text="Segundo número", bg="yellow")
		self.label1.place(x=10,y=50,width=100,height=30)
		# Entry
		self.txt2_entry = Entry(self, bg="orange")
		self.txt2_entry.place(x=120,y=50, width=100, height=30)
		# Buttons
		self.btn1 = Button(self,text="Sumar",command=self.fnSuma)
		self.btn1.place(x=230, y=50, width=80,height=30)
		# Labels
		self.label1 = Label(self, text="Resultado número", bg="yellow")
		self.label1.place(x=10,y=120,width=100,height=30)
		# Entry
		self.txt3_entry = Entry(self, bg="orange")
		self.txt3_entry.place(x=120,y=120, width=100, height=30)








root = Tk()
root.wm_title("App para Sumar")
app = MyVentana(master=root)

app.mainloop()