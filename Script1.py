from Tkinter import *
 
def flecha_mouse(evento):     
 
        cadena['text'] = "Se detecto un clic en X = "+str(evento.x)+" Y = "+str(evento.y) 
 
ventana = Tk() 
 
ventana.minsize(400,350)
 
cuadro = Frame(ventana, width =400, height =300, bg="red") 
 
cuadro.bind("<Button-1>", flecha_mouse) 
 
cuadro.pack() 
 
cadena = Label(ventana) 
 
cadena.pack() 
 
ventana.mainloop()