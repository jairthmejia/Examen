import shutil
# ... (tus otras importaciones y funciones se quedan igual)

def copiar_archivo_prueba(ruta_origen, ruta_destino):
    """
    Copia un archivo desde una ruta de origen a una ruta de destino.
    Si las carpetas de destino no existen, las crea automáticamente.
    """
    try:
        # Crea la carpeta de destino si no existe
        carpeta_destino = os.path.dirname(ruta_destino)
        if carpeta_destino and not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            print(f"Carpeta creada: {carpeta_destino}")
        
        # Realiza la copia física del archivo
        shutil.copy(ruta_origen, ruta_destino)
        print(f"Archivo copiado con éxito de '{ruta_origen}' a '{ruta_destino}'")
        return True
    except FileNotFoundError:
        print(f"Error: El archivo de origen '{ruta_origen}' no fue encontrado.")
        return False
    except Exception as e:
        print(f"Ocurrió un error inesperado al copiar: {e}")
        return False