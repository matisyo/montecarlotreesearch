from time import sleep
import pygame, sys
from pygame.locals import *
from game.game import *
from memorymontecarlo.memcts import Memcts
from minmax.minimax import *
from montecarlo.uct import uct
from film.animate import *

def calculate_pos(m, candidatos):
    tmp = [p for p in candidatos if m == p[1]]
    if len(tmp) == 0:
        return -1,-1
    b, a = tmp[0]
    moveset.append([a,b])
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

agente = MiniMax(t,4)
agentemmc = Memcts(t)

for i in range(TABLERO_ALTO):
    for j in range(TABLERO_ANCHO):
        a, b = int((j + .5) * (ANCHO // TABLERO_ANCHO)), int((i + .5) * (ALTO // TABLERO_ALTO))
        pygame.draw.circle(windowSurface, BLACK, (a, b), 20)
pygame.display.update()

moveset = []
def draw_circle(t2, t, mcts_enable,color=RED):
    a, b = calculate_pos(t2, t.moves)
    pygame.draw.circle(windowSurface, color, (a, b), 20)
    t.move(t2)
    print(t2)
    if mcts_enable:
        agentemmc.move(t2)
    pygame.display.update()

def draw_circle_player(t2, t, mcts_enable,color=RED):
    a, b = calculate_pos(t2, t.moves)
    tmp = [p for p in t.moves if t2 == p[1]]
    if a == -1:
        return
    pygame.draw.circle(windowSurface, color, (a, b), 20)
    t.move(t2)
    if mcts_enable:
        agentemmc.move(t2)
    pygame.display.update()


game_vars = {'PLAYER':1,'MCTS_ENABLE':True,'color':RED}
def move_mcts(game_vars,event):
    t2 = agentemmc.uct(150, plot=False)[1]
    print(t2)
    draw_circle(t2, t, game_vars['MCTS_ENABLE'],game_vars['color'])
    game_vars['PLAYER'] = 1 if game_vars['PLAYER'] == 2 else 2

def move_player(game_vars,event):
    if event.type==MOUSEBUTTONDOWN:
        jugador_nro = t.current_player
        x, y = pygame.mouse.get_pos()
        m = int(x // (ANCHO / TABLERO_ANCHO))
        print(m)
        draw_circle_player(m,t,game_vars['MCTS_ENABLE'],game_vars['color'])
        game_vars['PLAYER'] = 1 if game_vars['PLAYER'] == 2 else 2

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_dissplay(text):
    largeText = pygame.font.Font("freesansbold.ttf", 25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((ANCHO/2), (ALTO/2))
    #TextRect.center = screen.get_rect().center
    windowSurface.blit(TextSurf, TextRect)

player_1 = move_mcts
player_2 = move_player
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if game_vars['PLAYER'] == 1 and not t.end:
            game_vars['color'] = BLUE
            player_1(game_vars,event)

        if game_vars['PLAYER'] == 2 and not t.end:
            game_vars['color'] = RED
            player_2(game_vars,event)

        if t.end:
            message_dissplay(f"Gano jugador {'AZUL' if t.winner==1 else 'ROJO'}")
            pygame.display.update()
            print(moveset)
            game_drawing(moveset, "partida", TABLERO_ANCHO, TABLERO_ALTO)
            sleep(2)
            pygame.quit()
            sys.exit()
#print(t.winner)