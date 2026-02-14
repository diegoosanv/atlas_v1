import json
import os
from datetime import datetime

# Ruta del archivo de memoria
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_MEMORIA = os.path.join(BASE_DIR, "recuerdos.json")


def inicializar_memoria():
    """
    Crea el archivo de memoria si no existe
    """
    if not os.path.exists(ARCHIVO_MEMORIA):
        memoria_inicial = {
            "usuarios": {},
            "conversaciones": [],
            "hechos_importantes": []
        }
        with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as f:
            json.dump(memoria_inicial, f, indent=4, ensure_ascii=False)


def cargar_memoria():
    """
    Carga toda la memoria desde disco
    """
    with open(ARCHIVO_MEMORIA, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_memoria(memoria):
    """
    Guarda la memoria completa en disco
    """
    with open(ARCHIVO_MEMORIA, "w", encoding="utf-8") as f:
        json.dump(memoria, f, indent=4, ensure_ascii=False)


def guardar_conversacion(usuario, entrada, respuesta):
    """
    Guarda una conversación simple
    """
    memoria = cargar_memoria()

    registro = {
        "timestamp": datetime.now().isoformat(),
        "usuario": usuario,
        "entrada": entrada,
        "respuesta": respuesta
    }

    memoria["conversaciones"].append(registro)
    guardar_memoria(memoria)


def guardar_hecho_importante(texto):
    """
    Guarda un hecho importante que ATLAS no debe olvidar
    """
    memoria = cargar_memoria()

    hecho = {
        "timestamp": datetime.now().isoformat(),
        "contenido": texto
    }

    memoria["hechos_importantes"].append(hecho)
    guardar_memoria(memoria)


def obtener_resumen_memoria():
    """
    Devuelve un resumen corto de la memoria
    """
    memoria = cargar_memoria()

    return {
        "total_conversaciones": len(memoria["conversaciones"]),
        "hechos_importantes": len(memoria["hechos_importantes"]),
        "usuarios_registrados": len(memoria["usuarios"])
    }
