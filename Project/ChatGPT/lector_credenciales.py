import json


def cargar_credenciales():
    try:
        with open('config.json', 'r') as archivo_config:
            config = json.load(archivo_config)
            return config
    except FileNotFoundError:
        print("El archivo 'config.json' no se encontró.")
        return None
    

