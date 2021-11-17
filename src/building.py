import json

from elevator import Elevator
class Building:
    def __init__(self,minFloor:int=0,maxFloor:int=0):
        self.elevators={}
        self.minFloor=minFloor
        self.maxFloor=maxFloor
        self.numElev=0

    def addElev(self,elev:Elevator):
        self.elevators[elev.id]=elev
        self.numElev+=1

    def load_json(self,file_name):
        try:
            with open(file_name) as jasonFail:
                self.elevators = {}
                temp_dic=json.load(jasonFail)
                self.minFloor=temp_dic["minFloor"]
                self.maxFloor = temp_dic["maxFloor"]
                temp_elev=temp_dic["elevators"]
                for k,e in temp_elev.item():
                    elev=Elevator(id=e["id"],speed=["speed"],minFloore=["minFloore"],maxFloor=e["maxFloor"],closeTime=e["closeTime"],openTime=e["openTime"],startTime=e["startTime"],stopTime=e["stopTime"])
                    self.addElev(elev)
        except IOError as e:
            print("dont work")







