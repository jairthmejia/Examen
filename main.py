import os
from lector import obtener_datos_financieros
from copiar_archivos import copiar_archivos_planos

# A modo de prueba se crearon estas variables pero pueden ser parametricas o se podrian cambiar mes a mes para el copiado de los archivos 
# desde una ruta a otra

ANIO = "2026"
MES = "09"  # Puedes cambiar estos valores y todo el script se adaptará solo

# Definicion de rutas donde se encuentran alojados los archivos origen y destino de ContaPlus
carpeta_origen = "Archivos/Origen"
carpeta_destino = "Archivos/Destino"

# Definimos los nombres de los archivos. Unos usan la fecha dinámica y otros son fijos.
nombres_archivos = [
    f"cartera_corte_{ANIO}_{MES}.txt",
    "conceptos.txt",
    f"recaudos_{ANIO}_{MES}.txt"
]

print(f"--- Iniciando Copia Parametrizada para el periodo: {ANIO}-{MES} ---")

# ==========================================
# BUCLE DE COPIA AUTOMÁTICA
# ==========================================
archivos_copiados_con_exito = 0

for nombre in nombres_archivos:
    # Construimos la ruta exacta de dónde está y a dónde va cada archivo
    ruta_real = os.path.join(carpeta_origen, nombre)
    ruta_copia = os.path.join(carpeta_destino, nombre)
    
    if os.path.exists(ruta_real):
        # Usamos la función de copia que ya tienes en lector.py
        exito = copiar_archivos_planos(ruta_real, ruta_copia)
        if exito:
            archivos_copiados_con_exito += 1
    else:
        print(f"Alerta: El archivo no existe en el origen: {ruta_real}")

print(f"\nProceso terminado. Se copiaron {archivos_copiados_con_exito} de {len(nombres_archivos)} archivos.")


# Construimos la ruta segura a tu archivo dentro de la carpeta
ruta = os.path.join(carpeta_origen, "recaudos_2026_09.txt")

# Obtenemos el DataFrame (la tabla de datos de pandas)
df_datos_financieros = obtener_datos_financieros(ruta)

# Mostramos el resultado en pantalla
print("Datos cargados exitosamente")
print(df_datos_financieros)