# Sumar dos numeros. Si la suma esta entre 10 y 30, retornar 30.

def suma (x, y):
    """
    Suma dos numeros. Si la suma esta entre 10 y 30 se retorna 30.
    """
    suma = x + y

    if suma in range (10,30 + 1):
        return 30
    else:
        return suma
print(suma(7,3))
print(suma(7,23))
print(suma(12,17))
print(suma(23,17))