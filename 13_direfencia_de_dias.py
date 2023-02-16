# Calcular la diferencia en dias de dos fechas

from datetime import date

today = date(1995,6,25)

another_day = date(2023,2,7)

delta = another_day - today

print(delta)
print(delta.days)