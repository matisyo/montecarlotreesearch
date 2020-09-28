
import numpy as np
from montecarlo.nodo import *
from random import sample
import toytree
from toyplot import html

CP = 1#/2**.5

def uct(state, n, plot=False):
    v0 = Nodo(state,None)
    for t in range(n):
        vi = tree_policy(v0)
        me = vi.state.current_player
        Δ = default_policy(vi.state)
        if Δ==me:
            Δ=-1
        elif Δ==0:
            Δ=0
        else:
            Δ=1
        backup_negamax(vi, Δ)
    if plot:
        v0.tree_draw()
    return best_child(v0, 0).action


def tree_policy(node,silent=False):
    while not node.is_terminal:
        if len(node.untried_actions) != 0:
            return expand(node)
        else:
            node = best_child(node, CP,silent=silent)
    return node


def expand(nodo):
    a = sample(nodo.untried_actions, 1)[0]
    nodo.untried_actions.remove(a)
    tmp = nodo.state.copy()
    tmp.move(a[1])
    n = Nodo(tmp, a, nodo)
    nodo.hijos[a] = n
    return n


def best_child(nodo, c,silent=False):
    assert (len(nodo.hijos) != 0)
    actual = -200
    bc = []
    l = []
    cond = c == 0 and not nodo.padre
    for k in nodo.hijos:
        h = nodo.hijos[k]
        score = h.q / h.n + c * (2 * np.log(nodo.n) / h.n) ** .5
        if cond:
            l.append((h.action[1],f"{h.action[1]} ({round(score,2)},{h.q},{h.n})"))
            #print(, end=" ")
        if score == actual:
            bc.append(h)
        elif score > actual:
            actual = score
            bc = [h]
    assert(actual !=-200)
    if cond and not silent:
        print(', '.join([x[1] for x in sorted(l,key=lambda t: t[0])]))
        print()
    assert (len(bc) != 0)
    return sample(bc, 1)[0]


def default_policy(state):
    t = state.copy()
    while not t.end: t.move(sample(t.moves, 1)[0][1])
    return t.winner


def backup_negamax(nodo, Δ):
    while nodo:
        nodo.n += 1
        nodo.q += Δ
        Δ = Δ * -1
        nodo = nodo.padre




