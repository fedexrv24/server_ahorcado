from puesto import PuestoDeJuego
from jugador import Jugador
from baldePalabras import BaldeDePalabras
from balde import BaldeDeNombres
from notificador import Notificador

class Juego:
    def __init__(self, notificador):
        self._jugadores = []
        self._puestos_de_juego = []
        self._notificador = notificador
        self._balde = BaldeDeNombres()
        self._balde_palabras = BaldeDePalabras()       

    def agregar_jugador(self, sid):
        nuevo_jugador = Jugador(sid, self._balde.tomar())
        self._jugadores.append(nuevo_jugador)
        self._notificador.notificar_listas(self._jugadores)

    def sentar_jugador(self, sid):
        for jugador in self._jugadores:
            
            if sid == jugador.sid:
                jugador_sentado = PuestoDeJuego(jugador)
                self._puestos_de_juego.append(jugador_sentado)     
                        
                break
    

        self._notificador.notificar_listas(jugador_sentado)

    def dar_palabras(self):
        if len(self._puestos_de_juego) >=2 and len(self._puestos_de_juego) == len(self._jugadores):
            for puesto in self._puestos_de_juego:
                puesto.tomar_palabra(self._balde_palabras)
     
    def quitar_jugador(self, sid):
        for jugador in self._jugadores:
            if sid == jugador.sid:
                if jugador in self._puestos_de_juego:
                    print('El es jugador',jugador)
                    self._puestos_de_juego.remove(jugador)
                    print(len(self._puestos_de_juego))
                    break          
        