import pandas as pd

def obtener_datos_financieros(ruta_archivo):
    # Lee el archivo saltando las 3 primeras líneas y omitiendo la última
    df = pd.read_csv(
        ruta_archivo, 
        encoding="cp1252",
        skiprows=3, 
        skipfooter=1, 
        engine='python',
        sep=";"
    )
    return df

def limpiar_dataframe(df):
    # 2. Limpiar espacios en blanco invisibles en los nombres de las columnas
    df.columns = df.columns.str.strip()
    
    # 4. Eliminar filas duplicadas si existen
    df = df.drop_duplicates()
    
    # 5. Rellenar valores nulos (NaN) pendientes en celdas sueltas
    # Cambia "" por 0 si prefieres rellenar números faltantes con cero
    df = df.fillna("Sin Datos") 
    
    # 6. Resetear el índice para que empiece desde 0 de forma ordenada
    df = df.reset_index(drop=True)
    
    return df