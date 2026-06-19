"""
DEFINICIÓN DE UNA FUNCIÓN:
def nombre_de_la_funcion(param1, param2, ...):  // minus y snake_case
    # docstring
    # código (cuerpo de la función)   
    return valor_de_retorno  // opcional                     
"""
import os
os.system("cls")

# Ejemplo
def saludar():
    print("¡Hola!")

saludar()

# Ejemplo con parámetros -> lo que acepta la función
def saludar_a(nombre):
    print(f"Hola, {nombre}")

saludar_a("Su") # se le pasa un argumento

# Funciones con más parámetros
def sumar(a,b):
    return a + b

result = sumar(2, 3)
print(result) 

# Documentar funciones con docstring
def restar(a, b):
    """Resta dos números y devuelve el resultado"""
    return a - b

# Se puede acceder al docstring
# print(restar.__doc__)
# help(restar)

# parámetros por defecto
def multiplicar(a, b = 2):
    return a * b

print(multiplicar(2)) # multiplica 2 * 2 porque no se le pasa argumento para b
print(multiplicar(5, 5)) # ignora el parámetro por defecto porque se le pasa un argumento para b

# Argumentos por posición 
def describir_persona(nombre, edad, sexo):
    print(f"Soy {nombre}, tengo {edad} años y soy {sexo}")

# los parámetros son posicionales, según la posición de los argumentos significa una cosa u otra
# por lo tanto, si se cambian de posición, "rompes" la función
describir_persona("Su", 26, "mujer")
describir_persona(25, "mujer", "Su")

# Argumentos por clave - parámetros nombrados
describir_persona(nombre="Su", edad=26, sexo="mujer")

# aunque se pase en otra posición, es capaz de ponerlo en su orden a la hora de 
# ejecutar la función porque identifica cada parámetro
describir_persona(edad=26, sexo="mujer", nombre="Su")

# Argumentos de longitud de variable (*args) -> para cuando no se sabe cuántos argumentos se van a pasar
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(5, 10, 5, 98, 0))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_info_de(**kwargs):
    for key, word in kwargs.items():
        print(f"{key}: {word}")

mostrar_info_de(nombre="Valeria", edad=26)
print("\n")
mostrar_info_de(nombre="Su", sexo="mujer", cuenta_substack=True)
