#!/usr/bin/env python
from Tkinter import *

def funcion():
   v.set("Hola")

frame = Frame()
button=Button(frame, text="hola", command=funcion)
button.pack(side=LEFT)

v = StringVar()
text = Entry(frame, textvariable=v )
text.pack(side=LEFT);

frame.pack()
frame.mainloop()