from tkinter import *

from modulos.funcionalidad import *

def crear_botonera(self, botones, filas):
    contador = 0
    for fila in range(1,filas+1):
        for columna in range(4):
            botones[contador].grid(row=fila, column=columna, padx=5, pady=5)
            contador += 1

def colocar_boton(self, valor, color="gray80", mostrar=True, ancho=5, alto=2):
    return Button(self.ventana, text=valor, width=ancho, height=alto, font='Arial, 12', border=0, bg=color, command=lambda:pulsacion_teclas(self, valor, mostrar))
