import random

class BaldeDeNombres:
    def __init__(self):
        self._nombres_disponibles = ["Pera roja", "Lector ciego", "Nutria bebé", "Hombre invisible", 
        "Tu nombre", "El vecino", "Spiderman", "Hulk"]

    def tomar(self):
        nombre_aleatorio = random.choice(self._nombres_disponibles)
        self._nombres_disponibles.remove(nombre_aleatorio)
        return nombre_aleatorio    

    def devolver(self, nombre):
        self._nombres_disponibles.append(nombre)
    