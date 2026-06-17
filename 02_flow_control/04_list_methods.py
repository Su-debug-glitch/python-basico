import os
os.system("cls")

# AÑADIR
lista = [1, 2, 3, 4, 5]

lista.append(6) # añade al final

lista.insert(1, 5) # inserta un elemento en la posición que se le indique como primer parámetro
print(lista)

lista.extend([7, 8, 9]) # añade varios elementos al final
print(lista)

# ELIMINAR
lista.remove(5) # elimina el primer elemento que coincida con el valor indicado
print(lista)

lista.pop(0) # elimina el elemento en la posición indicada y lo devuelve
print(lista)
lista.pop() # elimina el último elemento y lo devuelve
print(lista)

# del -> se utiliza sobre todo para eliminar un rango de elementos
del lista[0] # elimina el elemento en la posición indicada
print(lista)
del lista[1:3]
print(lista)

lista.clear() # elimina todos los elementos de la lista
print(lista)

# ORDENAR
numbers = [5, 9, 10, 999, 74, 0]
numbers.sort() # modifica la lista, y la guarda ordenada, pero no la devuelve (no se podría guardar en una variable)
print(numbers)

# ordenar con cadenas de texto - ordena por orden alfabético
frutas = ['manzana', 'limón', 'pera', 'tomate']
frutas.sort()
print(frutas)

# si hay mayúsculas, primero las pone y luego pone lo demás
frutas = ['Manzana', 'limón', 'Pera', 'tomate']
frutas.sort()
print(frutas)

frutas.sort(key=str.lower) # convierte a minús. internamente y ordena
print(frutas)

# ordenar y crear una lista nueva, no modifica la original como .sort()
numbers = [5, 9, 10, 999, 74, 0]
numbers_ordenada = sorted(numbers)
print(numbers_ordenada)

# Más métodos útiles
animals = ['🫎', '🫎', '🫏', '🐣']
print(len(animals)) # longitud de la lista
print(animals.count('🫎')) # cuántas veces aparece
print('🫎' in animals) # True
