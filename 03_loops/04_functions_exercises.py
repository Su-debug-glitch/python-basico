# Tabla de multiplicar pidiendo el número por input al usuario
def mostrar_tabla_multiplicar():
    while True: 
        try:
            numero = int(input("Escribe un número para ver su tabla de multiplicar: "))
            break
        except:
            print("Debes introducir un número.")
    for num in range(1, 11):
        print(f"{numero} x {num} = {numero*num}")

mostrar_tabla_multiplicar()

# Imprimir un rango de números de 2 en 2
def imprimir_rango_numeros_paso_dos(desde_a, hasta_b):
    rango = [num for num in range(desde_a, hasta_b, 2)]
    print(rango)

imprimir_rango_numeros_paso_dos(1, 50)

# Calcular la media
numeros = [10, 11, 20, 22, 30, 33]
def calcular_media(lista_numeros):
    suma = 0
    for valor in lista_numeros:
        suma += valor
    media = suma / len(lista_numeros)
    print(f"La media es: {media}")

calcular_media(numeros)
