import numpy as np
import intersections
import paths
import math


def test_square(plt):
    c, points = np.asarray(paths.show_square(plt))
    return c, points


def test_maze(plt):
    c, points = np.asarray(paths.show_maze(plt))
    return c, points


def test_v(plt):
    c, points = np.asarray(paths.show_v(plt))
    return c, points


def test_sin(plt):
    c, points = np.asarray(paths.show_sin(plt))
    return c, points


def test_maze_hard(plt):
    c, points = np.asarray(paths.show_maze_hard(plt))
    return c, points


def check_if_passed(plt, x, y, argument):
    border = list(paths.default_border(plt))

    if argument == '1':
        c, points = test_square(plt)
    elif argument == '2':
        c, points = test_maze(plt)
    elif argument == '3':
        c, points = test_v(plt)
    elif argument == '4':
        c, points = test_sin(plt)
    elif argument == '5':
        c, points = test_maze_hard(plt)

    points.append(border)

    xn = np.asarray(x)
    yn = np.asarray(y)

    mistakes = []
    idx = 0
    label = 'Mistakes'
    for point in points:
        xp0, yp0 = intersections.intersection(xn, yn, point[0], point[1])
        plt.plot(xp0, yp0, 'or', label=label)
        mistakes = np.append(mistakes, xp0)
        idx += 1
        label = ''

    if math.pow((x[-1] - c[0]), 2) + math.pow((y[-1] - c[1]), 2) <= math.pow(c[2], 2):
        if not mistakes:
            return True
    return False


