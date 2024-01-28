## ENCAPSULAMIENTO, GETTER Y SETTER

class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor"  #Atributo privado (o protegido, en otros lenguajes)
        self.__atributo_muy_privado = "Otro Valor" #Atributo muy privado (o privado, en otros lenguajes)

    def _hablar(self):
        print("Hola, soy privado")
    
    def __hablar(self):
        print("Hola, soy muy privado")
    
    #Para acceder a atributos (muy)privados, se crean getters dentro de la clase
    def get_atributo_privado(self):
        return self._atributo_privado
    
    def get__atributo_muy_privado(self):
        return self.__atributo_muy_privado
    
    #Para modificar atributos (muy)privados, se crean setters dentro de la clase
    def set_atributo_privado(self, new_private_atribute):
        self._atributo_privado = new_private_atribute
    
    def set__atributo_muy_privado(self, new_very_private_atribute):
        self.__atributo_muy_privado = new_very_private_atribute
    


objeto = MiClase()
print(objeto._atributo_privado) #Por este lado, se puede acceder al valor del atributo de la forma convencional, así sea privado
#print(objeto.__atributo_muy_privado)  #Por este lado, lanza error pues el atributo no es accesible de la forma convencional

objeto._hablar() #Para este caso, lo mismo de los atributos privados
#objeto.__hablar() #Para este caso, lo mismo de los atributos muy privados

##########################################################################################################

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, new_nombre):
         self.__nombre = new_nombre
    
    def set_edad(self, new_edad):
         self.__edad = new_edad
    
yo = Persona("Sebastian", 24)

Nombre = yo.get_nombre()
print(Nombre)
yo.set_nombre("JuanSe")
Nombre = yo.get_nombre()
print(Nombre)

Edad = yo.get_edad()
print(Edad)
yo.set_edad(25)
Edad = yo.get_edad()
print(Edad)