import json

import pandas as pd

archivo_csv = "final.csv"
df = pd.read_csv(archivo_csv)

# Agrupar las palabras por clave
grupos = df.groupby("key")["palabras"].apply(list).to_dict()

# Nombre del archivo JSON de salida
archivo_json = "datos.json"

# Guardar el diccionario como JSON
with open(archivo_json, "w", encoding="utf-8") as file:
    json.dump(grupos, file, indent=4, ensure_ascii=False)
