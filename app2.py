#app2.py
from ttkbootstrap import *#pipenv install ttkbootstrap
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.dialogs import Messagebox


class Intefaz(Window):
	def __init__(self,):
		super().__init__(size=(900,500),title="Interfaz Moderna")
		self.widgets()

	def entry_label(self,frame,x,y,text):
		lbl = Label(frame,text=text, bootstyle= PRIMARY)
		lbl.place(x=x,y=y)
		entry = Entry(frame,bootstyle= (PRIMARY))
		entry.place(x=x+100,y=y)
		return entry

	def validaciones(self,fecha,area,asunto,tipo):
		pass
		#if len(fecha) != '':


	def guardar(self):
		fecha = self.fecha.get()
		area = self.area.get()
		asunto = self.asunto.get()
		tipo = self.tipo.get()

		if len(fecha)=='':
			return Messagebox.show_error(title="Error", message="Debes introducir una fecha con formato "Y-m-d",alert=True)
				

	def widgets(self):
		frame = Frame(self)
		frame.pack(side = TOP, fill = BOTH,expand=True)
		frame1 = Frame(frame,bootstyle= INFO)
		frame1.place(x=5,y=0,width=290, height=490)
		lblframe1 = Labelframe(frame1,text="Formulario",bootstyle=PRIMARY)
		lblframe1.pack(side= TOP,fill=BOTH, expand=True)

		#Formulario
		self.fecha = self.entry_label(lblframe1,5,0,"Fecha")
		self.area = self.entry_label(lblframe1,5,40,"Area")
		self.asunto = self.entry_label(lblframe1,5,80,"Asunto")
		self.tipo = self.entry_label(lblframe1,5,120,"Tipo")

		btnguardar = Button(lblframe1, text="Guardar",command="/")
		btnguardar.place(x=105,y=160,width=135)

		frame2 = Frame(frame,bootstyle=DANGER)
		frame2.place(x=300, y=0, height=490,width=590)
		lblframe2 = Labelframe(frame2, text="Datos", bootstyle= SUCCESS)
		lblframe2.pack(side = TOP, fill= BOTH,expand=True)
		# TableView
		coldata = [
			{"text":"ID","stretch":True},
			"Fecha",
			"Area",
			"Asunto",
			{"text":"Tipo","stretch":True},
		]
		tableview = Tableview(
			lblframe2,
			paginated=True,
			searchable=True,
			bootstyle=(SUCCESS),
			stripecolor=("cyan",None),
			autoalign=True,
			autofit=True,
			height=15,
			delimiter=";" )
		tableview.pack(fill=BOTH, expand=True, padx=5, pady=5)
		tableview.build_table_data(coldata,[])




# main
if __name__ == "__main__":
	app = Intefaz()
	app.mainloop()
