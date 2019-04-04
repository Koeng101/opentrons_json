import string
from itertools import groupby

import string
class Plate():
    def __init__(self, height:int=8, length:int=12,locations:list=[]) -> None:
        positions = []
        for letter in list(string.ascii_uppercase[0:height]):
            for number in range(length):
                positions.append((letter, number+1))
        self.height = height
        self.length = length
        if locations==[]:
            self.locations = [x[0]+str(x[1]) for x in positions]
        else:
            self.locations = locations

    def rows(self)-> list:
        return [list(g) for k, g in groupby(self.locations, key=lambda x: x[0])]
    def columns(self) -> list:
        return [[x for x in self.locations if x[1:] == str(num+1)] for num in range(self.length)]
    def reverse_columns(self)-> list:
        return [sorted(x, reverse=True) for x in self.columns()]
    def flat_columns(self) -> list:
        return [item for sublist in self.columns() for item in sublist]


    def subcolumns(self)-> list:
        if self.height%2 != 0:
            raise StandardError('Not compatible with multichannel')
        spaces = int(self.height/8)
        subcolumns=[]
        for column in self.columns():
            for space in range(spaces):
                count = space
                subcolumn=[]
                while count < len(column):
                    subcolumn.append(column[count])
                    count+=spaces
                subcolumns.append(subcolumn)
        return subcolumns
    
    def use_wells(self,tips:list)-> str:
        self.locations = [v for i, v in enumerate(self.locations) if v not in tips]
        return tips

    def use_number(self,num_wells:int=8,columns=None) -> str:
        if columns == None:
            columns=self.reverse_columns()
        for column in columns:
            if len(column) >= num_wells:
                return self.use_wells(column[0:num_wells])
        raise ValueError("No more tips.")

    
def efficient_transfer(derived,full=Plate().subcolumns()):
    derived = Plate(locations=derived).subcolumns()
    transfers=[]
    well = None
    for index,subcolumn in enumerate(derived):
        tip_count = 1
        loc_num=0
        wells=[]
        for well_index,well in enumerate(subcolumn):

            # Check if this is a new well
            wells.append(well)

            # Check that this is not the last location we can pull from 
            if not well_index+2 > len(subcolumn):
                loc_num = full[index].index(subcolumn[well_index+1])-well_index

            # If last location, add tips and location, reset new well
            if loc_num != 1:
                transfers.append((tip_count,wells))
                wells=[]
                tip_count=0

            loc_num=0
            tip_count+=1
    return transfers

def transfer_data(volume,transfers,to_plate_layout=Plate(),tipbox=Plate()):
    to = []
    tips = []
    for step in transfers:
        tips.append(tipbox.use_number(step[0])[-1])
        to+=to_plate_layout.use_number(step[0],to_plate_layout.columns())
    transfer_from = [item for sublist in [step[1] for step in transfers] for item in sublist]
    
    print(transfer_from)
    individual_transfers = [(volume,) + transfer for transfer in list(zip(tips,transfer_from,to))]
    return individual_transfers

        
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
                
                
