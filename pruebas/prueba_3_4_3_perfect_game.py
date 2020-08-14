from game.game import *
from memorymontecarlo.memcts import Memcts
from minmax.minimax import *
LARGO = 3
TABLERO_ALTO = 3
TABLERO_ANCHO = 4
t = Connect4(TABLERO_ANCHO, TABLERO_ALTO, LARGO)

agente = MiniMax(t,8)
t.move(2)
t.move(1)
t.move(2)
t.move(2)
t.move(1)
t.move(1)
t.move(3)
t.move(3)
t.move(3)
t.move(0)
agente.best_move()
t.move(0)
t.show()