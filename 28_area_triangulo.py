# Calcular el area de un triangulo
base = None
altura = None
while True:
    try:
        base = float(input('Ingrese la base del triangulo: '))
        break
    except:
        print('debe ingresar un numero')
while True:
    try:
        altura = float(input('Ingrese la altura del triangulo: '))
        break
    except:
        print('debe ingresar un numero')
area = base * altura / 2
print('El area del triangulo es igual: {}'.format(area))