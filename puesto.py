class PuestoDeJuego:
    def __init__(self, jugador):
        self._jugador = jugador
        self._palabra = ''

    def tomar_palabra(self, balde):
        palabra = balde.tomar_palabra()
        self._palabra = palabra
        print(palabra)
    