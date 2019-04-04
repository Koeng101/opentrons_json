from . import plates
def data_transfer_comprehension(data_transfer, old_plate=plates.Plate(),new_plate=plates.Plate()):
    output=[]
    for transfer in data_transfer:
        original_index = old_plate.flat_columns().index(transfer[1])
        new_index = new_plate.flat_columns().index(transfer[2])
        for i in range(transfer[0]):
            old_well = old_plate.flat_columns()[i+original_index]
            new_well = new_plate.flat_columns()[i+new_index]
            output.append((old_well,new_well))
    return output


def efficient_transfer(derived,full=plates.Plate().subcolumns()):
    derived = plates.Plate(locations=derived).subcolumns()
    transfers=[]
    well = None
    for index,subcolumn in enumerate(derived):
        tip_count = 1
        loc_num=0
        wells=[]
        counter = 0
        for well_index,well in enumerate(subcolumn):

            # Check if this is a new well
            wells.append(well)

            # Check that this is not the last location we can pull from 
            if not well_index+2 > len(subcolumn):
                loc_num = full[index].index(subcolumn[well_index])-well_index-counter

            # If last location, add tips and location, reset new well
            if loc_num != 0:
                if loc_num != 50:
                    transfers.append((len(wells[:-1]),wells[:-1]))
                    wells=[wells[-1]]
                    tip_count=0
                    counter=loc_num
                else:
                    transfers.append((len(wells),wells))
                    wells=[]
                    tip_count=0
                    counter=loc_num

            loc_num=50
            tip_count+=1
    return transfers

