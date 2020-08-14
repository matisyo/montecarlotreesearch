import numpy as np
import random


class Connect4():
    def __init__(self, ancho, alto, largo, new_game=True):
        self.last_move = [0 for i in range(100)]
        self.last_move_pos = -1
        self.player1 = 1
        self.player2 = 2
        self.unclear = 0
        self.outside = -1

        self.end = False
        self.winner = 0

        self.current_player = self.player1

        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        if new_game:
            self.moves = set([(self.alto - 1, j) for j in range(self.ancho)])
            self.init_map()

        self.mx_col = np.array([i for i in range(self.largo)])
        self.my_col = np.zeros(self.largo).astype(int) + self.largo - 1

        self.mx_row = np.zeros(self.largo).astype(int) + self.largo - 1
        self.my_row = np.array([i for i in range(self.largo)])

        self.mx_diag_2 = np.array([self.largo - 1 - 1 + self.largo - i for i in range(self.largo)])

    def init_map(self):
        tx = (self.alto + 2 * (self.largo - 1))
        ty = (self.ancho + 2 * (self.largo - 1))

        self.mapa = np.zeros(
            tx * ty
        ).reshape(tx, ty) + self.outside

        for i in range(self.alto):
            for j in range(self.ancho):
                self.mapa[i + self.largo - 1][j + self.largo - 1] = self.unclear

    def win_condition(self, x, y):
        v = self.check_row(x, y)
        v = v or self.check_col(x, y)
        v = v or self.check_diag_1(x, y)
        v = v or self.check_diag_2(x, y)
        return v

    def check_col(self, x, y):
        mask_x = self.mx_col + x
        mask_y = self.my_col + y

        for i in range(self.largo):
            if (self.mapa[mask_x + i, mask_y] == self.current_player).sum() == self.largo:
                return True
        return False

    def check_row(self, x, y):

        mask_x = self.mx_row + x
        mask_y = self.my_row + y

        for i in range(self.largo):
            if (self.mapa[mask_x, mask_y + i] == self.current_player).sum() == self.largo:
                return True
        return False

    def check_diag_1(self, x, y):
        mask_x = self.mx_col + x
        mask_y = self.mx_col + y

        for i in range(self.largo):
            if (self.mapa[mask_x + i, mask_y + i] == self.current_player).sum() == self.largo:
                return True
        return False

    def check_diag_2(self, x, y):
        mask_x = self.mx_diag_2 + x
        mask_y = self.mx_col + y
        for i in range(self.largo):
            if (self.mapa[mask_x - i, mask_y + i] == self.current_player).sum() == self.largo:
                return True
        return False

    def unmove(self):
        value = self.last_move_pos
        if value == -1:
            print("No jugaste nada no te doy CTRL+Z")
            return
        value = self.last_move[self.last_move_pos]
        self.last_move_pos -= 1

        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

        self.end = False
        self.winner = 0

        tmp = [(a, b) for a, b in self.moves if b == value]

        if len(tmp) == 0:
            x, y = 0, value
        else:
            x, y = tmp[0]
            self.moves.remove((x, y))
            x, y = x + 1, y
        self.mapa[x + self.largo - 1][y + self.largo - 1] = 0
        self.moves.add((x, y))

    def move(self, value):
        if self.end:
            return False
        tmp = [(a, b) for a, b in self.moves if b == value]
        if len(tmp) != 0:
            self.last_move_pos += 1
            self.last_move[self.last_move_pos] = value
            x, y = tmp[0]
            self.moves.remove((x, y))
            if x != 0:
                self.moves.add((x - 1, y))
            self.mapa[x + self.largo - 1][y + self.largo - 1] = self.current_player
            if self.win_condition(x, y):
                self.end = True
                self.winner = self.current_player
            #else:
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2
        if len(self.moves) == 0:
            self.end = True

        return len(tmp) != 0

    def copy(self):
        clon = Connect4(self.ancho, self.alto, self.largo, new_game=False)
        clon.end = self.end
        clon.winner = self.winner
        clon.current_player = self.current_player
        clon.mapa = self.mapa.copy()
        clon.moves = self.moves.copy()

        return clon


    def show(self):
        k = self.largo - 1
        kk = -1 * k
        print(self.mapa[k:kk, k:kk])