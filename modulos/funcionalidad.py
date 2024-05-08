from tkinter import *
import re

def pulsacion_teclas(self, valor, mostrar):
    try:
        if mostrar:
            self.operacion+=str(valor)
            mostrar_valores(self, valor)
        elif not mostrar and valor == '=':
            self.operacion = re.sub(u'\u00D7','*', self.operacion)
            self.operacion = '('+self.operacion+')'
            borrar_pantalla(self)
            if self.operacion != '()':
                mostrar_valores(self, str(eval(self.operacion)))
            else:
                self.operacion = ''
                mostrar_valores(self, self.operacion)
        elif valor == 'OFF':
            self.ventana.destroy()
        elif valor == 'C':
            borrar_pantalla(self)
            self.operacion = ''
    except SyntaxError:
        borrar_pantalla(self)
        self.operacion = ''

def mostrar_valores(self, valor):
    self.entry_display.insert(END, valor)

def borrar_pantalla(self):
    self.entry_display.delete(0, END)