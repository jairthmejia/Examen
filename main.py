import os
from lector import obtener_datos_financieros

# Construimos la ruta segura a tu archivo dentro de la carpeta
ruta = os.path.join("Archivos/", "recaudos_2026_09.txt")

# Obtenemos el DataFrame (la tabla de datos de pandas)
df_datos_financieros = obtener_datos_financieros(ruta)

# Mostramos el resultado en pantalla
print("Datos cargados exitosamente")
print(df_datos_financieros)