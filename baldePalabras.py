import requests
import random

class BaldeDePalabras:
    def __init__(self):
        self._palabras_disponibles = ["MERCURIO", "MOCHILA", "VECINDAD", "COMEDIA", "DOCTOR", "PALABRAS", "ENTRETENER", "AHORCADO"]

    # def guardar_palabras(self):
    #     URL = 'https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt'
    #     solicitud = requests.get(URL) 
    #     self._palabras = solicitud.text.split("\n")

    def tomar_palabra(self):
        palabra_aleatoria = random.choice(self._palabras_disponibles)
        return palabra_aleatoria        