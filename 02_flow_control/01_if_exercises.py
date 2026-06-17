###
# EJERCICIOS
###
import os
os.system("cls")

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num1 = float(input("Introduce el primer número:\n"))
num2 = float(input("Introduce el segundo número:\n"))
if num1 > num2:
    print(f"El número {num1} es mayor que {num2}")
elif num2 > num1:
    print(f"El número {num2} es mayor que {num1}")
else:
    print("Ambos números son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

numero1 = float(input("Introduce el primer número:\n"))
numero2 = float(input("Introduce el segundo número:\n"))
operacion = input("Introduce la operación (+, -, *, /):\n").strip()
if operacion == "+":
    resultado = numero1 + numero2
    print(f"El resultado de {numero1} + {numero2} es: {resultado}")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"El resultado de {numero1} - {numero2} es: {resultado}")
elif operacion == "*":
    resultado = numero1 * numero2
    print(f"El resultado de {numero1} * {numero2} es: {resultado}")
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de {numero1} / {numero2} es: {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
year = int(input("Introduce un año:\n"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Introduce una edad:\n"))
if 0 <= edad <= 2:
    print("Eres un bebé.")
elif 3 <= edad <= 12:
    print("Eres un niño.")
elif 13 <= edad <= 17:
    print("Eres un adolescente.")
elif 18 <= edad <= 64:
    print("Eres un adulto.")
elif edad >= 65:
    print("Eres un adulto mayor.")