
import matplotlib.pyplot as plot
import numpy as np
import os

# red for quadratic, green for linear
a, b, c = input("Enter coefficents: ").split(',')
a = int(a)
b = int(b)
c = int(c)
x = np.linspace(-10, 9, 100)
linear = [a * xi + b for xi in x]
quadratic = [a * xi**2 + b * xi + c for xi in x]
plot.plot(x, linear, 'green', label=f'{a}x + {b}')
plot.plot(x, quadratic, 'red', label=f'{a}x^2 + {b}x + {c}')
plot.xlabel('x values')
plot.ylabel('y values')
plot.title('Linear and quadratic equations')
plot.legend()
plot.grid(True)

path = "equations"
if not os.path.exists(path):
    os.mkdir(path)

plot.savefig('equations/graph.png')

# plot.show()
