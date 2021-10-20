class Notificador:
    def __init__(self, sio):
        self._sio = sio
    
    def notificar_listas(self, lista_jugadores):
        lista_de_estados_jugadores = []
        for jugador in lista_jugadores:
            lista_de_estados_jugadores.append(jugador.to_dict())
        
        for jugador in lista_jugadores:
            self._sio.emit('jugadores', {
                'yo': jugador.to_dict(), 
                'jugadores': lista_de_estados_jugadores
                }, room=jugador.sid)