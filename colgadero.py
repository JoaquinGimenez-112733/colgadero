import json
import random as r

from generar_posibilidades import generar_particiones

archivo_json = "datos.json"

with open(archivo_json, "r", encoding="utf-8") as file:
    datos_cargados = json.load(file)

mapa_num_letra = {
    "0": ["r"],
    "1": ["t", "d"],
    "2": ["n"],
    "3": ["m"],
    "4": ["c", "k", "q"],
    "5": ["l"],
    "6": ["s", "c"],
    "7": ["f", "j"],
    "8": ["g", "ch"],
    "9": ["p", "b", "v"],
}

mapa_letra_num = {
    "b": "9",
    "c": "4",
    "d": "1",
    "f": "7",
    "g": "8",
    "ch": "8",
    "j": "7",
    "k": "4",
    "l": "5",
    "m": "3",
    "n": "2",
    "ñ": "2",
    "p": "9",
    "q": "4",
    "r": "0",
    "s": "6",
    "t": "1",
    "v": "9",
    "z": "6",
}


def de_num_a_letra():
    print("Pasame un numero UnU:")
    num = input()
    str_num = str(num)
    palabra = ""
    for elem in str_num:
        value = mapa_num_letra.get(elem)
        palabra = palabra + (value[r.randint(0, len(value) - 1)])
    print(palabra)
    return palabra


def de_letra_a_num():
    print("Pasame una palabrita jiji OwO:")
    string = input()
    num = ""

    len_palabra = len(string) - 1
    for idx_p, elem in enumerate(string):
        next_index = idx_p + 1
        if elem == "c" and next_index <= len_palabra:
            if string[next_index] == "h":
                elem = "ch"
        if elem in mapa_letra_num:
            num = num + (mapa_letra_num.get(elem))
    return int(num) if num else 0


def de_key_a_palabras(num):
    palabras = []


for arr in generar_particiones(de_num_a_letra()):
    frase = ""
    for code in arr:
        try:
            datos = datos_cargados[code]
            frase = frase + " " + datos[r.randint(0, len(datos) - 1)]
        except:
            frase = ""
            break

    if frase != "":
        print(f"Frase: {frase} | codigo usados: {arr}")
