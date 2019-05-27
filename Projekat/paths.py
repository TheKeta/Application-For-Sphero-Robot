import numpy as np


def default_border(plt):
    x1 = np.asarray([-5, -5, 125, 125, -5])
    y1 = np.asarray([-5, 125, 125, -5, -5])

    plt.plot(x1, y1, 'k-', label='Border')
    return x1, y1


def get_finish(plt, coordinates):
    c = plt.Circle((coordinates[0], coordinates[1]), coordinates[2], color='g', label='Finish')
    ax = plt.gca()
    ax.add_patch(c)
    plt.axis('scaled')


def show_square(plt):
    x2 = np.asarray([20, 20, 100, 100, 20])
    y2 = np.asarray([-5, 100, 100, 20, 20])

    plt.plot(x2, y2, 'k-')

    center = [30, 7.5, 5]
    get_finish(plt, center)
    return center, [[x2, y2]]


def show_maze(plt):
    x0 = np.asarray([-5, 80])
    y0 = np.asarray([22.5, 22.5])

    x1 = np.asarray([40, 125])
    y1 = np.asarray([60, 60])

    x2 = np.asarray([-5, 80])
    y2 = np.asarray([97.5, 97.5])

    plt.plot(x0, y0, 'k-')
    plt.plot(x1, y1, 'k-')
    plt.plot(x2, y2, 'k-')

    center = [5, 111.25, 7.5]
    get_finish(plt, center)
    return center, [[x0, y0], [x1, y1], [x2, y2], [x2, y2]]


def show_v(plt):
    x0 = np.asarray([-5, 75, -5])
    y0 = np.asarray([15, 60, 105])

    x1 = np.asarray([15, 125, 15])
    y1 = np.asarray([-5, 60, 125])

    plt.plot(x0, y0, 'k-')
    plt.plot(x1, y1, 'k-')

    center = [5, 115, 7.5]
    get_finish(plt, center)
    return center, [[x0, y0], [x1, y1]]


def show_sin(plt):
    x0 = np.arange(-5, 125, 0.1)  # start,stop,step
    w = 0.1
    y0 = np.sin((x0 - 15) * w) * 40 + 85

    y1 = np.sin((x0 - 15) * w) * 40 + 35

    plt.plot(x0, y0, 'k-')
    plt.plot(x0, y1, 'k-')

    center = [120, 20, 5]
    get_finish(plt, center)
    return center, [[x0, y0], [x0, y1]]


def show_maze_hard(plt):
    x0 = np.asarray([-5, 15])
    y0 = np.asarray([110, 110])

    x1 = np.asarray([25, 25, 15, 15])
    y1 = np.asarray([-5, 60, 60, 95])

    x2 = np.asarray([25, 25])
    y2 = np.asarray([125, 95])

    x3 = np.asarray([35, 55, 55, 75])
    y3 = np.asarray([95, 95, 110, 110])

    x4 = np.asarray([55, 100, 100])
    y4 = np.asarray([95, 95, 75])

    x5 = np.asarray([45, 45, 75, 75, 122])
    y5 = np.asarray([20, 70, 70, 20, 20])

    x6 = np.asarray([60, 60])
    y6 = np.asarray([-5, 35])

    x7 = np.asarray([75, 115, 115, 95])
    y7 = np.asarray([50, 50, 35, 35])

    plt.plot(x0, y0, 'k-')
    plt.plot(x1, y1, 'k-')
    plt.plot(x2, y2, 'k-')
    plt.plot(x3, y3, 'k-')
    plt.plot(x4, y4, 'k-')
    plt.plot(x5, y5, 'k-')
    plt.plot(x6, y6, 'k-')
    plt.plot(x7, y7, 'k-')

    center = [120, 0, 5]
    get_finish(plt, center)
    return center, [[x0, y0], [x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5], [x6, y6], [x7, y7]]


