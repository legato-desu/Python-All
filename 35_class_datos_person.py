# Crear una clase para representar los datos de una persona.

class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    def __str__(self):
        return 'Nombre: {}\nEdad: {}\nCorreo: {}'.format(self.nombre,self.edad,self.correo)
david = Persona('David', '27','prueba-python@hotmail.com')

print(david)