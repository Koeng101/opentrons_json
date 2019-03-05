import json
# https://github.com/Opentrons/opentrons/blob/edge/shared-data/protocol-json-schema/protocol-schema.json

# Aspirate, dispense, air gap
def aspirate(pipette:str,volume:float,target:str,well:str) -> dict:
    return {"command": "aspirate",
            "params": {
                "pipette": pipette,
                "volume": volume,
                "labware": target,
                "well": well}}

def dispense(pipette:str,volume:float,target:str,well:str) -> dict:
    return {"command": "dispense",
            "params": {
                "pipette": pipette,
                "volume": volume,
                "labware": target,
                "well": well}}

def air_gap(pipette:str,volume:float,target:str,well:str) -> dict:
    return {"command": "air-gap",
            "params": {
            "pipette": pipette,
            "volume": volume,
            "labware": target,
            "well": well}}

# Touch tip
def touch_tip(pipette:str,target:str,well:str) -> dict:
        return  {"command": "touch-tip",
                "params": {
                "pipette": pipette,
                "labware": target,
                "well": well}}

# Pick up tip, drop tip, blowout
def pick_up_tip(pipette:str,target:str,well:str) -> dict:
    return {"command": "pick-up-tip",
            "params": {
            "pipette": pipette,
            "labware": target,
            "well": well}}

def drop_tip(pipette:str,target:str,well:str) -> dict:
    return {"command": "drop-tip",
            "params": {
            "pipette": pipette,
            "labware": target,
            "well": well}}

def blowout(pipette:str,target:str,well:str) -> dict:
    return {"command": "blowout",
            "params": {
            "pipette": pipette,
            "labware": target,
            "well": well}}

# Delay

def delay(sec:float, message:str) -> dict:
    return {"command": "delay",
            "params": {
          "wait": sec,
          "message": message}}

