# Calcular la suma de tres numeros si todos son diferentes, en caso contrario la suma sera 0.

def sumar (x, y, z):
    """
    Suma tres numeros. Si al menos dos numeros son iguales, la suma sera 0.
    """
    if x == y or x == z or y == z:
        return 0
    else:
        return x + y + z    
print(sumar(2,5,3))
print(sumar(2,5,2))
print(sumar(5,5,2))
print(sumar(11,7,5))