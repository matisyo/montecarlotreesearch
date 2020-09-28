import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors

class Nodo():
    def __init__(self, game, a,padre=None):
        self.untried_actions = game.moves.copy()
        self.is_terminal = game.end
        self.padre = padre
        self.splits = game.ancho
        self.hijos = {}
        self.n = 0
        self.q = 0
        self.reward = 0
        self.state = game
        self.action = a

    def _tree_draw(self, x=0, y=0, width=4, depth_dist=5):
        segments = []
        xn = x + depth_dist
        yn = y + width
        for hijo in self.hijos:
            yi = yn - width / self.splits * (hijo[1]+1)
            segments.append([[x, y], [xn, yi]])
            segments += self.hijos[hijo]._tree_draw( xn, yi, width / self.splits)
        return segments

    def tree_draw(self):
        depth_dist = 5
        width_dist = 5
        segs = self._tree_draw(width=width_dist, depth_dist=depth_dist)

        colors = [mcolors.to_rgba(c) for c in plt.rcParams['axes.prop_cycle'].by_key()['color']]
        line_segments = LineCollection(segs, linewidths=1, colors=colors, linestyle='solid')

        fig, ax = plt.subplots(figsize=(9, 7))
        ax.set_xlim(-1, max([h for (_, _), (h, _) in segs]) + 1)
        ax.set_ylim(-.5, max([h for (_, _), (_, h) in segs]) + 1)
        ax.add_collection(line_segments)
        plt.show()