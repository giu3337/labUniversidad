from .persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, sexo, codigo, especialidad):
        super().__init__(nombre, edad, sexo)
        self.codigo = codigo
        self.especialidad = especialidad

    def __str__(self):
        return f"Profesor: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}, Código: {self.codigo}, Especialidad: {self.especialidad}"
