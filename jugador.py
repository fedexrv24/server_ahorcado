class Jugador:    
    def __init__(self, sid, nombre):
        self._sid = sid
        self._nombre = nombre
 
    @property
    def sid(self):
        return self._sid

    def to_dict(self):
        return {
            'sid': self._sid, 
            'nombre': self._nombre,
            'listo': False
        }       
