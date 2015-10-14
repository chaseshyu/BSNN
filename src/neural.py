#  neural.py
#
#
#  Created by Phoenix on 10/13/15.
#
from tools import rotate2D, sum_vector, neg_vector


class Brain:

    def __init__(self,name,num):
        self.__name = name
        self.__ring = 1 + num
        self.__cell_num = 1 + 3*(1+num)*num
        
        self.__cells = [Cell(i,(0.,0.)) for i in range(self.__cell_num)]

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
            cell_bonds = self.__cells[i].get_Bonds()
            for k in range(len(cell_bonds)):
                bonds.append(cell_bonds[k])
        return bonds
        
    def get_AllCell(self):
        return self.__cells
        
    def get_Cell(self,ind):
        return self.__cells[ind]
    def get_CellNum(self):
        return self.__cell_num

    def move_Charge(self,ID):
        print('============= Charge release from',ID,' =============')
        over_charg = []
        cell = self.get_Cell(ID)
        bonds = cell.get_Bonds()
        for i in range(cell.get_AxonNum()):
            bond = bonds[i]
            targ_cell = self.get_Cell(bond.get_TargID())
            targ_cell.obtain_Charge(bond.get_Strength())
            if targ_cell.check_Charge():
                over_charg.append(bond.get_TargID())
            print (bond.get_Strength())
            bond.StrengthenBond()
            print ('Charge goes to: ',targ_cell.get_Name(),bond.get_Strength())
        cell.release_Charge()
        return over_charg

class Cell:

    def __init__(self,name,cord):
        self.__name = name
        self.__cord = cord
        self.__connect_to = []
        self.__connect_from = []
        self.__cell_size = 1
        self.__dendrite_num = 0
        self.__axon_num = 0
        self.__bond = []
        self.__charge = Charge(self.__cord,0.)
        self.__threshold = 1.
#        self.__indn[name] = __ind
#        print ('Create a Cell "',self.__name,'" with index:',self.__ind)
    
    def ConnectTo(self,targ):
        cord = targ.get_Cord()
        self.__axon_num += 1
        self.__connect_to.append(cord)
        self.__bond.append(Bond(self,targ))
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
    def get_Bonds(self):
        return self.__bond
    def get_BondNum(self):
        return len(self.__bond)
    def get_BondInfo(self):
        i = len(self.__bond)
        return [self.__bond[x].get_Strength() for x in range(i)]
    
    def get_BondCord(self):
        x = [self.get_Bonds[i].get_Start[0] for i in range(len(self.__bond))]
        y = [self.get_Bonds[i].get_Start[1] for i in range(len(self.__bond))]
        return x, y
    
    def get_Charge(self):
        return self.__charge
    
    def obtain_Charge(self,inte):
        self.__charge.marge(inte)
    
    def release_Charge(self):
        self.__charge.set_Inte(self.__charge.get_Inte()-self.__threshold)
        
    def check_Charge(self):
        if self.__charge.get_Inte() >= self.__threshold:
            return True

class Bond:

    def __init__(self,cell,targ):
        self.__targID = targ.get_Name()
        self.__start = cell.get_Cord()
        self.__end = targ.get_Cord()
        self.__distance = ((self.__start[0]-self.__end[0])**2+(self.__start[1]-self.__end[1])**2)**0.5
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
    def get_TargID(self):
        return self.__targID



class Charge:

    def __init__(self,cord,intensity):
        self.__cord = cord
        self.__inte = intensity

    def marge(self,pulse):
        self.__inte += pulse
    

    def move(self,bond):
        cord = bond.get_End()
        stre = bond.get_Strength()

    def get_Inte(self):
        return self.__inte

    def set_Inte(self,inte):
            self.__inte = inte





