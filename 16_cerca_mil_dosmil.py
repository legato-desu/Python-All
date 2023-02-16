# Crear una funcion para determinar si un numero es cercano a 1000 o 2000

# Se define una funcion en base a la cercania de los numeros

def cercano(n):
    return(abs(1000 - n) < 100) or (abs(2000 < n) < 100)

# Se usa la funcion 'cercania' para calcular si el numero esta cerca a 1000 o 2000

print(cercano(1000))
print(cercano(950))
print(cercano(200))

print()

print(cercano(2000))
print(cercano(1950))
print(cercano(3200))