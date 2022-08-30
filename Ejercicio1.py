#Guía 8 - Ejercicio 1.py

#Validar Entero: Desarrollar un formulario para validar un importe entero de 7 dígitos.
#1 Utilizar un control entry.
#2 Permitir solo el ingreso de números y teclas de control.
#3 Limitar el tamaño en caracteres a 12.
#4 Insertar un control Button.
#5 Asignar un texto a text.
#6 Asignar una función a command.
#7 Validar que el entry contenga un valor mayor a 0 y menor o igual a 9999999.

import tkinter as tk
from centrar_ventana import centrar

def validar_teclas(accion, texto_previo, nuevo_texto, texto):
    print('1 Acción', accion)
    print('2 Texto previo', texto_previo)
    print('3 Texto que se está ingresando', nuevo_texto)
    print('4 Texto si el resultado es True', texto, '\n')

    if not nuevo_texto.isdigit():
        return False

    if len(texto) > 7:
        return False

    return True

#Se instancia la clase Tk, ahora root es un objeto de la clase Tk.
root = tk.Tk()
# Se define el tamaño de la ventana llamando la función centrar.
root.geometry(centrar(ancho=300, alto=200, app=root))
#root.geometry('300x200+900+800')
# Se le asigna un título a la ventana.
root.title('Validación entero')

label = tk.Label(root, text='Ingrese un valor entero:')
#label.pack()
#label.place(x=0, y=0, width=300, height=30)
label.grid(column=0, row=0, padx=10, pady=10)

entry = tk.Entry(root, width=7, validate='key')
#entry.pack()
#entry.place(x=50, y=50)
entry.grid(column=1, row=0, padx=10, pady=10)

#entry = tk.Entry(root, validate='key')
# Asocio la función validar_tecla a la propiedad validate.
entry['validatecommand'] = (entry.register(validar_teclas), '%d',  '%s', '%S', '%P')
# %d = Type of action (1=insert, 0=delete, -1 for others)
# %i = index of char string to be inserted/deleted, or -1
# %P = value of the entry if the edit is allowed.
# %s = value of entry prior to editing
# %S = the text string being inserted or deleted, if any
# %v = the type of validation that is currently set
# %V = the type of validation that triggered the callback
#      (key, focusin, focusout, forced)
# %W = the tk name of the widget

root.mainloop()