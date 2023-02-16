# Obtener un conjunto de numeros separados por coma y crear una lista

# 2, 8, 9, 0, 1, 8

entrada = input('Ingrese varios numeros separados por una coma (,): ')

print(entrada)
print(type(entrada))

numeros = entrada.split(',')

print(type(numeros))
print(numeros)