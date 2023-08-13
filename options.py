#options.py

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#597678')

def check(*args):
    print(f"the variable has changed to '{variable.get()}'")

variable = StringVar(value='United States')
variable.trace('w', check)


# choices available with user.
countries = ['Bahamas','Canada', 'Cuba', 'Dominica', 'Jamaica', 'Mexico', 'United States']

# set default country as United States
variable.set(countries[6])

#  creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *countries
)
# positioning widget
dropdown.pack(expand=True)

# infinite loop 
ws.mainloop()