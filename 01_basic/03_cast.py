# Transformar un tipo de un valor a otro tipo se llama "casting" o "type conversion"

print("Conversión de tipos")
print("str a int:")
print(int("123")) # convierte la cadena "123" a un entero 123
print(type(int("123"))) # muestra el tipo del resultado
print(int("123") + 3) # muestra que el resultado es un entero y se puede sumar con otro entero

print("100" + str(3)) # convierte el entero 3 a una cadena "3" y la concatena con "100"

print(type(float("3.14"))) # convierte la cadena "3.14" a un número de punto flotante 3.14 y muestra su tipo

print(type(bool(0))) # convierte el entero 0 a un valor booleano False y muestra su tipo
print(type(bool(1))) # convierte el entero 1 a un valor booleano True y muestra su tipo
print(type(bool(-1))) # convierte el entero 1 a un valor booleano True y muestra su tipo
print(type(bool(""))) # convierte la cadena vacía a un valor booleano False y muestra su tipo
print(type(bool("Hello"))) # convierte la cadena no vacía a un valor booleano True y muestra su tipo
print(type(bool(None))) # convierte el valor None a un valor booleano False y muestra su tipo

print(round(3.5)) # redondea el número 3.5 al entero PAR más cercano, que es 4
print(round(2.5)) # redondea el número 2.5 al entero PAR más cercano, que es 2
print(round(1.5)) # redondea el número 1.5 al entero PAR más cercano, que es 2
print(round(3.2)) # redondea el número 3.2 al entero más cercano, que es 3