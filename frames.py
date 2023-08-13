#frames.py
from tkinter import Button, Frame,Label, Tk

root = Tk()

def frame(root):
	root.title("Ejemplo con Frames")
	root.geometry("200x70")

	frame1 = Frame(root, bg="blue")
	frame1.pack(expand=True,fill='both')

	frame2 = Frame(root, bg="yellow")
	frame2.pack(expand=True,fill="both")
	frame2.config(cursor='pirate')

	redbutton = Button(frame1, text="red" ,fg="red")
	greenbutton = Button(frame1, text="green" ,fg="green")
	bluebutton = Button(frame1, text="blue" ,fg="blue")

	redbutton.place(relx=.05, rely=.05, relwidth=.25, relheight=.9)
	greenbutton.place(relx=.35, rely=.05, relwidth=.25, relheight=.9)
	bluebutton.place(relx=.65, rely=.05, relwidth=.25, relheight=.9)

	blackbutton = Button(frame2, text="Black", fg="black")
	blackbutton.pack()

	"""
			w = Frame ( master, option, ...)

	w.config(bg="blue") # color de fondo
	w.config(cursor="pirate") # tipo de cursor
	w.config(relief="sunken") # relieve del frame
	w.config(bd=23) # tramaño del borde en pixeles

	option = {
	Cambiar tamaño 			 :	mi_Frame.config(width="200",heigth="200")	
	Cambiar color de fondo	 :	mi_Frame.config(bg="blue")
	Cambiar grosor del borde :	mi_Frame.config(bd=24)
	Cambiar el tipo de bordo :	mi_Frame.config(relief="sunken")
	Cambiar el cursor 		 :	mi_Frame.config(cursor="heart")
	}

	"""

if __name__ == '__main__':
	frame(root)
	root.mainloop()