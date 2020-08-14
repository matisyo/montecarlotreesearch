
from game.game import *
from minmax.minimax import *

LARGO = 3
TABLERO_ALTO = 3#6
TABLERO_ANCHO = 3#7
t = Connect4(TABLERO_ANCHO, TABLERO_ALTO, LARGO)
agente = MiniMax(t,9)
t.show()
print(t.current_player)
t2 = agente.best_move()
t.move(0)
t.show()
print(t.current_player)
t2 = agente.best_move()
print(t.current_player)
t.move(2)
t.show()