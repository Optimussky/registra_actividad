#app.py
from tkinter import Tk,Button,Label,Scrollbar, Listbox, StringVar,Entry, W,E,N,S,END
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry# URL = https://www.plus2net.com/python/tkinter-DateEntry.php
from  datetime import date
from datetime import datetime
#Connecting to mysql
from db_config import dbConfig
import mysql.connector as pyo





#Instance dbConfig
con = pyo.connect(**dbConfig)
# test connection
print(con)

# Create a cursor to connect
cursor = con.cursor()


class Registrodb:
	def __init__(self):
		self.con = pyo.connect(**dbConfig)
		self.cursor = con.cursor()
		print("Connected to database successfully")
		print(con)


	def __del__(self):
		self.con.close()

	def mostrar(self):
		self.cursor.execute("SELECT r.id,r.fecha,r.area,r.asunto,t.tipo FROM registros r INNER JOIN cattipo t ON t.id=r.idtipo ORDER BY r.fecha DESC")
		rows = self.cursor.fetchall()
		return rows

	def insertar(self, fecha,area,asunto,idtipo):
		sql = ("INSERT INTO registros(fecha,area,asunto,idtipo)VALUES (%s,%s,%s,%s);")
		values = [fecha,area,asunto,idtipo]
		self.cursor.execute(sql,values)
		self.con.commit()
		messagebox.showinfo(title="Base de Registros",message="Nuevo registro agregado.")


	def editar(self,id,fecha,area,asunto,idtipo):
		try:

			tsql = 'UPDATE registros SET fecha=%s, area=%s, asunto=%s, idtipo=%s WHERE id=%s;'
			self.cursor.execute(tsql,[fecha,area,asunto,idtipo,id])
			self.con.commit()
			messagebox.showinfo(title="Base de Registros", message="Registro Actualizado.")
		except:
			pass

	def borrar(self,id):
		delquery = 'DELETE FROM registros WHERE id=%s'
		self.cursor.execute(delquery,[id])
		self.con.commit()
		messagebox.showinfo(title="Base de Registros",message="Registro Borrado.")

	

db = Registrodb()


def get_selected_row(event):
	global selected_tuple
	index = list_bx.curselection()[0]
	selected_tuple = list_bx.get(index)

	fecha_entry.delete(0,'end')
	fecha_entry.insert('end', selected_tuple[1])

	area_entry.delete(0,'end')
	area_entry.insert('end',selected_tuple[2])

	asunto_entry.delete(0,'end')
	asunto_entry.insert('end',selected_tuple[3])

	tipo_entry.delete(0,'end')
	tipo_entry.insert('end',selected_tuple[4])


def mostrar_registro():
	list_bx.delete(0,'end')
	for row in db.mostrar():
		list_bx.insert('end',row)


def insertar_registro():
	#default_text = fecha_text.get_date()
	#print(default_text[0])
	db.insertar(fecha_text.get(),area_text.get(),asunto_text.get(),tipo_text.get())
	list_bx.delete(0,'end')
	list_bx.insert('end',(fecha_text.get(),area_text.get(),asunto_text.get(),tipo_text.get()))
	#fecha_entry.delete(0,'end')
	area_entry.delete(0,'end')
	asunto_entry.delete(0,'end')
	tipo_entry.delete(0,'end')
	con.commit()



def borrar_registro():
	db.borrar(selected_tuple[0])
	con.commit()
	mostrar_registro()


def limpiar_registro():
	list_bx.delete(0,'end')
	fecha_entry.delete(0,'end')
	area_entry.delete(0,'end')
	asunto_entry.delete(0,'end')
	tipo_entry.delete(0,'end')


def editar_registro():
	db.editar(selected_tuple[0],fecha_text.get(), area_text.get(), asunto_text.get(), tipo_text.get())
	fecha_entry.delete(0,'end')
	area_entry.delete(0,'end')
	asunto_entry.delete(0,'end')
	tipo_entry.delete(0,'end')
	con.commit()

def salir():
	dd = db
	if messagebox.askokcancel("Cerrar", "¿Desea salir de la Aplicación?"):
		root.destroy()
		del dd


# START APP
root = Tk()
root.title("Register Database Application")
root.configure(background="navy blue")
root.geometry("1100x600")
root.resizable(width=False,height=False)



def getdate():
	"""Obtiene la fecha a través de fecha_text y ocupa con x.get_date() """
	if(fecha_text.get()!=''):
		fecha_entry.get_date()
		print(fecha_entry.get_date())
	else:
		fecha_entry.set_date(datetime.datetime.now())#datetime.date.min
		print(fecha_entry.get_date())

# START LABELS
	#FECHA
fecha_label = ttk.Label(root,text="Fecha:",background="navy blue",font=("TkDefaultFont",16),foreground="gray")
fecha_label.grid(row=0,column=0,sticky=W)
#fecha=datetime.utcnow

fecha_text = StringVar()
fecha_entry=DateEntry(root,textvariable=fecha_text,selectmode='day',year=2023,date_pattern="yyyy-mm-dd")
fecha_entry.grid(row=0,column=1, pady=40, padx=5,sticky=W)
#lambda: getdate()



	#AREA	
area_label = ttk.Label(root, text="Area", background="navy blue",font=("TkDefaultFont",14),foreground="gray")
area_label.grid(row=0, column=2, sticky=W)
area_text = StringVar()
area_entry =ttk.Entry(root, width=24, textvariable=area_text)
area_entry.grid(row=0, column=3,padx=5, sticky=W)

	#ASUNTO
asunto_label = ttk.Label(root,text="Asunto",background="navy blue", font=("TkDefaultFont",14),foreground="gray")
asunto_label.grid(row=0,column=4, sticky=W)
asunto_text = StringVar()
asunto_entry = ttk.Entry(root, width=24, textvariable=asunto_text)
asunto_entry.grid(row=0, column=5,padx=5, sticky=W)

	#TIPO
tipo_label = ttk.Label(root, text="Tipo",background="navy blue", font=("TkDefaultFont",14),foreground="gray")
tipo_label.grid(row=0, column=6,sticky=W)
tipo_text = StringVar()
tipo_entry= ttk.Entry(root, width=24,textvariable=tipo_text)
tipo_entry.grid(row=0, column=7,padx=5, sticky=W)

#START BUTTONS
	#REGISTRO
add_btn = Button(root, text="+ Registro", bg="light green",fg="white",font="helvetica 10 bold", command=insertar_registro)
add_btn.grid(row=0, column=8,padx=5, sticky=W)

#START LISTBOX
list_bx = Listbox(root,height=16, width=40,font="helvetica 13", bg="gray")
list_bx.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40,padx=15)

# Define binds
list_bx.bind('<<ListboxSelect>>',get_selected_row)

#START SCROLLBAR
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=9, rowspan=14, sticky=W)

	# START CONFIGURE LISTBOX DIRECTION
list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)

#START BUTTON 
	#VER
ver_btn = Button(root, text="Ver Registros", bg="white",fg="black", font="helvetica 9 bold",command=mostrar_registro)
ver_btn.grid(row=15, column=1)
	
	#LIMPIAR REGISTROS
reset_btn = Button(root, text="Limpiar Registros", bg="orange",fg="blue", font="helvetica 9 bold",command=limpiar_registro)
reset_btn.grid(row=15, column=2)
	
	#EDITAR REGISTRO
editar_btn = Button(root, text="Editar Registro", bg="purple",fg="white", font="helvetica 9 bold",command=editar_registro)
editar_btn.grid(row=15, column=3)

	#BORRAR REGISTRO
borrar_btn = Button(root, text="Borrar Registro", bg="yellow",fg="black", font="helvetica 9 bold",command=borrar_registro)
borrar_btn.grid(row=15, column=4)

	#SALIR
salir_btn = Button(root, text="Salir de sisema", bg="gray",fg="white", font="helvetica 9 bold",command=salir)#command=root.destroy
salir_btn.grid(row=15, column=5)

#END MAIN
root.mainloop()