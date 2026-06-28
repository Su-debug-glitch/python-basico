from datetime import datetime, timedelta

# Obtener fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actuales: {now}")

# Crear fecha y hora especifica
specific_date = datetime(2026, 2, 8, 15, 30)
print(f"Fecha y hora especifica: {specific_date}")

# Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especificado
# formato:

# hacerlo en español
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

format_date = now.strftime("%A %B %Y %H:%M:%S") # domingo junio 2026 13:05:47
print(f"Fecha formateada: {format_date}")
format_date = now.strftime("%d-%m-%Y") # 28-06-2026 (%y sería solo con 2 digitos del año)
print(f"Fecha formateada: {format_date}")

# Operaciones con fechas
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Ayer: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after}")

# Obtener componentes individuales de la fecha
year = now.year
print(year)

month = now.month
print(month)

# Calcular la diferencia entre 2 fechas
date1 = datetime(2025, 2, 8)
date2 = datetime.now()
difference = date1 - date2
print(difference)
print(difference.seconds)