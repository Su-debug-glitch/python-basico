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

# enumerate() - permite iterar sobre los elementos de un iterable 
# y devolver un índice y el elemento
frutas = ["manzana", "pera", "sandía"]
for index, fruta in enumerate(frutas):
    print(f"El índice es {index} y la fruta es {fruta}")