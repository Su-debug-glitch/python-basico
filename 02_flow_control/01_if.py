# if, elif, else
import os
os.system("cls")

# Ejemplo 1
print("------Sentencia simple condicional------")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejemplo 2 (mío)
print("------Sentencia simple condicional pidiendo datos al usuario------")
edad = int(input("¿Qué edad tienes?\n"))

if edad >= 18:
    print("Eres mayor de edad")
else: 
    print("Eres menor de edad")

# Ejemplo 3
print("------Sentencia condicional con elif------")
nota = 7.5
print("Tu nota es:", nota)

if nota >= 9:
    print("Excelente")
elif nota >= 5:
    print("Bien")
else:
    print("Insuficiente")

# Ejemplo 4 con condiciones múltiples + input del usuario (mio)
print("------Sentencia condicional con condiciones múltiples------")
edad = int(input("¿Qué edad tienes?\n"))
tiene_carnet = input("¿Tienes carnet de conducir? (True/False)\n").strip().lower() == "true"

if edad >= 18 and tiene_carnet:
    print("Puedes conducir 🚗")
else:
    print("No puedes conducir 🚫")

# Ejemplo 5 con OR
print("------Sentencia condicional con OR------")
dia = input("¿Qué día es hoy? (lunes, martes, miércoles, jueves, viernes, sábado, domingo)\n").strip().lower()
if dia == "sábado" or dia == "domingo":
    print("Es fin de semana 🎉")
else:    
    print("Es día laborable 💼")

# Ejemplo 6 con NOT + OR, guardando la condición en una variable con el ejemplo anterior
print("------Sentencia condicional con NOT------")
is_weekend = dia == "sábado" or dia == "domingo"
if not is_weekend:
    print("Es día laborable 💼")
else:
    print("Es fin de semana 🎉")

numero = 5
if numero: # Cualquier número distinto de 0 se considera True, el 0 se considera False
    print("El número es verdadero (distinto de 0)")

nombre = "Alice"
if nombre: # Cualquier cadena no vacía se considera True, la cadena vacía "" se considera False
    print("El nombre es verdadero (no está vacío)")

# Ejemplo 7 con operador ternario
# [código si cumple la condición] if [condición] else [código si no se cumple]
print("------Operador ternario------")
edad = int(input("¿Qué edad tienes?\n"))
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)