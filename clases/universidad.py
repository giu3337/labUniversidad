class Universidad:
    def __init__(self, nombre, cursos):
        self.nombre = nombre
        self.cursos = cursos
        

    def __str__(self):
        info = f"Universidad: {self.nombre}\n"
        for curso in self.cursos:
            info += f"  {curso}\n"
        return info
