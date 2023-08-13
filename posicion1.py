#posicion.py
""" Ejemplo de uso de place para posicionar elementos en la ventana
"""
from tkinter import Tk,Label,Button, Entry

root = Tk()

def fnSuma():
	n1 = txt1_entry.get()
	n2 = txt2_entry.get()
	r = float(n1) + float(n2)
	txt3_entry.delete(0,'end')
	txt3_entry.insert(0,r)



#propiedades al main	
root.title("Ejemplo de place")
root.geometry("400x200")
# Labels
label1 = Label(root, text="Primer número", bg="yellow")
label1.place(x=10,y=10,width=100,height=30)
# Entry
txt1_entry = Entry(root, bg="orange")
txt1_entry.place(x=120,y=10, width=100, height=30)
# Labels
label1 = Label(root, text="Segundo número", bg="yellow")
label1.place(x=10,y=50,width=100,height=30)
# Entry
txt2_entry = Entry(root, bg="orange")
txt2_entry.place(x=120,y=50, width=100, height=30)
# Buttons
btn1 = Button(root,text="Sumar",command=fnSuma)
btn1.place(x=230, y=50, width=80,height=30)
# Labels
label1 = Label(root, text="Resultado número", bg="yellow")
label1.place(x=10,y=120,width=100,height=30)
# Entry
txt3_entry = Entry(root, bg="orange")
txt3_entry.place(x=120,y=120, width=100, height=30)









root.mainloop()