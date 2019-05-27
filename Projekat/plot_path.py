import matplotlib.pyplot as plt
import pandas
import check_path as cp
import sys

x = []
y = []

df = pandas.read_csv('path', sep=',')
data = df.values
for row in data:
    x.append(int(row[1]))
    y.append(int(row[2]))

plt.plot(x, y, 'b-', label='Your path')

argument = sys.argv[1]

passed = cp.check_if_passed(plt, x, y, argument)

plt.xlabel('x')
plt.ylabel('y')
if passed:
    plt.title('Great job! Try next one.')
else:
    plt.title('Give it another try.')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=-1.)

plt.show()
