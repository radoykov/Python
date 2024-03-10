from tkinter import *
from tkinter import ttk
from math import sqrt

def calculate(*args):
    try:
        A = float(a.get())
        B = float(b.get())
        C = float(c.get())


        result_1.set(f"{sqrt(A + B + C):.4f}")  
        result_2.set(f"{(A + B + C) / 3:.4f}") 

    except ValueError:
        pass

root = Tk()
root.title("Quadratic Equation")

mainframe = ttk.Frame(root, padding="3 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

a = StringVar()
a_entry = ttk.Entry(mainframe, width=7, textvariable=a)
a_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(mainframe, text="A: ").grid(column=1, row=1, sticky=W)

b = StringVar()
b_entry = ttk.Entry(mainframe, width=7, textvariable=b)
b_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="B: ").grid(column=1, row=2, sticky=W)

c = StringVar()
c_entry = ttk.Entry(mainframe, width=7, textvariable=c)
c_entry.grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="C: ").grid(column=1, row=3, sticky=W)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=4, row=3, sticky=W)


result_1 = StringVar()
result_2 = StringVar()
ttk.Label(mainframe, text="Sqare:").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, textvariable=result_1).grid(column=2, row=4, sticky=(W, E))

ttk.Label(mainframe, text="Average:").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, textvariable=result_2).grid(column=2, row=5, sticky=(W, E))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

a_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()