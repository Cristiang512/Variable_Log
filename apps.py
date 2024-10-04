# apps.py
from django.apps import AppConfig

class BitacoraConfig(AppConfig):
    name = 'Bitacora'

    def ready(self):
        import Bitacora.signals  # Asegúrate de importar tu módulo de señales
