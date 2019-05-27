import matplotlib.pyplot as plt
import paths
import sys


argument = sys.argv[1]
paths.default_border(plt)

if argument == '1':
    paths.show_square(plt)
elif argument == '2':
    paths.show_maze(plt)
elif argument == '3':
    paths.show_v(plt)
elif argument == '4':
    paths.show_sin(plt)
elif argument == '5':
    paths.show_maze_hard(plt)

plt.show()
