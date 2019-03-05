
# Labware
def labware(slot:str,labware_type:str,name=None) -> dict:
    return {
      "slot": slot,
      "model": labware_type,
      "name": name
    }

# Instruments
def pipette(mount:str,name:str,model:str) -> dict:
    if mount not in ["right", "left"]:
        return ValueError("Mount not left or right")
    pipette_names = [
        "p10_single",
        "p10_multi",
        "p50_single",
        "p50_multi",
        "p300_single",
        "p300_multi",
        "p1000_single",
        "p1000_multi"
      ]
    if name not in pipette_names:
        return ValueError("Name not included in pipette_names")
    
    pipette_models = [
        "p10_single_v1",
        "p10_multi_v1",
        "p50_single_v1",
        "p50_multi_v1",
        "p300_single_v1",
        "p300_multi_v1",
        "p1000_single_v1",
        "p1000_multi_v1",

        "p10_single_v1.3",
        "p10_multi_v1.3",
        "p50_single_v1.3",
        "p50_multi_v1.3",
        "p300_single_v1.3",
        "p300_multi_v1.3",
        "p1000_single_v1.3",
        "p1000_multi_v1.3"]
    if model not in pipette_models:
        return ValueError("Name not included in pipette_models")

    return {
      "type": "pipette",
      "mount": mount,
      "name": name,
      "model": model
    }

# Robot
ot2_standard = {"model": "OT-2 Standard"}

# Application
designer_application = {"application-name": "opentrons_json",
    "application-version": "1.0.0",
    "data": {}
  }

# Default values
default_values = {
        "aspirate-flow-rate": {
            "p10_single": 5,
            "p10_multi": 5,
            "p50_single": 25,
            "p50_multi": 25,
            "p300_single": 150,
            "p300_multi": 150,
            "p1000_single": 500
        },
        "dispense-flow-rate": {
            "p10_single": 10,
            "p10_multi": 10,
            "p50_single": 50,
            "p50_multi": 50,
            "p300_single": 300,
            "p300_multi": 300,
            "p1000_single": 1000
        },
        "aspirate-mm-from-bottom": 1,
        "dispense-mm-from-bottom": 0.5,
        "touch-tip-mm-from-top": -1
    }
