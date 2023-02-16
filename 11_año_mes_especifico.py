# Imprimir el calendario para un año y mes especifico 

import calendar

# Dado el año y mes ingresado por el usuario se imprime tipo calendario de la fecha ingresada

year = int(input('Escribe el año: '))
month = int(input('Escriba el mes: '))

print(calendar.month(year, month))