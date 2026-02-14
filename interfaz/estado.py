from enum import Enum
import time

class Estado(Enum):
    INACTIVO = "inactivo"
    ESCUCHANDO = "escuchando"
    PENSANDO = "pensando"
    HABLANDO = "hablando"
    ERROR = "error"

estado_actual = Estado.INACTIVO

def cambiar_estado(nuevo_estado):
    global estado_actual
    estado_actual = nuevo_estado
    mostrar_estado()

def mostrar_estado():
    """
    En V1 solo imprime el estado.
    En V2/V3 esto se conectará a pantalla, LEDs o cara.
    """
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] ATLAS → {estado_actual.value.upper()}")
