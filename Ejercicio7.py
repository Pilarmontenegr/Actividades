# Validar Correo: Desarrollar un formulario para validar correo electrónico.
# Declarar un objeto correo como StringVar para asociar al entry1.
# Insertar un control entry1, establecer las propiedad validate=’key’, width=30, textvariable=correo, show=’*’, validatecommand=(root.register(validar), '%d', '%i', '%P', '%s', '%S').
# Definir la función 
# Permitir el ingreso de los caracteres de la “a” a la “z”, números, “@”, “-”, “_” y “.”.
# Solo debe permitir una sola arroba “@” para esto buscar si ya está la arroba en previous_text.
# Insertar un button1 y establecer la propiedad text=’Validar’, command=validar_button1.
# Definir la función validar_entry1.
# Limitar el ingreso a 10 caracteres.
# Permitir el ingreso de números y guión medio en su respectiva posición.
# Definir la función validar_button1.
# Verificar que los cuatro últimos caracteres de la derecha sean uno de los siguientes, “.com”, “.org”, “.net”, “.edu”, “.gov”, “.gob”, “.mil”, “.inf”, “.tur” (utilizar slicing).
# Verificar que no comience ni termine con arroba “@”.
# Verificar que no comience ni termine con punto “.”.
# En caso de superar los filtros mostrar el mensaje ‘El correo es válido’ de lo contrario ‘El correo no es válido’.