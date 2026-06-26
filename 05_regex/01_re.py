# Primero, importamos el módulo
import re

# Creamos un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"

# Texto donde queremos buscar
text = "Hola mundo"

# Usamos la función de búsqueda de "re"
result = re.search(pattern, text)
print(result)

if result:
    print("He encontrado el patrón en el texto") 
else: 
    print("No he encontrado el patrón en el texto")

# .group() devuelve la cadena que coincide con el patrón que queremos encontrar
print(result.group())

# .start() devuelve la posición inicial de la coincidencia
print(result.start())

# .end() devuelve la posición final de la coincidencia
print(result.end())

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_ia = re.search(pattern, text)
if found_ia:
    print(f"Encontrado. Empieza en la posición {found_ia.start()} y acaba en la {found_ia.end()}")
else:
    print("No he encontrado la ocurrencia de IA")

# -----------------------

### Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)
print(len(matches))

# -----------------------

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group(), match.start(), match.end())

# EJERCICIO 02
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto 
# e indica en qué posición empieza y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"

matches = re.finditer(pattern, text)
contador = 0
for match in matches:
    print(match.group(), match.start(), match.end())
    contador +=1
print(contador)

# Modificadores - opciones que se pueden agregar a un patrón para cambiar su comportamiento

# .IGNORECASE -> ignora mayúsculas y minúsculas
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)
print(found)


# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto,
# sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "Python"
found_py = re.findall(pattern, text, re.IGNORECASE)
print(found_py)

# Reemplazar texto
# .sub() -> reemplaza todas las coincidencias 
text = "Hola, mundo! Hola de nuevo."
pattern = "Hola"
replacement = "Adiós"

new_text = re.sub(pattern, replacement, text)
print(new_text)

