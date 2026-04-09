import json

import os


ARCHIVO = "memoria/recuerdos.json"



def cargar():

    if not os.path.exists(ARCHIVO):

        return {}

    with open(ARCHIVO, "r", encoding="utf-8") as f:

        return json.load(f)



def guardar(data):

    with open(ARCHIVO, "w", encoding="utf-8") as f:

        json.dump(data, f, indent=2, ensure_ascii=False)



def guardar_si_importante(texto):

    data = cargar()


    texto = texto.lower()


    if "me llamo" in texto:

        data["nombre"] = texto.replace("me llamo", "").strip()


    elif "me gusta" in texto:

        data["gusto"] = texto.replace("me gusta", "").strip()


    elif "estudio" in texto:

        data["estudio"] = texto.replace("estudio", "").strip()


    guardar(data)



def obtener():

    return cargar()
