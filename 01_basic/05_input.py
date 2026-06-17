# Entrada de usuario con la función input(), que permite obtener datos 
# del usuario a través de la consola. El valor ingresado se almacena como una cadena (string).


# Ejemplo 1
print("Hola, ¿cómo te llamas?")
nombre = input()  # La función input() espera a que el usuario ingrese un valor y presione Enter
print("¡Hola, " + nombre + "! Encantado de conocerte.")

# Ejemplo 2, igual pero de otra manera
nombre = input("Hola, ¿cómo te llamas?\n ")
print(f"¡Hola, {nombre}! Encantado de conocerte.")

# Ejemplo 3, con números
edad = input("¿Cuántos años tienes?\n ")
print(f"Tienes {edad} años.")
# Nota: La función input() siempre devuelve una cadena, incluso si el usuario ingresa un número.
# Si queremos trabajar con números, debemos convertir la cadena a un tipo numérico, como int o float.
edad = int(input("¿Cuántos años tienes?\n "))
print(f"Tienes {edad} años.")

print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n ").split() 
# La función split() divide la cadena en partes basándose en un separador (por defecto, el espacio) 
# y devuelve una lista de las partes.
print(f"Vives en {city.capitalize()}, {country.capitalize()}.") 
# La función capitalize() convierte la primera letra de una cadena a mayúscula y el resto a minúscula.


