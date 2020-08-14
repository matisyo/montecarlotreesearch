import toytree
from toyplot import html

from montecarlo.nodo import Nodo
from montecarlo.uct import tree_policy, backup_negamax, default_policy, best_child


class Memcts():
    def __init__(self,game):
        self.root = Nodo(game,None)
        self.root.action = [-1,-1]
    def move(self, m):
        existia = False
        for h in self.root.hijos:
            if self.root.hijos[h].action[1]==m:
                self.root = self.root.hijos[h]
                self.root.padre = None
                existia=True
                break
        if not existia:
            print("Estado inaxesible")

    def uct(self, n, plot=False,silent=False):
        v0 = self.root
        for t in range(n):
            vi = tree_policy(v0,silent=silent)
            me = vi.state.current_player
            Δ = default_policy(vi.state)
            if Δ == me:
                Δ = -1
            elif Δ == 0:
                Δ = 0
            else:
                Δ = 1
            backup_negamax(vi, Δ)
        if plot:
            tre = toytree.tree(v0.context() + ";")
            canvas, axes = tre.draw(width=300)
            html.render(canvas, "C:/Users/Admin/Desktop/mcts/tree-plot.html")
        return best_child(v0, 0,silent=silent).action