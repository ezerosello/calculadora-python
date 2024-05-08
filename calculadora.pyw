from tkinter import *
import re

root = Tk()

class Calculadora():
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('Calculadora')
        self.ventana.config(bg='gray12')
        self.ventana.resizable(0,0)
        self.operacion = ''

        #Display

        self.entry_display = Entry(self.ventana)
        self.entry_display.grid(row=0,column=0, pady=20, columnspan=4)
        self.entry_display.config(fg="white", bg="gray12", width=12, border=0, font="Arial, 25", justify="right")

        #Botones
        boton_borrar = self.colocar_boton('C', mostrar=False, color='orange')
        boton_cuadrado = self.colocar_boton('(', color='cyan')
        boton_raiz = self.colocar_boton(')', color='cyan')
        boton_dividir = self.colocar_boton('/', color='gray50')
        
        boton_siete = self.colocar_boton(7)
        boton_ocho = self.colocar_boton(8)
        boton_nueve = self.colocar_boton(9)
        boton_multiplicar = self.colocar_boton(u'\u00D7', color='gray50')
        
        boton_cuatro = self.colocar_boton(4)
        boton_cinco = self.colocar_boton(5)
        boton_seis = self.colocar_boton(6)
        boton_restar = self.colocar_boton('-', color='gray50')
        
        boton_uno = self.colocar_boton(1)
        boton_dos = self.colocar_boton(2)
        boton_tres = self.colocar_boton(3)
        boton_sumar = self.colocar_boton('+', color='gray50')
        
        boton_apagar = self.colocar_boton('OFF', mostrar=False, color='red')
        boton_cero = self.colocar_boton(0)
        boton_coma = self.colocar_boton('.', color='gray50')
        boton_igual = self.colocar_boton('=', mostrar=False, color='green')

        botones = [boton_borrar, boton_cuadrado, boton_raiz, boton_dividir, boton_siete, boton_ocho, boton_nueve, boton_multiplicar, boton_cuatro, boton_cinco, boton_seis, boton_restar, boton_uno, boton_dos, boton_tres, boton_sumar, boton_apagar, boton_cero, boton_coma, boton_igual]

        contador = 0

        for fila in range(1,6):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna, padx=5, pady=5)
                contador += 1

    def colocar_boton(self, valor, color="gray80", mostrar=True, ancho=5, alto=2):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font='Arial, 12', border=0, bg=color, command=lambda:self.pulsacion_teclas(valor, mostrar))

    def pulsacion_teclas(self, valor, mostrar):
            try:
                if mostrar:
                    self.operacion+=str(valor)
                    self.mostrar_valores(valor)
                elif not mostrar and valor == '=':
                    self.operacion = re.sub(u'\u00D7','*', self.operacion)
                    self.operacion = '('+self.operacion+')'
                    self.borrar_pantalla()
                    if self.operacion != '()':
                        self.mostrar_valores(str(eval(self.operacion)))
                    else:
                        self.operacion = ''
                        self.mostrar_valores(self.operacion)
                elif valor == 'OFF':
                    self.ventana.destroy()
                elif valor == 'C':
                    self.borrar_pantalla()
                    self.operacion = ''
            except SyntaxError:
                self.borrar_pantalla()
                self.operacion = ''

    def mostrar_valores(self, valor):
        self.entry_display.insert(END, valor)

    def borrar_pantalla(self):
        self.entry_display.delete(0, END)

calculadora = Calculadora(root)

root.mainloop()