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

a = uct(t, 60, plot=False)
a = uct(t, 60*2, plot=False)
a = uct(t, 60*5, plot=False)
a = uct(t, 60*10, plot=False)
a = uct(t, 3600, plot=True)

#t.show()
#print(a)

#import os
#os.startfile("C:/Users/Admin/Desktop/mcts/tree-plot.html")