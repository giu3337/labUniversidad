class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo


    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años.")
        