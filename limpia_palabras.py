import pandas as pd

archivo_a_limpiar = "argentinas.csv"
archivo_salida = "final2.csv"
letras_ok = [
    "b",
    "c",
    "d",
    "f",
    "g",
    "ch",
    "j",
    "k",
    "l",
    "m",
    "n",
    "ñ",
    "p",
    "q",
    "r",
    "s",
    "t",
    "v",
    "z",
]

# esto es para importar el archivo de texto con palabras, y hacer una lista
palabras = pd.read_csv(archivo_a_limpiar, header=None, names=["Palabra"])
palabras["Palabra"] = palabras["Palabra"].str.strip()
lista = palabras["Palabra"].to_list()

final_dict = {}
key = []
palabras_arr = []


for idx, palabra in enumerate(lista):  # recorremos cada palabra
    len_palabra = len(palabra) - 1
    keyword = ""
    for idx_p, ch in enumerate(palabra):  # recorremos cada caractér de cada palbra
        # acá hacemos una pequeña validación por que la CH es un caractér de por sí, entonces tenemos que fijarnos en la siguiente letra
        next_index = idx_p + 1
        if ch == "c" and next_index <= len_palabra:
            if palabra[next_index] == "h":
                ch = "ch"
        if ch in letras_ok:
            keyword += ch
    if keyword != "":
        palabras_arr.append(palabra)
        key.append(keyword)

# para exportar a CSV, luego podemos ver que hacemos con eso
final_dict["key"] = key
final_dict["palabras"] = palabras_arr

df = pd.DataFrame(final_dict)
df.to_csv(archivo_salida, index=False)
