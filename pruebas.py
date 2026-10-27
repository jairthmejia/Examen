import pandas as pd

# DataFrame de ejemplo
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Ana', 'Carlos'],
    'Edad': [25, 30, 25, 40]
})

# Elimina filas duplicadas
df_limpio = df.drop_duplicates()
print(df)
print(df_limpio)

