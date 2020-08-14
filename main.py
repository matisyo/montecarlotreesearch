import pygame, sys
from pygame.locals import *
from game.game import *
from memorymontecarlo.memcts import Memcts
from minmax.minimax import *
from montecarlo.uct import uct


def calculate_pos(m, candidatos):
    tmp = [p for p in candidatos if m == p[1]]
    if len(tmp) == 0:
        return -1,-1
    b, a = tmp[0]
    a, b = int((a + .5) * (ANCHO // TABLERO_ANCHO)), int((b + .5) * (ALTO // TABLERO_ALTO))
    return a, b

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

ALTO = 400
ANCHO = 500
LARGO = 4
TABLERO_ALTO = 6
TABLERO_ANCHO = 7
t = Connect4(TABLERO_ANCHO, TABLERO_ALTO, LARGO)
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
windowSurface.fill(WHITE)

PLAYER_1 = 1 #humano
PLAYER_1 = 3 #MCTS
PLAYER_2 = 1 #MINIMAX

ai_prendida=True
ai_mcts = True
agente = MiniMax(t,4)
agentemmc = Memcts(t)

for i in range(TABLERO_ALTO):
    for j in range(TABLERO_ANCHO):
        a, b = int((j + .5) * (ANCHO // TABLERO_ANCHO)), int((i + .5) * (ALTO // TABLERO_ALTO))
        pygame.draw.circle(windowSurface, BLACK, (a, b), 20)
pygame.display.update()


def draw_circle(t2, t, color=RED):
    a, b = calculate_pos(t2, t.moves)
    pygame.draw.circle(windowSurface, color, (a, b), 20)
    t.move(t2)
    print(t2)
    agentemmc.move(t2)
    pygame.display.update()

PLAYER_TURN = 1
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if PLAYER_TURN==1 and not t.end:
            color = BLUE
            if PLAYER_1==1:
                if event.type == MOUSEBUTTONDOWN and not t.end:
                    jugador_nro = t.current_player
                    x, y = pygame.mouse.get_pos()
                    m = int(x // (ANCHO / TABLERO_ANCHO))
                    a,b = calculate_pos(m, t.moves)
                    tmp = [p for p in t.moves if m == p[1]]
                    if a == -1:
                        continue
                    pygame.draw.circle(windowSurface, color, (a, b), 20)
                    t.move(m)
                    pygame.display.update()
                    PLAYER_TURN = 2
            elif PLAYER_1 == 2:
                t2 = uct(t, 6000, plot=False)[1]
                print(t2)
                draw_circle(t2, t, color)
                PLAYER_TURN=2

            elif PLAYER_1 == 3:
                t2 = agentemmc.uct(3000, plot=False)[1]
                print(t2)
                draw_circle(t2, t, color)
                PLAYER_TURN=2
            else:
                t2 = agente.best_move()
                print(t2)
                draw_circle(t2, t, color)
                PLAYER_TURN = 2

            if PLAYER_TURN == 2 and not t.end:
                color = RED
                if PLAYER_2 == 1:
                    if event.type == MOUSEBUTTONDOWN:
                        jugador_nro = t.current_player
                        x, y = pygame.mouse.get_pos()
                        m = int(x // (ANCHO / TABLERO_ANCHO))
                        a, b = calculate_pos(m, t.moves)
                        tmp = [p for p in t.moves if m == p[1]]
                        if a == -1:
                            continue
                        pygame.draw.circle(windowSurface, color, (a, b), 20)
                        t.move(m)
                        pygame.display.update()
                        PLAYER_TURN = 1
                elif PLAYER_2 == 2:
                    t2 = uct(t, 3600, plot=False)[1]
                    print(t2)
                    draw_circle(t2, t, color)
                    PLAYER_TURN = 1
                elif PLAYER_2 == 3:
                    t2 = agentemmc.uct(3000, plot=False)[1]
                    print(t2)
                    draw_circle(t2, t, color)
                    PLAYER_TURN = 1
                else:
                    t2 = agente.best_move()
                    print(t2)
                    draw_circle(t2, t, color)
                    PLAYER_TURN = 1

#print(t.winner)