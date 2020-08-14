from random   import choice

class MiniMax():
    def __init__(self, game, depth=5):
        self.game = game
        self.depth = depth

    def best_move(self,silent=False):
        if self.game.end:
            return
        t = self.game
        k = -99999
        dp = self.depth
        self.me = t.current_player
        movidas = list(t.moves)

        jugada = []
        for p in movidas:
            if not silent:
                print(p[1], end=" ")
            t.move(p[1])
            tmp = self.mm(dp, False)
            if not silent:
                print(tmp, end=", ")
            if tmp > k:
                jugada = [p[1]]
                k = tmp
            elif tmp==k:
                jugada.append(p[1])
            t.unmove()
        if not silent:
            print("")

        return choice(jugada)

    def mm(self, dp, maximizingPlayer=True):

        t = self.game
        if t.end:
            if t.winner == 0:
                return 0
            if t.winner == self.me:
                return 1-dp/10000
            else:
                return -1+(self.depth-dp)/10000

        if dp == 0:
            if t.current_player == self.me:
                return -.5
            return .5

        if maximizingPlayer:
            k = -99999
            movidas = list(t.moves)
            for p in movidas:
                # print(p[1],end=" ")
                movio = t.move(p[1])

                if movio:
                    u = t.current_player
                    tmp = self.mm(dp - 1, False)
                    #t.current_player = u
                    v = t.current_player
                    if  u!=v:
                        print(u,v,dp,p,movidas, t.moves,t.last_move_pos)
                    k = max(k, tmp)
                    t.unmove()
                    if u != v:
                        print(u, v, dp, p, movidas, t.moves,t.last_move_pos)
                else:
                    print("lista mala")
            return k
        else:
            k = 99999
            movidas = list(t.moves)
            for p in movidas:
                # print(p[1],end=" ")
                movio = t.move(p[1])

                if movio:
                    u = t.current_player
                    tmp = self.mm(dp - 1, True)
                    #t.current_player = u
                    v = t.current_player
                    if  u!=v:
                        print(u,v,dp,p,movidas,t.moves,t.last_move_pos)
                    k = min(k, tmp)
                    t.unmove()
                    if u != v:
                        print(u, v, dp, p, movidas, t.moves,t.last_move_pos)

                else:
                    print("lista mala")
            return k
