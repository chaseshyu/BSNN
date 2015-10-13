

def AllCellLocation(brain):
    nx = len(brain[0])
    ny = len(brain)
    x = [[brain[j][i].get_Ind()[0] for i in range(nx)] for j in range(ny)]
    y = [[brain[j][i].get_Ind()[1] for i in range(nx)] for j in range(ny)]
    return x, y
class Cell:

    def __init__(self,name,i,j):
        self.__name = name
        self.__ind = [i,j]
        self.__connect_to = []
        self.__connect_from = []
        self.__cell_size = 1
        self.__dendrite_num = 0
        self.__axon_num = 0
        self.__bond = []
#        self.__indn[name] = __ind
#        print ('Create a Cell "',self.__name,'" with index:',self.__ind)
    
    def ConnectTo(self,targ):
        ind = targ.get_Ind()
        self.__axon_num += 1
        self.__connect_to.append(ind)
        self.__bond.append(Bond(self.get_Ind(),targ.get_Ind()))
        targ.ConnectFrom(self)
        print ('Connect',self.__name,'to ',targ.__name)

#    def ConnectToWithName(self,name):
#        ind = self.__indn[name]
#        targ

    def ConnectFrom(self,targ):
        ind = targ.get_Ind()
        self.__dendrite_num += 1
        self.__connect_from.append(ind)
#        print ('Connect',self.__name,'from ',targ.__name)
    
    def get_CellInfo(self):
        print ()
        print ('       Cell Name: ',self.get_Name(),'( Index: ',self.get_Ind(),')')
        print ('    Connect From: ',self.get_DendriteNum(),self.get_ConnectFrom())
        print ('      Connect to: ',self.get_AxonNum(),self.get_ConnectTo())
        print ('Strength of Bond: ',self.get_BondInfo())
    
    
    def get_Name(self):
        return self.__name
    def get_Ind(self):
        return self.__ind
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
    
    def get_BondLoc(self):
        x = [self.get_Bond[i].get_Start[0] for i in range(len(self.__bond))]
        y = [self.get_Bond[i].get_Start[1] for i in range(len(self.__bond))]
        return x, y



class Bond:

    def __init__(self,inds,inde):
        self.__start = inds
        self.__end = inde
        self.__distance = ((inds[0]-inde[0])**2+(inds[1]-inde[1])**2)**0.5
        self.__strength = 1./self.__distance

    def WeakenBond(self):
        self.__strength *= 0.9
    def StrengthenBond(self):
        self.__strength *= 1.1

    def get_Start(self):
        return self.__start
    def get_End(self):
        return self.__end
    def get_Loc(self):
        return [self.__start[0],self.__end[0]], [self.__start[1],self.__end[1]]
    def get_Strength(self):
        return self.__strength
    def get_Distance(self):
        return self.__distance
