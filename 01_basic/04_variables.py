# Asignar
my_name = "Su"
print(my_name)

# Reasignar
my_name = "Su"
print(my_name)

my_name = "Suhaila"
print(my_name)

age = 26
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución
# no hay que declararlo explicitamente
name = "Su"
print(type(name)) # <class 'str'>

name = 123
print(type(name)) # <class 'int'>

# Tipado fuerte: no realiza conversiones implícitas entre tipos de datos
# print ("El nombre es " + name) # TypeError: can only concatenate str (not "int") to str 
print ("El nombre es " + str(name)) # El nombre es 123

# Formateo de cadenas - f-strings
print(f"El nombre es {my_name} y tiene {age} años") # El nombre es Suhaila y tiene 26 años

# Convenciones de nombrado
# snake_case: palabras separadas por guiones bajos
mi_nombre_de_variable = "ok"
mi_nombre_de_variable_123 = "ok" # con números AL FINAL, no al inicio

MI_CONSTANTE = 3.14 # mayúsculas para constantes (aunque no existen realmente en Python)

# Asignar tipo de dato a variable (opcional, pero recomendado para mejorar la legibilidad y evitar errores)
is_user_logged_in: bool = True # booleano, puede ser True o False
print(is_user_logged_in) # True

is_user_logged_in = 1 # funciona también
print(is_user_logged_in) # 1 