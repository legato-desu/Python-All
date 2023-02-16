# Obtener un conjunto de numeros separados por coma y crear una lista

# 2, 8, 9, 0, 1, 8

entrada = input('Ingrese varios numeros y separelos por una coma (,): ')

# Se enseña por pantalla los numeros ingresados por el usuario y se enseña el tipo de dato

print(entrada)
print(type(entrada))

numeros = entrada.split(',')

# Tras la conversion se muestra el tipo de dato y se imprime la lista

print(type(numeros))
print(numeros)