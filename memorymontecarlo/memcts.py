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

    def uct(self, n, plot=False,silent=False,persist=False,criterion="best_child",fn=None):
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
            v0.tree_draw()
        if persist:
            ct = best_child(v0, 0, silent=silent, persist=persist)
            return ct[0].action, ct[1]
        if criterion == "best_child":
            return best_child(v0, 0, silent=silent, persist=persist).action
        return choose_child(v0, 0,fn).action


from random import sample
def choose_child(nodo, c,fn):
    assert (len(nodo.hijos) != 0)
    actual = -200
    bc = []
    for k in nodo.hijos:
        h = nodo.hijos[k]
        score = fn(h)
        if score == actual:
            bc.append(h)
        elif score > actual:
            actual = score
            bc = [h]
    assert(actual !=-200)
    assert (len(bc) != 0)
    return sample(bc, 1)[0]
