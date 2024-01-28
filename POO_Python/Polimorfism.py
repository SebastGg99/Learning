class Gato:
    def sonido(self):
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"
    
class Pato:
    def sonido(self):
        return "Cuack"

gato = Gato()
perro = Perro()

#print(perro.sonido()) / print(gato.sonido())

def hacer_sonido(animal):
    print(animal.sonido())

#hacer_sonido(perro) / hacer_sonido(perro)

''' De lo anterior, podemos ver dos tipos de polimorfismo:
    1) Por un lado, polimorfismo de objetos y también
    2) Polimorfismo de argumentos en funciones.'''