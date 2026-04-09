import json

import os


ARCHIVO = "memoria/historial.json"

ARCHIVO_RESUMEN = "memoria/resumen.txt"


MAX_MENSAJES = 12



def cargar():

    if not os.path.exists(ARCHIVO):

        return []

    with open(ARCHIVO, "r", encoding="utf-8") as f:

        return json.load(f)



def guardar(historial):

    with open(ARCHIVO, "w", encoding="utf-8") as f:

        json.dump(historial, f, indent=2, ensure_ascii=False)



def agregar(rol, contenido):

    historial = cargar()


    historial.append({

        "rol": rol,

        "contenido": contenido

    })



    if len(historial) > MAX_MENSAJES:

        resumen = generar_resumen(historial[:-6])

        guardar_resumen(resumen)

        historial = historial[-6:]


    guardar(historial)



def contexto():

    historial = cargar()

    resumen = leer_resumen()


    texto = ""


    if resumen:

        texto += f"Resumen previo:\n{resumen}\n\n"


    for m in historial:

        texto += f"{m['rol']}: {m['contenido']}\n"


    return texto



# ======================

# RESUMEN

# ======================


def generar_resumen(mensajes):

    texto = ""

    for m in mensajes:

        texto += f"{m['rol']}: {m['contenido']}\n"


    return f"Resumen de conversación:\n{texto}"



def guardar_resumen(resumen):

    with open(ARCHIVO_RESUMEN, "w", encoding="utf-8") as f:

        f.write(resumen)



def leer_resumen():

    if not os.path.exists(ARCHIVO_RESUMEN):

        return ""

    with open(ARCHIVO_RESUMEN, "r", encoding="utf-8") as f:

        return f.read()
