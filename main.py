from tkinter import *
from funcionesBotones import *
from funcionesMatematicas import *

root = Tk()
root.config(bg="gray16")

root.resizable(0,0)


# Display

frameDisplay = Frame(root)
frameDisplay.grid(row=0, column=0, padx=7, pady=10)
frameDisplay.config(bg="gray12")

stringDisplay = StringVar()

entryDisplay = Entry(frameDisplay, textvariable=stringDisplay)
entryDisplay.grid(row=0,column=0, pady=20)
entryDisplay.config(fg="white", bg="gray12", border=0, font="Arial, 25", justify="center")


# Botonera

frameBotonera = Frame(root)
frameBotonera.grid(row=1, column=0)
frameBotonera.config(width=302, height=300, bg="gray16")

    # Primera fila de botones

botonBorrado = Button(frameBotonera, text="Borrar", width=7)
botonBorrado.grid(row=0, column=0, padx=20, pady=15)
botonBorrado.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

botonExponente = Button(frameBotonera, text="x²", width=7, command=botonCuadrado)  
botonExponente.grid(row=0, column=1, padx=20, pady=15)
botonExponente.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

botonRaizCuadrada = Button(frameBotonera, text="√x", width=7)
botonRaizCuadrada.grid(row=0, column=2, padx=20, pady=15)
botonRaizCuadrada.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

botonDivision = Button(frameBotonera, text="÷", width=7)
botonDivision.grid(row=0, column=3, padx=20, pady=15)
botonDivision.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

    # Segunda fila de botones

boton7 = Button(frameBotonera, text="7", width=7)
boton7.grid(row=1, column=0, padx=20, pady=15)
boton7.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

boton8 = Button(frameBotonera, text="8", width=7)  
boton8.grid(row=1, column=1, padx=20, pady=15)
boton8.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

boton9 = Button(frameBotonera, text="9", width=7)
boton9.grid(row=1, column=2, padx=20, pady=15)
boton9.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

botonMultiplicacion = Button(frameBotonera, text="x", width=7)
botonMultiplicacion.grid(row=1, column=3, padx=20, pady=15)
botonMultiplicacion.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

    # Tercera fila de botones

boton4 = Button(frameBotonera, text="4", width=7)
boton4.grid(row=2, column=0, padx=20, pady=15)
boton4.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

boton5 = Button(frameBotonera, text="5", width=7)  
boton5.grid(row=2, column=1, padx=20, pady=15)
boton5.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

boton6 = Button(frameBotonera, text="6", width=7)
boton6.grid(row=2, column=2, padx=20, pady=15)
boton6.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

botonResta = Button(frameBotonera, text="-", width=7)
botonResta.grid(row=2, column=3, padx=20, pady=15)
botonResta.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

    # Cuarta fila de botones

boton1 = Button(frameBotonera, text="1", width=7)
boton1.grid(row=3, column=0, padx=20, pady=15)
boton1.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

boton2 = Button(frameBotonera, text="2", width=7)  
boton2.grid(row=3, column=1, padx=20, pady=15)
boton2.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")
 
boton3 = Button(frameBotonera, text="3", width=7)
boton3.grid(row=3, column=2, padx=20, pady=15)
boton3.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

botonSuma = Button(frameBotonera, text="+", width=7)
botonSuma.grid(row=3, column=3, padx=20, pady=15)
botonSuma.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

    # Quinta fila de botones

boton3coma14 = Button(frameBotonera, text="π", width=7)
boton3coma14.grid(row=4, column=0, padx=20, pady=15)
boton3coma14.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

boton0 = Button(frameBotonera, text="0", width=7)  
boton0.grid(row=4, column=1, padx=20, pady=15)
boton0.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

botonFloat = Button(frameBotonera, text=",", width=7)
botonFloat.grid(row=4, column=2, padx=20, pady=15)
botonFloat.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

botonIgualar = Button(frameBotonera, text="=", width=7)
botonIgualar.grid(row=4, column=3, padx=20, pady=15)
botonIgualar.config(width=5, height=2, font='arialblack, 10', border=0, bg="gray80")

mainloop()