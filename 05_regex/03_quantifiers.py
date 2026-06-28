import re

# * -> puede aparecer 0 o más veces
text = "aaaaaaaba"
pattern = "a*b"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 1:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?
text = "b ab aab aaab cab"
pattern = r"\ba*b\b"
matches = re.findall(pattern, text)
print(len(matches))

# + -> puede aparecer una o más veces
text = "ddd aaaaa cc bb acab casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

# ? -> puede aparecer 0 o 1 vez
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern = r"\+34? \d{9}"
matches = re.findall(pattern, phone)
print(matches)

# {n} -> debe aparecer exactamente n veces
text = "aaaaaaaaaaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
print(matches)

# {n, m} -> de n a m veces´
text = "ss s sssssss s"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Ejercicio
# Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)