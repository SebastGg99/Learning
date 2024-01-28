## CLASES, OBJETOS = INSTANCIAS, ATRIBUTOS Y MÉTODOS

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print("Estás llamando")
    
    def colgar(self):
        print("Estás colgando")

#celular1 = Celular("Samsung", "S23", "48MP")
#print(celular1.marca)

##########################################################################################################

## HERENCIAS DE CLASES

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print("\nHola, ¿cómo estás?")

class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, trabajo, salario):
        super().__init__(nombre, apellido, edad)
        self.trabajo = trabajo
        self.salario = salario

#roberto = Empleado("Roberto", "Arteaga", 24)
#roberto.saludar()
#print(f"\nme llamo {roberto.nombre} {roberto.apellido} y tengo {roberto.edad} años.\n")

roberto = Empleado("Roberto", "Arteaga", 24, "Albañil", 800000)
#roberto.saludar()

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, universidad, carrera):
        super().__init__(nombre, apellido, edad)
        self.universidad = universidad
        self.carrera = carrera

### Con las dos clases, Estudiante y Empleado, podemos hablar del concepto de herencia jerarquica.
##########################################################################################################

## HERENCIA MÚLTIPLE

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, apellido, edad, habilidad, trabajo, salario):
        Persona.__init__(self, nombre, apellido, edad)
        Artista.__init__(self, habilidad)
        self.trabajo = trabajo
        self.salario = salario
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, {super().mostrar_habilidad()} y trabajo de {self.trabajo}")

roberto = EmpleadoArtista("Roberto", "Arteaga", 24, "Pintar", "Albañil", 800000)
#roberto.presentarse()

herencia = issubclass(EmpleadoArtista, Artista)
instancia = isinstance(roberto, EmpleadoArtista)

#print(herencia/instancia)