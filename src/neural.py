#  neural.py
#
#
#  Created by Phoenix on 10/13/15.
#
from tools import rotate2D, sum_vector, neg_vector

def get_AllCellLocation(self):
    len = self.get_CellNum()
    x = [self.get_Cell(i).get_Cord()[0] for i in range(len)]
    y = [self.get_Cell(i).get_Cord()[1] for i in range(len)]
    return x, y

class Brain:

    def __init__(self,name,num):
        self.__name = name
        self.__ring = 1 + num
        self.__cell_num = 1 + 3*(1+num)*num
        
        self.__cells = [Cell(i,0.,0.) for i in range(self.__cell_num)]

# Set the coordinate of cells
        self.__cells[0].set_Cord((0.,0.,))
        cell_count = 1

        for i in range(num):
            vect1 = (1.*(i+1),0.)
            cell_count += 1
            self.__cells[cell_count-1].set_Cord(vect1)
            vect2 = rotate2D((1.,0.),120)
    
            for j in range(i+1):
                vect1 = sum_vector(vect1,vect2)
                cell_count += 1
                self.__cells[cell_count-1].set_Cord(vect1)
        
            vect2 = rotate2D(vect2,60)
            
            for j in range(i+1):
                vect1 = sum_vector(vect1,vect2)
                cell_count += 1
                self.__cells[cell_count-1].set_Cord(vect1)
            
            vect2 = rotate2D(vect2,60)

            for j in range(i):
                vect1 = sum_vector(vect1,vect2)
                cell_count += 1
                self.__cells[cell_count-1].set_Cord(vect1)
        
            for j in range(3*(i+1)):
                cell_count += 1
                cord = neg_vector(self.__cells[cell_count-1 - 3*(i+1)].get_Cord())
                self.__cells[cell_count-1].set_Cord(cord)

# set initial connection of cells
        for i in range(self.__cell_num):
            for j in range(self.__cell_num):
                if i != j:
                    self.__cells[i].ConnectTo(self.__cells[j])
        
    def get_AllBond(self):
        bonds = []
        for i in range(self.__cell_num):
            cell_bonds = self.__cells[i].get_Bond()
            for k in range(len(cell_bonds)):
                bonds.append(cell_bonds[k])
        return bonds
        
        
    def get_Cell(self,ind):
        return self.__cells[ind]
    def get_CellNum(self):
        return self.__cell_num

class Cell:

    def __init__(self,name,i,j):
        self.__name = name
        self.__cord = (i,j)
        self.__connect_to = []
        self.__connect_from = []
        self.__cell_size = 1
        self.__dendrite_num = 0
        self.__axon_num = 0
        self.__bond = []
#        self.__indn[name] = __ind
#        print ('Create a Cell "',self.__name,'" with index:',self.__ind)
    
    def ConnectTo(self,targ):
        cord = targ.get_Cord()
        self.__axon_num += 1
        self.__connect_to.append(cord)
        self.__bond.append(Bond(self.get_Cord(),targ.get_Cord()))
        targ.ConnectFrom(self)
#        print ('Connect',self.__name,'to ',targ.__name)

#    def ConnectToWithName(self,name):
#        ind = self.__indn[name]
#        targ

    def ConnectFrom(self,targ):
        cord = targ.get_Cord()
        self.__dendrite_num += 1
        self.__connect_from.append(cord)
#        print ('Connect',self.__name,'from ',targ.__name)
    
    def get_CellInfo(self):
        print ()
        print ('       Cell Name: ',self.__name,'( Cord: ',self.__cord,')')
        print ('    Connect From: ',self.__dendrite_num,self.__connect_from)
        print ('      Connect to: ',self.__axon_num,self.__connect_to)
        print ('Strength of Bond: ',self.get_BondInfo())
    
    
    def get_Name(self):
        return self.__name
    def get_Cord(self):
        return self.__cord
    def set_Cord(self,cord):
        self.__cord = cord
    def get_AxonNum(self):
        return self.__axon_num
    def get_DendriteNum(self):
        return self.__dendrite_num
    def get_ConnectFrom(self):
        return self.__connect_from
    def get_ConnectTo(self):
        return self.__connect_to
    def get_Bond(self):
        return self.__bond
    def get_BondNum(self):
        return len(self.__bond)
    def get_BondInfo(self):
        i = len(self.__bond)
        return [self.__bond[x].get_Strength() for x in range(i)]
    
    def get_BondCord(self):
        x = [self.get_Bond[i].get_Start[0] for i in range(len(self.__bond))]
        y = [self.get_Bond[i].get_Start[1] for i in range(len(self.__bond))]
        return x, y



class Bond:

    def __init__(self,cords,corde):
        self.__start = cords
        self.__end = corde
        self.__distance = ((cords[0]-corde[0])**2+(cords[1]-corde[1])**2)**0.5
        self.__strength = 1./self.__distance
        self.strekey = 1./self.__distance

    def WeakenBond(self):
        self.__strength *= 0.9
    def StrengthenBond(self):
        self.__strength *= 1.1

    def get_Start(self):
        return self.__start
    def get_End(self):
        return self.__end
    def get_Cord(self):
        return [self.__start[0],self.__end[0]], [self.__start[1],self.__end[1]]
    def get_Strength(self):
        return self.__strength
    def get_Distance(self):
        return self.__distance
