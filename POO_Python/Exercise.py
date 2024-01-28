class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def NomnbreEdad(self):
        return f"mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def Grado(self):
        return f"Además, estoy en grado {self.grado}."
    
estudiante = Estudiante("Sebastian", 24, 11)

print(f"Hola, {estudiante.NomnbreEdad()} {estudiante.Grado()}")