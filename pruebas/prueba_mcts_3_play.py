from game.game import *
from minmax.minimax import MiniMax
from montecarlo.uct import *

LARGO = 4
TABLERO_ALTO = 6
TABLERO_ANCHO = 7

t = Connect4(TABLERO_ANCHO, TABLERO_ALTO, LARGO)
agente = MiniMax(t,4)
t.move(3)
t.move(6)
t.move(3)
t.move(5)
t.move(3)
t.move(3)
t.move(2)
t.move(3)

t2 = agente.best_move()
a = uct(t, 6000, plot=False)
print(a,t.current_player)
t.show()
#t.show()
#print(a)

#import os
#os.startfile("C:/Users/Admin/Desktop/mcts/tree-plot.html")