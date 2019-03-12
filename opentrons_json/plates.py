import string
from itertools import groupby

class Plate():
    def __init__(self, height:int, length:int) -> None:
        positions = []
        for letter in list(string.ascii_uppercase[0:height]):
            for number in range(length):
                positions.append((letter, number+1))
        self.positions = positions
        
        self.locations = [x[0]+str(x[1]) for x in positions]
        self.rows = [list(g) for k, g in groupby(self.locations, key=lambda x: x[0])]
        self.columns = [[x[0]+str(x[1]) for x in self.positions if x[1] == num] for num in set([x[1] for x in self.positions])]

standard96 = Plate(8,12)
standard384 = Plate(16,24)



class TipRack(Plate):
    def __init__(self,height:int,length:int,mode:str):
        super(TipRack,self).__init__(height,length)
        modes = ["single_single","multi_multi","multi_range"]
        if mode not in modes:
            raise ValueError("Mode not in modes")
        self.mode = mode


