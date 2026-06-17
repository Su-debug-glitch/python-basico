import os
os.system("cls")
# Crear listas
lista1 = [1, 2, 3, 4, 5] # enteros
lista2 = ['a', 'b', 'c', 'd'] # cadenas de texto
lista3 = [1, 'a', 3.14, True] # mezcla de tipos de datos

lista_vacia = []
lista_de_listas = [[1, 2], ['a', 'b'], [3.14, True]]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceder a elementos de una lista por índice
print("-------Acceso a elementos por índice-------")
print(lista1[0]) # primer elemento (1)
print(lista1[-1]) # último elemento (5)

print(lista_de_listas[0][1]) # accede al segundo elemento de la primera sublista (2)

# Slicing
print("-------Slicing-------")
lista = [10, 20, 30, 40, 50]
print(lista[1:4]) # elementos desde el índice 1 hasta el 3

print(lista[:3]) # primeros 3 elementos (10, 20, 30)
print(lista[2:]) # elementos desde el índice 2 hasta el final (30, 40, 50)
print(lista[::2]) # elementos con paso de 2 (10, 30, 50)
print(lista[::-1]) # lista invertida (50, 40, 30, 20, 10)
print(lista[:]) # toda la lista (10, 20, 30, 40, 50)

# Modificar elementos de una lista
print("-------Modificar elementos-------")
lista[0] = 10.5
print(lista)

# Añadir elementos a una lista
print("-------Añadir elementos-------")
lista = lista + [60] # concatenación pero no eficiente pq guarda en memoria la operación y luego la asigna
print(lista) # [10.5, 20, 30, 40, 50, 60]

lista += [70, 80] # concatenación más corta y más eficiente pq directamente añade los elementos a la lista
print(lista) # [10.5, 20, 30, 40, 50, 60, 70, 80]

# Recuperar longitud
print("-------Longitud de la lista-------")
print("Longitud de la lista: ", len(lista)) # devuelve 8
