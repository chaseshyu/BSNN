#!/sw/bin/python3.4
#  main.py
#  main contral of BSNN
#
#  Created by Phoenix on 10/13/15.
#  Copyright © 2015 Zranwind. All rights reserved.
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from ctypes import cdll

import interface as inf
import neural as nr
a = nr.Cell('a',1,1)
b = nr.Cell('b',1,2)
c = nr.Cell('c',1,3)

nx = 10
ny = 5
nz = 5
# brain(y,x)
brain1 = [[(j+1)+(i*nx) for j in range(nx)] for i in range(ny)]
brain = [ [ nr.Cell((j+1)+(i*nx),j,i) for j in range(nx) ] for i in range(ny) ]

for i in range(ny):
    print (brain1[i][:])

brain[3][2].get_CellInfo()

# Initialize the connection of cells
for i in range(ny):
    for j in range(nx):
        for k in range(ny):
            for l in range(nx):
                if (i != k or j != l):
                    brain[i][j].ConnectTo(brain[k][l])

brain[3][2].get_CellInfo()

# Plot the cell locations
x, y = nr.AllCellLocation(brain)
plt.plot(x,y,'o')


for j in range(ny):
    for i in range(nx):
        bonds = brain[j][i].get_Bond()
        for k in range(len(bonds)):
            x, y = bonds[k].get_Loc()
            plt.plot(x,y)


#plt.plot([1],[2],'o')

plt.xlim(-1,10)
plt.ylim(-1,5)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("The Title")
plt.show()



# For animation
fig = plt.figure()
ax = plt.axes(xlim=(-1,10), ylim=(-1, 5))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,
anim = animation.funcanimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=true)
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()






