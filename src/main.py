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

### Paramaters ###


brain_layer = 10
#

ip = 0

### Programs ###

brain2 = nr.Brain('proto',brain_layer)

print('Run 1')
brain2.get_Cell(0).obtain_Charge(1.1)
over_charg = []
if brain2.get_Cell(0).check_Charge():
    over_charg = brain2.move_Charge(0)
print('Run 2')
over_charg2 = []
num = len(over_charg)
for i in range(num):
    over_charg2.append(brain2.move_Charge(over_charg[i]))


if ip == 1:
# Get all cells
    cells = brain2.get_AllCell()
    tools.plot_cells(cells)

# Get all bonds
    bonds = brain2.get_AllBond()
    tools.plot_bonds(bonds)

    tools.plot_frame(brain_layer+1)

