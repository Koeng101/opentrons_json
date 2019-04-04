from opentrons_json import plates,commands
import opentrons_json
import datetime
import uuid
import json
from opentrons_json import transfer as Transfer

with open('/home/koeng/Downloads/response_1554406909932.json') as f:
    test_plate = json.load(f)

opentrons = {'uuid': '43346aba-41e0-483d-ad43-d46a85a6ead5',
             'right_300': '9c3b3205-4fe3-4bf1-af3f-8cf9ab95d918',
             'left_10': '82e95a7a-f335-4178-a7b6-4f38954e497a'
            }

def transformation(robot,plate,breadcrumb=None,strain='E.coli Top10',transformant_volume=15,media='lb',transformation_volume=2):
    # Create new plate
    new_plate = {"plate_form": "96pcr",
                 "plate_name": "{}-transformation".format(plate['plate_name']),
                 "plate_type": "transformation",
                 "status": "planned",
                 "breadcrumb": breadcrumb,
                 "uuid": str(uuid.uuid4())}

    # Metadata
    metadata = {
            "protocolName": "Transformation of {}".format(plate['uuid']),
            "author": "Keoni Gandall",
            "datetime": "{}".format(str(datetime.datetime.now()))
          }

    # Addresses from
    addresses = []
    for well in plate['wells']:
        addresses.append(well['address'])

    # Tipbox
    tipbox = plates.Plate()
    new = plates.Plate()

    # Labware
    pipette = robot['left_10']
    tips = '11_tip_box'

    labware = {
        tips: opentrons_json.labware('11',"opentrons-tiprack-10ul",name="11_tip_box"),
        'trash_yo': opentrons_json.labware('12',"fixed-trash",name="Trash yo"),
        new_plate['uuid']: opentrons_json.labware('5', '96-PCR-flat', name=new_plate['plate_name']),
        plate['uuid']: opentrons_json.labware('4', '96-PCR-flat', name=plate['plate_name'])
    }
    
    # Create new procedure
    procedure = []
    data_transfer = []
    high_level_transfers = Transfer.efficient_transfer(addresses)
    volume = transformation_volume
    for transfer in high_level_transfers:
        procedure.append(commands.pick_up_tip(pipette,tips,tipbox.use_number(transfer[0])[-1]))
        transfer_from = transfer[1][0]
        procedure.append(commands.aspirate(pipette,volume,plate['uuid'],transfer_from))
        transfer_to = new.use_number(transfer[0],columns=new.columns())[0]
        procedure.append(commands.dispense(pipette,volume,new_plate['uuid'],transfer_to))
        procedure.append(commands.drop_tip(pipette,'trash_yo','A1'))
        data_transfer.append((transfer[0],transfer_from,transfer_to))
    
    protocol = {'uuid': str(uuid.uuid4()),
               'description': metadata['protocolName'],
               'protocol': opentrons_json.Protocol(robot,labware,[{'subprocedure': procedure}],metadata=metadata).toJSON(),
               'status': 'planned'}
    
    transfers = Transfer.data_transfer_comprehension(data_transfer)
    new_wells=[]
    for transfer in transfers:
        old_well = {}
        for well in plate['wells']:
            if well['address'] == transfer[0]:
                old_well = well
        new_well = {'address': transfer[1],
                    'media': media,
                    'organism': strain,
                    'plate_uuid': new_plate['uuid'],
                    'quantity': None,
                    'samples': [sample['uuid'] for sample in old_well['samples']],
                    'volume': transformant_volume+transformation_volume,
                   'well_type': 'transformation'}
        new_wells.append(new_well)
    
    output = {'Plate': [new_plate],
             'Well': new_wells,
             'Protocol': [protocol]}
    return output
    
    
result = transformation(opentrons,test_plate)#['protocol']
print(result)
