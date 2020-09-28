from game.game import Connect4
from minmax.minimax import MiniMax
from memorymontecarlo.memcts import Memcts
import time
from film.animate import *

def minimax_vs_memcts(largo=4,alto=6,ancho=7,depth=4,iters=150,start=0,fname="experiment0",silent=True):

    game_board = Connect4(ancho, alto, largo)
    agente = MiniMax(game_board, depth)
    agentemmc = Memcts(game_board)
    moveset = []
    start_time = time.time()
    move = agentemmc.uct(iters, plot=False)[1]
    while not game_board.end:
        # your code
        if start == 1:
            move = agente.best_move(silent=silent)
        else:
            move = agentemmc.uct(iters, plot=False,silent=silent)[1]

        tmp = [p for p in game_board.moves if move == p[1]]
        b, a = tmp[0]

        moveset.append([a, b])

        elapsed_time = time.time() - start_time
        print(f"{int(elapsed_time)}s", end="\r")
        start = (start+1)%2
        game_board.move(move)
        agentemmc.move(move)

    game_drawing(moveset, fname+f"_{game_board.winner}", ancho, alto)
    return game_board.winner


def memcts_vs_memcts(largo=4,alto=6,ancho=7,iters1=150,iters2=150,start=0,fname="experiment0",silent=True):

    game_board = Connect4(ancho, alto, largo)
    agentemmc1 = Memcts(game_board)
    agentemmc2 = Memcts(game_board)

    move = agentemmc1.uct(iters1, plot=False)[1]
    move = agentemmc2.uct(iters2, plot=False)[1]

    moveset = []
    start_time = time.time()
    while not game_board.end:
        # your code
        if start == 0:
            move = agentemmc1.uct(iters1, plot=False,silent=silent)[1]
        else:
            move = agentemmc2.uct(iters2, plot=False,silent=silent)[1]

        tmp = [p for p in game_board.moves if move == p[1]]
        b, a = tmp[0]

        moveset.append([a, b])

        elapsed_time = time.time() - start_time
        print(f"{int(elapsed_time)}s", end="\r")
        start = (start+1)%2
        game_board.move(move)
        agentemmc1.move(move)
        agentemmc2.move(move)

    game_drawing(moveset, fname+f"_{game_board.winner}", ancho, alto)
    return game_board.winner