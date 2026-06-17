###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
nombre = "Su"
ciudad = "Manresa"
print(f"Te llamas {nombre}\nVives en {ciudad}.")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"El tipo de dato de a es {type(a)}")
print(f"El tipo de dato de b es {type(b)}")
print(f"El tipo de dato de c es {type(c)}")
print(f"El tipo de dato de d es {type(d)}")
print(f"El tipo de dato de e es {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
cadena_entero = int(cadena)
print(f"El número entero es: {cadena_entero}")
cadena_float = float(cadena)
print(f"El número float es: {cadena_float}")
num = 3.99
num_entero = int(num)
print(f"El número entero de 3.99 es: {num_entero} (se redondea hacia abajo)")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
my_name = "Suhaila"
my_age = 26
my_height = 1.72
print(f"Holiwi, me llamo {my_name}, tengo {my_age} años y mido {my_height}.")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
pi = 3.1416
pi_redondeado = round(pi)
division_entera = pi_redondeado // 2
print(f"La división entera de {pi_redondeado} entre 2 es: {division_entera}")