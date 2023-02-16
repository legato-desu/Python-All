# solicitar al usuario un numero n y calcular n + nn + nnn

n = input('Ingrese el valor de n: ')

nn = int('{}{}'.format(n,n))

nnn = int('%s%s%s'%(n,n,n))

n = int(n)

suma = n + nn + nnn

print(suma)