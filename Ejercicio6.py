# Validar Fecha: Desarrollar un formulario para validar una fecha.
# Declarar un objeto fecha como StringVar para asociar al entry1.
# Insertar un control entry1, establecer las propiedad validate=’key’, width=10, textvariable=fecha, validatecommand=(root.register(validar_entry1), '%d', '%i', '%P', '%s', '%S').
# Insertar un button1 y establecer la propiedad text=’Validar’, command=validar_button1.
# Definir la función validar_entry1.
# Limitar el ingreso a 10 caracteres.
# Permitir el ingreso de números y guión medio en su respectiva posición.
# Definir la función validar_button1.
# Utilizando rebanado de cadenas, obtener dia, mes y año.
# Verificar que el mes esté entre 01 y 12 de lo contrario mostrar el mensaje “El mes es incorrecto”.
# Verificar si el día es menor a 0 y si el día es mayor a 28, 29, 30, 31 según corresponda, de lo contrario mostrar el mensaje “El día es incorrecto”.
# Verificar si el año es menor 1900 o el año mayor al año actual.
# Utilizar:
# from datetime import datetime
# Obtener el año con: 
# añoactual=str(datetime.today())[:4]
# Si está todo correcto mostrar el mensaje “La fecha es válida.”.
