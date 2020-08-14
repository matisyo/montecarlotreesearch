class Nodo():
    def __init__(self, game, a,padre=None):
        self.untried_actions = game.moves.copy()
        self.is_terminal = game.end
        self.padre = padre
        self.hijos = {}
        self.n = 0
        self.q = 0
        self.reward = 0
        self.state = game
        self.action = a

    def context(self,dp = 0):
        if self.is_terminal or not self.hijos or dp==2:
            k = "neg" if self.q < 0 else "pos"
            if dp==2:
                return f"({self.padre.action[1]}_{self.action[1]}_{k}_{self.q}_{self.n}_move:3)"
            else:
                return f"({self.action[1]}_{k}_{self.q}_{self.n}_move:3)"
        c = ", ".join([f"{self.hijos[k].context(dp+1)}:1" for k in self.hijos])
        c = f"({c})"
        return c
