import pandas as pd

def obtener_datos_financieros(ruta_archivo):
    # Lee el archivo saltando las 3 primeras líneas y omitiendo la última, se realiza de esta manera por la forma 
    # en que se encuentra construido el archivo
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
    # Limpia espacios en blanco
    df.columns = df.columns.str.strip()
    
    # Elimina filas duplicadas si existen
    df = df.drop_duplicates()
    
    # 5. Rellenar valores nulos (NaN) pendientes en celdas sueltas
    # Cambia "" por 0 si prefieres rellenar números faltantes con cero
    df = df.fillna("Sin Datos") 
    
    # 6. Resetear el índice para que empiece desde 0 de forma ordenada
    df = df.reset_index(drop=True)

           
    # 2. Eliminación garantizada libre de errores de sintaxis regex:
    df.iloc[:, 2] = df.iloc[:, 2].str.replace(".", "", regex=False)  # Quita puntos
    df.iloc[:, 2] = df.iloc[:, 2].str.replace("-", "", regex=False)  # Quita guiones
    df.iloc[:, 2] = df.iloc[:, 2].str.replace(" ", "", regex=False)  # Quita espacios tradicionales
