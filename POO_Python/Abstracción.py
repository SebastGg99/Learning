# Las clases abstractas son como una especie de plantilla de fondo...
# ... Sirve para crear una especie de metaclase que esconda toda la complejidad interna del programa.

## EJEMPLO
class Auto():
    def __init__(self):
        self._estado = "apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("Encendido")

    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo")

#mi_auto = Auto()
#mi_auto.conducir()

## OTRO EJEMPLO DE CLASES ABSTRACTAS
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, apellido, edad, ocupacion):
        self.nombre = nombre
        self.edad = apellido
        self.edad = edad
        self.ocupacion = ocupacion

    @abstractclassmethod
    def Ocupacion(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, ocupacion):
        super().__init__(nombre, apellido, edad, ocupacion)

    def Ocupacion(self):
        print(f"Yo estudio: {self.ocupacion}")

class Trabajador(Persona):
    def __init__(self, nombre, apellido, edad, ocupacion):
        super().__init__(nombre, apellido, edad, ocupacion)

    def Ocupacion(self):
        print(f"Yo trabajo en el rubro de: {self.ocupacion}")

Yo = Estudiante("Sebas", "G", 24, "Física")
Obrero = Trabajador("Carlos", "C", 43, "Albañil")

Yo.presentarse()
Yo.Ocupacion()
Obrero.presentarse()
Obrero.Ocupacion()