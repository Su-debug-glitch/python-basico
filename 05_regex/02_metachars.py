import re
# 1. El punto (.)
# Coincide con cualquier caracter (UNO) excepto una nueva línea

text = "Hola mundo, HOla de nuevo, h$la otra vez."
pattern = "H.la" # coincide con cualquier caracter en esa posición (excepto nueva línea)

found = re.findall(pattern, text, re.IGNORECASE)
print(found)

# -------------------------

text = "Hola mundo, HOla de nuevo, h$la otra vez."
pattern = r"H.la" # coincide con cualquier caracter en esa posición (excepto nueva línea)

found = re.findall(pattern, text, re.IGNORECASE)
print(found)

text = "Mi casa es blanca. Mi coche es negro."
pattern = r"\." # anula el significado del punto (cualquier caracter) y busca el punto literal
matches = re.findall(pattern, text)
print(matches)


# 2. Buscar dígitos -> \d: coincide con cualquier dígito (0-9)

text = "El número de teléfono es 123456789"
found = re.findall(r'\d{9}', text) # se repite 9 veces -> encuentra todo el número
print(found)

# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34
text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)
print(f"Encontré el número de teléfono {found.group()}")

# \w: coincide con cualquier caracter alfanumérico (a-z, A-Z, 0-9, _)
text = "el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: coincide con espacios en blanco, tabulación, salto de línea
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"
matches = re.findall(pattern, text)
print(matches)

# ^: coincide con el principio de una cadena
username = "546_name"
pattern = r"^\w"

valid = re.search(pattern, username)

if valid: 
    print("El nombre de usuario es válido")
else: 
    print("El nombre de usuario no es válido")

phone = "+34 698854458"
pattern = r"^\+\d{1,3} \d{9}"

valid = re.search(pattern, phone)

if valid: 
    print("El teléfono es válido")
else: 
    print("El teléfono no es válido")

# $: coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"

valid = re.search(pattern, text)
if valid: print("Acaba en 'mundo'")
else: print("No acaba en 'mundo'")

# EJERCICIO
# Valida que un correo sea de gmail
text = "susu@gmail.com"
pattern = r"@gmail.com$"
valid = re.search(pattern, text)

if valid: print("Correo gmail válido")
else: print("No válido")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\w+\.txt"

files_txt = re.findall(pattern, files)

if files_txt: print(files_txt)
else: print("No hay archivos con .txt")

# \b: Coincide con el principio o final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found)

# |: Coincidr con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)
