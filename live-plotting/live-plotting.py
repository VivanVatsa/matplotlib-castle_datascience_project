import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = [] 

index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))

    plt.cla()
    plt.plot(x_vals, y_vals)
    # output => random lines with random colors!!
    # why? => there are multiple lines are just stacking up & they are just being covered up and no info is seen
    # 
 
ani = FuncAnimation(plt.gcf(), animate, interval=1000) 

plt.tight_layout()
plt.show()


# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']

# plt.plot(x_vals, y_vals)
