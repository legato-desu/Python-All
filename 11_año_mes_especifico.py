# Imprimir el calendario para un año y mes especifico 

import calendar

year = int(input('Escribe el año: '))
month = int(input('Escriba el mes: '))

print(calendar.month(year, month))