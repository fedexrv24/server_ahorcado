import eventlet
import socketio

from juego import Juego
from jugador import Jugador
from balde import BaldeDeNombres
from notificador import Notificador
from baldePalabras import BaldeDePalabras

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

notificador = Notificador(sio)
juego = Juego(notificador)
balde = BaldeDeNombres()

@sio.event
def connect(sid, environ):
    juego.agregar_jugador(sid)

@sio.event
def saludo(sid):
    print('Hola', sid)
    sio.emit('bienvenido','Tu nombre es: '+ sid, room=None)

@sio.event
def listo(sid):
    juego.sentar_jugador(sid)
    juego.dar_palabras()    
    print(sid, 'Esta lindo.')

@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    # if sid in nombres_asignados:
    #     nombres_disponibles.append(nombres_asignados[sid])
    #     del nombres_asignados[sid]
    #     sio.emit('mostrar_lista', nombres_asignados)
    # else:
    #     pass
    
    # print('***LISTA DESCONECTADO***', nombres_disponibles)
    # print('***DICCIONARIO DESCONECTADO***', nombres_asignados)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
    
