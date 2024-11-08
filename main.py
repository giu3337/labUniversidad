from clases.curso import Curso
from clases.estudiante import Estudiante
from clases.persona import Persona
from clases.profesor import Profesor
from clases.universidad import Universidad

profesor = Profesor("Juan Perez", 40, "M", "1234", "Matematica")
universidad = Universidad("Universidad de el Salvador", [])
cursos = [Curso("Matematica", "MAT123", profesor), Curso("Fisica", "FIS123", profesor)]
universidad.cursos.extend(cursos)
estudiante = Estudiante("Maria Perez", 20, "F", "12345", "Ingenieria")
print(universidad)
print(estudiante)
print(profesor)
print(cursos[0])