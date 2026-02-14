# ==============================
# CONFIGURACIÓN GENERAL ATLAS V1
# ==============================

# Nombre del asistente
ATLAS_NAME = "ATLAS"

# Idioma principal
LANGUAGE = "es"

# Wake word (futuro)
WAKE_WORD = "atlas"

# Modo de operación
OFFLINE_FIRST = True

# Modelo local Ollama
OLLAMA_MODEL = "phi3"

# Rutas del proyecto
BASE_PATH = "/home/diego/atlas_v1"

MEMORY_PATH = f"{BASE_PATH}/memoria/recuerdos.json"
LOG_PATH = f"{BASE_PATH}/registros/atlas.log"

# Voz (espeak)
VOICE_NAME = "es"

# Internet check
PING_HOST = "8.8.8.8"
PING_TIMEOUT = 1

#CONFIGURACIONES AÑADIDAS PARA WAKEWORD
IDIOMA_DEFECTO = "es"

USAR_VOZ = True
USAR_CAMARA = True
USAR_TTS = True
