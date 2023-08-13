#top-level.py
from tkinter import *
import tkinter as tk
from os import system

### Crear una clase Ventana
class Ventana:
	## variables de clase
	tipo = tk.Tk()
	## constructor
	def __init__(self,tipo,size,title):
		#self.tipo = tk.Tk()
		self.tipo = tipo
		self.size = size
		self.titulo = title


## Crear objetos de clase de tipo ventana

v1 = Ventana('principal',"500x300","")


tipo.mainloop()