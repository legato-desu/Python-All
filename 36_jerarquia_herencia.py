# Crear una jerarquia de herencia basica.

# Persona <- Estudiante

class Persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo

class Estudiante(Persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
        super().__init__(documento, nombre, correo)        
        self.carnet = carnet
        self.carrera = carrera
david = Estudiante('950625','David','Pruebapython@col.co','15143','Programador') 

print(isinstance(david, Estudiante))
print(isinstance(david, Persona))