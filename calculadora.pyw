from tkinter import *

from modulos.botonera import *

root = Tk()

class Calculadora():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Calculadora')
        self.ventana.config(bg='gray12')
        self.ventana.resizable(0,0)
        self.operacion = ''

        #------Display------#
        self.entry_display = Entry(self.ventana)
        self.entry_display.grid(row=0,column=0, pady=20, columnspan=4)
        self.entry_display.config(fg="white", bg="gray12", width=12, border=0, font="Arial, 25", justify="right")

        #------Botones------#
        #fila1
        boton_borrar = colocar_boton(self, 'C', mostrar=False, color='orange')
        boton_cuadrado = colocar_boton(self, '(', color='cyan')
        boton_raiz = colocar_boton(self, ')', color='cyan')
        boton_dividir = colocar_boton(self, '/', color='gray50')
        
        #fila2
        boton_siete = colocar_boton(self, 7)
        boton_ocho = colocar_boton(self, 8)
        boton_nueve = colocar_boton(self, 9)
        boton_multiplicar = colocar_boton(self, u'\u00D7', color='gray50')
        
        #fila3
        boton_cuatro = colocar_boton(self, 4)
        boton_cinco = colocar_boton(self, 5)
        boton_seis = colocar_boton(self, 6)
        boton_restar = colocar_boton(self, '-', color='gray50')
        
        # fila4
        boton_uno = colocar_boton(self, 1)
        boton_dos = colocar_boton(self, 2)
        boton_tres = colocar_boton(self, 3)
        boton_sumar = colocar_boton(self, '+', color='gray50')
        
        #fila5
        boton_apagar = colocar_boton(self, 'OFF', mostrar=False, color='red')
        boton_cero = colocar_boton(self, 0)
        boton_coma = colocar_boton(self, '.', color='gray50')
        boton_igual = colocar_boton(self, '=', mostrar=False, color='green')

        botones = [boton_borrar, boton_cuadrado, boton_raiz, boton_dividir, boton_siete, boton_ocho, boton_nueve, boton_multiplicar, boton_cuatro, boton_cinco, boton_seis, boton_restar, boton_uno, boton_dos, boton_tres, boton_sumar, boton_apagar, boton_cero, boton_coma, boton_igual]

        crear_botonera(self, botones, 5)


calculadora = Calculadora(root)

root.mainloop()