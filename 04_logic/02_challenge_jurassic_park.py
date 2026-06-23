"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, 
como el temible T-Rex, depositan un número par de huevos. 
Imagina que tienes una lista de números enteros en la que cada número 
representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) 
aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma 
total de los huevos que pertenecen a los dinosaurios carnívoros 
(es decir, la suma de todos los números pares en la lista).
"""

import os
os.system("cls")

def count_carinvore_dinosaur_eggs(egg_list) -> int:
    """
    Esta función recibe una lista de numeros enteros que representan la cantidad de huevos
    que han puesto diferentes dinosaurios en el parque jurásico y los de número par 
    son de carnívoros. Devuelve un número con la suma de todos los huevos de carnívoros.
    """

    total_eggs = 0

    for egg in egg_list:
        if egg % 2 == 0:
            total_eggs += egg
        
    return total_eggs

egg_list = [3, 5, 8, 9, 10, 1]

print(count_carinvore_dinosaur_eggs(egg_list))




