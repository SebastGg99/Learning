class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @nombre.setter
    def nombre(self, new_nombre):
         self.__nombre = new_nombre
    
    @edad.setter
    def edad(self, new_edad):
         self.__edad = new_edad
    

#Los @property permiten usar los getters y setters de forma más directa...
#... ya no son funciones, sino propiedades.

yo = Persona("Sebastian", 24)

Nombre = yo.nombre
print(Nombre)
yo.nombre = "JuanSe"
Nombre = yo.nombre
print(Nombre)

Edad = yo.edad
print(Edad)
yo.edad = 25
Edad = yo.edad
print(Edad)