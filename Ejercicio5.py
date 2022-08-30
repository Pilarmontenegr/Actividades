# Validar Password: Desarrollar un formulario para validar password.
# Declarar un objeto password como StringVar.
# Insertar un control entry1, establecer las propiedad validate=’key’, width=10, textvariable=password, show=’*’, validatecommand=(root.register(validar), '%d', '%i', '%P', '%s', '%S').
# Insertar un button1 y establecer la propiedad text=’Validar’, command=validar_button1.
# Insertar un button2 y establecer la propiedad text=’Ver’, command=validar_button2.
# Definir la función validar_entrada.
# Limitar el ingreso a 10 caracteres.
# Permitir el ingreso de letras, números, teclas de control, !, #, $, %, &,/,(,),=,?, -, _.
# Definir la función validar_button1.
# Validar que el objeto StringVar password tenga al menos una mayúscula, una minúscula y un número.
# Si no supera las validaciones mostrará un mensaje ‘La contraseña no es válida’.
# Definir la función validar_button2.
# Si la propiedad button2['text']=='Ver', establecer entry1[show]='', y button2['text']='Ocultar'.
# La propiedad button2['text']=='Ver' es falso, establecer entry1[show]='*' y button2['text']='Ver'.

#Guía 8 - Ejercicio 5.py

import tkinter as tk
from tkinter import messagebox
from centrar_ventana import centrar

#Validar Password: Desarrollar un formulario para validar password.
def validate_entry(action, index, new_text, previous_text, text):
    print("Acción:", action)
    print("Índice (posición) en el que se quiere insertar el texto:", index)
    print("Texto si la validación es verdadera:", new_text)
    print("Contenido anterior de la caja:", previous_text)
    print("Texto que se quiere insertar:", text)

    #2 Limitar el ingreso a 10 caracteres.
    if len(previous_text) > 10 and action != '0':
        return False

    #5 Permitir el ingreso de letras, números, teclas de control, !, #, $, %, &,/,(,),=,?, -, _.
    cadena='!#$%&/()=?-_'
    if len(new_text) > 0:
        if cadena.find(new_text[-1]) == -1 and not new_text[-1].isalpha() and not new_text.isdigit() and action != '0':
            return False

    return True

#2 Insertar un botón y validar..
def validar():
    #7 Validar que el entry tenga al menos una mayúscula, una minúscula y un número.
    mayuscula = False
    minuscula = False
    numero = False
    for x in password.get():
        if x.upper == x: mayuscula == True

        if x.lower == x: minuscula == True

        if x.isdigit(): numero == True

    if not mayuscula or not minuscula or not numero:
        messagebox.showerror(title='Error', message='No cumple')
        return False

    #8 Si supera las validaciones mostrar un mensaje “La contraseña es válida”.

    #9 Insertar un botón y establecer la propiedad Name en Ver y la propiedad Text en Ver.

    #10 Cuando entry1.Text del botón sea “Ver” cambiar a “Ocultar” y la establecer la propiedad PasswordChar = “”, caso contrario cambiar  Text poner en “Ver” y PasswordChar = “*”.

    return True

root = tk.Tk()
root.geometry(centrar(ancho=300, alto=200, app=root))
root.title('Validación password')

#%d = tipo de acción (1 = insertar, 0 = eliminar, -1 para otros)
#%i = índice de cadena de caracteres para insertar / eliminar, o -1
#%P = valor de la entrada si se permite la edición.
#%s = valor de la entrada antes de la edición
#%S = la cadena de texto que se está insertando o eliminando, si hay alguna
#%v = el tipo de validación que se establece actualmente
#%V = el tipo de validación que activó la devolución de llamada
# (clave, enfoque, enfoque, forzado)
#%W = el nombre tk del widget

password=tk.StringVar()
#1 Insertar un control entry.
#2 Establecer la propiedad width en 10.
#3 Establecer la propiedad show en *.
#4 Habilitar el evento validate para el control entry.
entry=tk.Entry(root, validate="key", width=10, textvariable=password, show='*',
    validatecommand=(root.register(validate_entry), '%d', '%i', '%P', '%s', '%S'))
entry.place(x=50, y=50)
entry.focus()

#6 Insertar un botón y establecer la propiedad Name en Validar y la propiedad Text en Validar.
button=tk.Button(root, text='Ver', command=validar)
button.place(x=50,y=80)

root.mainloop()