# Obtener la fecha y hora actuales en el sistema

import datetime

ahora = datetime.datetime.now()

print(ahora)

print(type(ahora))

# Organizar la fecha 
print(ahora.strftime('%d/%m/%y %H:%M:%S'))