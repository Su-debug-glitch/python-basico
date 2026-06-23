# Son parecidos a los objetos en javascript
import os
os.system("cls")
# Ejemplo
persona = {
    "nombre": "Su",
    "edad": 26,
    "es_estudiante": True,
    "notas": [10, 9, 9],
    "comida_fav": {
        "primer_plato": "tostadas",
        "segundo_plato": "pasta",
        "postre": "helado"
    }
}

# para acceder a los valores
print(persona["nombre"])
print(persona["comida_fav"]["postre"])

# para cambiar valores -> se vuelve a asignar
persona["nombre"] = "Suhaila"
print(persona["nombre"])

# eliminar una propiedad
del persona["edad"]
print(persona)
del persona["comida_fav"]["segundo_plato"]
print(persona["comida_fav"])

# devuelve el valor de la clave pero lo elimina del objeto
es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = {"name": "Su", "edad": 26}
b = {"name": "Suhaila", "es_estudiante": True}

a.update(b)
print(a)

# comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True

# para obtener todas las claves
print(persona.keys())

# para obtener todos los valores
print(persona.values())

# para obtener claves y valores
print(persona.items())

for key, value in persona.items():
    print(f"key: {key} \nvalue: {value}")