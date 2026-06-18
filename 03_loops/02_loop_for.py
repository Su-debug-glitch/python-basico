import os
os.system("cls")

print("----Bucle for:----")

# Iterar una lista
frutas = ["manzana", "pera", "sandía"]
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa iterable
cadena = "Hola soy Su"
for caracter in cadena:
    print(caracter)

print("----Bucle for + enumerate():----")
# enumerate() - permite iterar sobre los elementos de un iterable 
# y devolver un índice y el elemento
frutas = ["manzana", "pera", "sandía"]
for index, fruta in enumerate(frutas):
    print(f"El índice es {index} y la fruta es {fruta}")

print("----Bucles for anidados:----")
# Bucles anidados
letras = ['a', 'b', 'c']
numeros = [1, 2, 3]

for letra in letras:
    for num in numeros:
        print(f"{letra} x {num} = {letra * num}")


# break
print("----Bucle for con break:----")
animales = ["perro", "gato", "loro", "rata", "cobaya", "ardilla"]
for idx, animal in enumerate(animales):
    print(f"Idx: {idx}, animal: {animal}")
    if animal == "loro":
        break

# continue
print("----Bucle for con continue:----")
animales = ["perro", "gato", "loro", "rata", "cobaya", "ardilla"]
for idx, animal in enumerate(animales):
    if animal == "loro":
        continue
    print(f"Idx: {idx}, animal: {animal}")

# List comprehension
print("-----List comprehension:-----")
animales = ["perro", "gato", "loro", "rata", "cobaya", "ardilla"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# List comprehension con condicionales
pares = [num for num in [1,2,3,4,5,6,7,8,9,10] if num % 2 == 0]
print(pares)