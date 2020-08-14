from game.game import *
from montecarlo.uct import *

LARGO = 4
TABLERO_ALTO = 6
TABLERO_ANCHO = 7
t = Connect4(TABLERO_ANCHO, TABLERO_ALTO, LARGO)
t.move(3)
t.move(4)
t.move(3)
t.move(4)
t.move(3)
t.move(4)

a = uct(t, 100, plot=True)
t.show()
print(t.current_player)
print(a)

import os
#os.startfile("C:/Users/Admin/Desktop/mcts/tree-plot.html")