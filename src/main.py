#!/sw/bin/python3.4
#  main.py
#  main contral of BSNN
#
#  Created by Phoenix on 10/13/15.
#  Copyright © 2015 Zranwind. All rights reserved.
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from operator import itemgetter, attrgetter, methodcaller
from ctypes import cdll

import interface as inf
import neural as nr
import tools
ip = 1

brain2 = nr.Brain('proto',5)

nx = 10
ny = 5
nz = 5
# brain(y,x)
brain1 = [[(j+1)+(i*nx) for j in range(nx)] for i in range(ny)]
brain = [ [ nr.Cell((j+1)+(i*nx),j,i) for j in range(nx) ] for i in range(ny) ]

#for i in range(ny):
#    print (brain1[i][:])

brain2.get_Cell(1).get_CellInfo()

# Initialize the connection of cells
for i in range(ny):
    for j in range(nx):
        for k in range(ny):
            for l in range(nx):
                if (i != k or j != l):
                    brain[i][j].ConnectTo(brain[k][l])

# Get all cells cord
x, y = nr.get_AllCellLocation(brain2)
# Plot the cell locations
plt.plot(x,y,'o')


#for j in range(ny):
#    for i in range(nx):
#        bonds = brain[j][i].get_Bond()
#        for k in range(len(bonds)):
#            x, y = bonds[k].get_Cord()
#            strangth = 1. - bonds[k].get_Strength()
#            color = [strangth, strangth, strangth]
#            plt.plot(x,y,color=color)
bonds = brain2.get_AllBond()
bond_num = len(bonds)
stremax = max([bonds[i].get_Strength() for i in range(bond_num)])
stremin = min([bonds[i].get_Strength() for i in range(bond_num)])
streinter = stremax - stremin

bonds = sorted(bonds, key=attrgetter('strekey'),reverse=False)

bond_crod = [bonds[i].get_Cord() for i in range(bond_num)]
bond_stre = [bonds[i].get_Strength() for i in range(bond_num)]

for i in range(bond_num):
    x, y = bond_crod[i]
    color = (stremax-bond_stre[i])/streinter
    colors = [color,color,color]
    plt.plot(x,y,color=colors)


plt.xlim(-10,10)
plt.ylim(-10,10)

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("The Title")
if ip == 1:
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

#anim = animation.FuncAnimation(fig, animate, init_func=init,frames=200, interval=20, blit=True)

#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#plt.show()






