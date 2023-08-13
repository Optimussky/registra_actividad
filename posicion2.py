#posicion.py
""" Ejemplo de uso de place usando relx rely relwidth, rerlheight
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
label1.place(relx=0.03,rely=0.02, relwidth=0.2, relheight=0.1)
# Entry
txt1_entry = Entry(root, bg="orange")
txt1_entry.place(relx=0.3,rely=0.03, relwidth=0.22, relheight=0.1)
# Labels
label2 = Label(root, text="Segundo número", bg="yellow")
label2.place(relx=0.03,rely=0.17,relwidth=0.23,relheight=0.1)
# Entry
txt2_entry = Entry(root, bg="orange")
txt2_entry.place(relx=0.3,rely=0.17, relwidth=0.22, relheight=0.1)
# Buttons
btn1 = Button(root,text="Sumar",command=fnSuma)
btn1.place(relx=0.55, rely=0.17, relwidth=0.20,relheight=0.1)
# Labels
label3 = Label(root, text="Resultado número", bg="yellow")
label3.place(relx=0.03,rely=0.35,relwidth=0.23,relheight=0.1)
# Entry
txt3_entry = Entry(root, bg="orange")
txt3_entry.place(relx=0.3,rely=0.35, relwidth=0.22, relheight=0.1)









root.mainloop()