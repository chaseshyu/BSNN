#  tools.py
#  
#
#  Created by Phoenix on 10/14/15.
#
from math import cos, sin, radians
import matplotlib.pyplot as plt
from operator import methodcaller

import neural as nr

def rotate2D(self, theta):
    """ Rotate this vector by theta in degrees.
        
        Returns a new vector.
        """
    theta = radians(theta)
    # Just applying the 2D rotation matrix
    dc, ds = cos(theta), sin(theta)
    x, y = self
    x, y = dc*x - ds*y, ds*x + dc*y
    return x, y

def sum_vector(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1+x2, y1+y2

def neg_vector(v):
    x, y = v
    return -x, -y

def mergeList(lists):
    a = []
    for i in lists: a += i
    return list(set(a))

### for visualize

def plot_frame(num):
    plt.xlim(-1.*num,num)
    plt.ylim(-1.*num,num)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("The Brain")
    plt.show()

def plot_cells(cells):
    cell_num = len(cells)
    x = [cells[i].get_Cord()[0] for i in range(cell_num)]
    y = [cells[i].get_Cord()[1] for i in range(cell_num)]
    plt.plot(x,y,'o')

def plot_bonds(bonds):
    bond_num = len(bonds)
    stremax = max([bonds[i].get_Strength() for i in range(bond_num)])
    stremin = min([bonds[i].get_Strength() for i in range(bond_num)])
    streinter = stremax - stremin

    bonds = sorted(bonds, key=methodcaller('get_Strength'),reverse=False)

    bond_crod = [bonds[i].get_Cord() for i in range(bond_num)]
    bond_stre = [bonds[i].get_Strength() for i in range(bond_num)]

    for i in range(bond_num):
        x, y = bond_crod[i]
        color = (stremax-bond_stre[i])/streinter
        colors = [color,color,color]
        plt.plot(x,y,color=colors)