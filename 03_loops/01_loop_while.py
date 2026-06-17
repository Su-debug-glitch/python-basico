import os
os.system("cls")

# Bucle con una condición simple
# contador = 0
# while contador <= 5: 
    # print(contador)
    # contador += 1 # para romper el bucle infinito

print("Bucle con while y break")
contador = 0
while True: # SIEMPRE es True -> bucle infinito
    print(contador)
    contador += 1
    if (contador == 5):
        break # rompe/sale del bucle

print("Bucle con continue")
# se salta esa iteración concreta y continua con el bucle
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)

print("Bucle con else")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

# El else se utiliza cuando te quieres asegurar de que la condición
# del while es FALSA, o sea, deja de cumplirse
# si dentro del bucle se usa un while, nunca entra en el else pq nunca
# encontrará una condición que sea FALSA
# else se usa para ejecutar el bloque de código SOLO SI EL BUCLE TERMINA DE FORMA NATURAL
# NO SI FUE INTERRUMPIDO POR UNA SENTENCIA
print("Bucle con else")
contador = 0
while contador < 5:
    print(contador)
    contador += 1
    break
else:
    print("El bucle ha terminado")

# EJEMPLO: 
# Imagina que estás programando un sistema de inicio de sesión 
# donde el usuario tiene un número limitado de intentos. 
# Puedes usar el bloque else para mostrar un mensaje de bloqueo 
# si el usuario agota todos los intentos sin éxito, 
# o usar break si acierta la contraseña

intentos_restantes = 3
contrasena_correcta = "secreta123"

while intentos_restantes > 0:
    intento = input("Introduce la contraseña: ")
    if intento == contrasena_correcta:
        print("¡Acceso concedido!")
        break # El bucle se rompe aquí, el 'else' no se ejecutará
    else:
        intentos_restantes -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos.")
else:
    # Este bloque solo se ejecuta si el bucle terminó porque 'intentos_restantes' llegó a 0
    print("Has agotado todos tus intentos. Cuenta bloqueada.")

# EJEMPLO 2: pedirle al usuario un número que debe ser positivo
numero = -1
while numero < 0:
    numero = int(input("Escribe un número positivo:"))
    if numero < 0:
        print("El número debe ser positivo. Intenta de nuevo")
    
print(f"El número introducido es {numero}")
# NO TIENE EN CUENTA SI EL USUARIO ESCRIBE OTROS TIPOS DE VALORES -> PETA

# Try - Except
numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un número positivo:"))
        if numero < 0:
            print("El número debe ser positivo. Intenta de nuevo")
    except:
        print("Debes introducir un NÚMERO")
    
print(f"El número introducido es {numero}")
