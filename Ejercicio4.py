# Validar Nombre: Desarrollar un formulario para validar nombres, quitando los blancos de los extremos, no permitir blancos consecutivos, poner en mayúscula la primera letra de cada nombre y el resto en minúscula.
#1- Insertar un control entry.
# Limitar el ingreso a 50 caracteres.
# Permitir solo el ingreso de letras, espacios en blanco o caracteres de control.
# No permitir ingresar blancos consecutivos, es decir solo uno a la vez.
#2- Insertar un botón y validar..
# No debe terminar ni comenzar con blanco.
# Poner con mayúscula la primera letra de cada palabra y el resto en minúsculas.

#Guía 8 - Ejercicio 4.py
# Validar Nombre: Desarrollar un formulario para validar nombres,
# quitando los blancos de los extremos, no permitir blancos consecutivos,
# poner en mayúscula la primera letra de cada nombre y el resto en minúscula.

import tkinter as tk
from centrar_ventana import centrar

#1 Insertar un control entry.
def validate_entry(action, index, new_text, previous_text, text):
    print("Acción:", action)
    print("Índice (posición) en el que se quiere insertar el texto:", index)
    print("Texto si la validación es verdadera:", new_text)
    print("Contenido anterior de la caja:", previous_text)
    print("Texto que se quiere insertar:", text)

    #1.a Limitar el ingreso a 50 caracteres.
    if len(previous_text) > 35 and action != '0':
        return False

    #1.b Permitir solo el ingreso de letras, espacios en blanco o caracteres de control.
    if len(previous_text) > 0:
        if not new_text[-1].isalpha() and not new_text[-1].isspace() and action != '0':
            return False

    #1.c No permitir ingresar blancos consecutivos, es decir solo uno a la vez.
    if len(previous_text) > 0 and action != '0':
        #if previous_text[int(index) - 1: int(index) :1].isspace() and new_text[-1].isspace():
        if previous_text[-1].isspace() and new_text[-1].isspace():
            return False

    #1.d No permitir ingresar blancos al principio.
    if index == '0' and action != '0' and new_text[-1].isspace():
        return False

    return True

#2 Insertar un botón y validar..
def validar():
    #2.a No debe terminar ni comenzar con blanco.
    nombre.set(nombre.get().strip())

    #2.b Poner con mayúscula la primera letra de cada palabra y el resto en minúsculas.
    nombre.set(' '.join(x.capitalize() for x in nombre.get().split()))

    return True

root = tk.Tk()
root.geometry(centrar(ancho=300, alto=200, app=root))
root.title('Validación nombre')

#%d = tipo de acción (1 = insertar, 0 = eliminar, -1 para otros)
#%i = índice de cadena de caracteres para insertar / eliminar, o -1
#%P = valor de la entrada si se permite la edición.
#%s = valor de la entrada antes de la edición
#%S = la cadena de texto que se está insertando o eliminando, si hay alguna
#%v = el tipo de validación que se establece actualmente
#%V = el tipo de validación que activó la devolución de llamada
# (clave, enfoque, enfoque, forzado)
#%W = el nombre tk del widget

nombre=tk.StringVar()
entry=tk.Entry(root, validate="key", width=30, textvariable=nombre,
    validatecommand=(root.register(validate_entry), '%d', '%i', '%P', '%s', '%S'))
entry.place(x=50, y=50)
entry.focus()

button=tk.Button(root, text='Validar', command=validar)
button.place(x=50,y=80)

root.mainloop()