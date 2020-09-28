import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update_drawings(p):
    i, j, t, ax = p
    if t % 2 == 0:
        s1, = ax.plot(i + .5, j + .5, 'o', markersize=30, markeredgecolor=(0, 0, 0), markerfacecolor='w',
                      markeredgewidth=2)
    else:
        s2, = ax.plot(i + .5, j + .5, 'o', markersize=30, markeredgecolor=(0, 0, 0), markerfacecolor='k',
                      markeredgewidth=2)

def game_drawing(moves, fname='game', width=3, height=5):
    fig = plt.figure(figsize=[width, height])
    fig.patch.set_facecolor((1, 1, .8))

    ax = fig.add_subplot(111)

    # draw the grid
    for x in range(width + 1):
        ax.plot([x, x], [0, height], 'k')
    for y in range(height + 1):
        ax.plot([0, width], [y, y], 'k')

    # scale the axis area to fill the whole figure
    ax.set_position([0, 0, 1, 1])

    # get rid of axes and everything (the figure background will show through)
    ax.set_axis_off()

    # scale the plot area conveniently (the board is in 0,0..18,18)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)

    moves = [[a, height-1-b, i, ax] for i, (a, b) in enumerate(moves)]
    anim = FuncAnimation(fig, update_drawings, frames=moves, interval=500)
    anim.save(f'videos/{fname}.mp4')