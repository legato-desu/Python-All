# Obtener la representacion inversa de una cadena de caracteres

# Python => nohtyP

cadena = 'Python'

# Utilizamos el ciclo "for" para invertir los caracteres de "cadena"
for i in range(len(cadena)-1,-1,-1):
    print(cadena[i],end='')

# Hacemos un salto de linea para darle forma estetica al resultado
print()

print(cadena[::-1])