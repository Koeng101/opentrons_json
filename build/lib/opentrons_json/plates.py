import string
from itertools import groupby

class Plate():
    def __init__(self, height:int, length:int) -> None:
        positions = []
        for letter in list(string.ascii_uppercase[0:height]):
            for number in range(length):
                positions.append((letter, number+1))
        self.height = height
        self.length = length
        self.locations = [x[0]+str(x[1]) for x in positions]
    def rows(self)-> list:
        return [list(g) for k, g in groupby(self.locations, key=lambda x: x[0])]
    def columns(self) -> list:
        return [[x for x in self.locations if x[1:] == str(num+1)] for num in range(self.length)]
    def reverse_columns(self)-> list:
        return [sorted(x, reverse=True) for x in self.columns()]
        
standard96 = Plate(8,12)
standard384 = Plate(16,24)

class TipRack(Plate):
    def __init__(self,height:int=8,length:int=12)-> None:
        super(TipRack,self).__init__(height,length)
    
    def use_tips(self,tips:list)-> str:
        self.locations = [v for i, v in enumerate(self.locations) if v not in tips]
        return tips[-1]
    
    def use_number(self,num_tips:int=8) -> str:
        for column in tip.reverse_columns():
            if len(column) >= num_tips:
                return self.use_tips(column[0:num_tips])
        raise ValueError("No more tips.")
                
                
