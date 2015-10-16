#!/sw/bin/python3.4
#  main.py
#  main contral of BSNN
#
#  Created by Phoenix on 10/13/15.
#  Copyright © 2015 Zranwind. All rights reserved.
import numpy as np
import time

import interface as inf
import neural as nr
import dynamic as dy
import tools
### tools

#return a method
from operator import methodcaller

### Paramaters ###


brain_layer = 10
#

ip = 0

### Programs ###

def main():
    brain2 = nr.Brain('proto',brain_layer)
    cells = brain2.get_AllCell()

    nloop = 0
    
    while True:
        nloop += 1
        print('Run ',nloop)
        cell = brain2.get_Cell(brain2.get_CellNum()-1)
        
        cell.obtain_Charge(.2)
        
        if cell.check_OverCharge():

        # conduct charge to bonded cells
        # get bond info
            bonds = cell.get_Bonds()
            targIDs = [bond.get_TargID() for bond in bonds]
            bonds_stre = [bond.get_Strength() for bond in bonds]

            for i in range(len(bonds)):
                cells[targIDs[i]].obtain_Charge(bonds_stre[i])

            over_charg = []
            for i in range(len(bonds)):
                if brain2.get_Cell(targIDs[i]).check_OverCharge():
                    over_charg.append(targIDs[i])
            break




    over_chargIDs = []
    # multiprocessing start ??


    while True:
        nloop += 1
        print('Run ',nloop)
        for targID in over_charg:
            over_chargIDs.append(nr.charg_seperate(cells,targID))

        over_charg = tools.mergeList(over_chargIDs)
        print (over_charg)
        time.sleep(1)


    if ip == 1:
        # Get all cells
        cells = brain2.get_AllCell()
        tools.plot_cells(cells)

        # Get all bonds
        bonds = brain2.get_AllBond()
        tools.plot_bonds(bonds)

        tools.plot_frame(brain_layer+1)



if __name__ == '__main__':
    main()
#    so_test()
#    reload_test()


