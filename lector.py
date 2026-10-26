# lector.py

def obtener_lineas_especificas(nombre_archivo):
    # Reemplaza "cp1252" por el encoding que te funcionó
    with open(nombre_archivo, "r", encoding="cp1252") as archivo:
        lineas = archivo.readlines()
    
    # Extrae desde la línea 4 hasta la penúltima
        lineas_filtradas = lineas[3:-1]
    
    # Devuelve la lista de líneas limpia (sin espacios vacíos al inicio/final)
    return [linea.strip() for linea in lineas_filtradas]