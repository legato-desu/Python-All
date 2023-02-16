# Emular el funcionamiento del producto de cadenas.

def producto_cadena(cadena,repeticion):
    """
    Emula el funcionamiento del producto (*) de cadenas.
    """

    resultado = ""

    for i in range(repeticion):
        resultado += cadena
    return resultado    

print('python ' * 3)
print(producto_cadena('python ',3))


