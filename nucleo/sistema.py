# nucleo/sistema.py

import os

class SistemaAtlas:
    def __init__(self):
        self.nombre = "ATLAS"
        self.version = "v1"
        self.idioma = "es"
        self.modo = "offline"  # offline | online
        self.usuario_actual = "desconocido"

        # Rutas base
        self.base_dir = os.path.expanduser("~/atlas_v1")
        self.memoria_dir = os.path.join(self.base_dir, "memoria")
        self.registros_dir = os.path.join(self.base_dir, "registros")

        self._verificar_directorios()

    def _verificar_directorios(self):
        os.makedirs(self.memoria_dir, exist_ok=True)
        os.makedirs(self.registros_dir, exist_ok=True)

    def cambiar_modo(self, modo):
        if modo in ["offline", "online"]:
            self.modo = modo

    def cambiar_usuario(self, nombre):
        self.usuario_actual = nombre

    def info(self):
        return {
            "nombre": self.nombre,
            "version": self.version,
            "idioma": self.idioma,
            "modo": self.modo,
            "usuario": self.usuario_actual
        }
