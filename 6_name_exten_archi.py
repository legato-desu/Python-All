# Obtener la extencion de un archivo especificado por el usuario

"""
El usuario va a ingresar el nombre del archivo y se 
usara el metodo basico para obtener la extencion de 
ese nombre de archivo que nos a dado el usuario 

"""
nombre_archivo = input('Ingrese el nombre del archivo: ')

partes_nombre_archivo = nombre_archivo.split('.')

print(partes_nombre_archivo)

print(partes_nombre_archivo[-1])