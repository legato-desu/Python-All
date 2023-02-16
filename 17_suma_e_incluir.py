# Calcular la suma de tres numeros, e incluir una condicion de igualdad

def sumar_numeros (a,b,c):
    """
    Calcular la suma de tres numeros. si los tres numeros son
    iguales, la suma se multiplica por 3.
    """
    suma = a + b + c

    if a == b and a == c:
        suma *= 3
    return suma    

print (sumar_numeros(2, 2, 7))
print (sumar_numeros(2, 2, 2))