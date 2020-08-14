from game.game import *
from montecarlo.uct import *

LARGO = 4
TABLERO_ALTO = 6
TABLERO_ANCHO = 7
t = Connect4(TABLERO_ANCHO, TABLERO_ALTO, LARGO)
a = uct(t, 6000, plot=False)

print(a)
#import os
#os.startfile("C:/Users/Admin/Desktop/mcts/tree-plot.html")