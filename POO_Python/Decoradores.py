# Los decoradores son funciones adicionales que "decoran" una función inicial (global)

def decorador(funcion):
    def funcion_mod():
        print("Antes de llamar la función")
        funcion()
        print("Después de llamar la función")
    return funcion_mod

# No existe una forma estándar de construir los decoradores, por ejemplo esta forma sería una válida:

# def saludo():
#     print("Hola")

# saludo_mod = decorador(saludo)
# saludo_mod()

# Pero, esta es la forma recomendada, ya que puede ser más generalizable.
@decorador
def saludo():
    print("Hola")

saludo()
# Los decoradores "Añaden funcionalidades a la función global"