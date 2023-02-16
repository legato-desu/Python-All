# Obtener la extencion de un archivo especificado por el usuario

nombre_archivo = input('Ingrese el nombre del archivo: ')

partes_nombre_archivo = nombre_archivo.split('.')

print(partes_nombre_archivo)

print(partes_nombre_archivo[-1])