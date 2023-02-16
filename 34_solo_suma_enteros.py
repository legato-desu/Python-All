# Crear una funcion unicamente para sumar numeros enteros.

def sumar (x, y):
    """
    Suma dos numeros. Valida que estos numeros sean enteros.
    """
    if isinstance (x, int) and isinstance(y,int):
        return x + y
    else:
        raise TypeError('Los valores deben ser enteros. ')
    
"""
Termina de una forma mas formal y menos brusca para el usuario.
"""    
try:
    print(sumar(2,3))
    print(sumar(2,'3'))
except TypeError as e:
    print(e)