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

    def load_json(self, file_name):
        try:
            with open(file_name, "r+") as jasonFile:
                temp_dic = json.load(jasonFile)
                self.minFloor=temp_dic["_minFloor"]
                self.maxFloor = temp_dic["_maxFloor"]
                temp_elev=temp_dic["_elevators"]
                for e in temp_elev:
                    elev=Elevator(id=e["_id"],speed=e["_speed"],minFloor=e["_minFloor"],maxFloor=e["_maxFloor"],closeTime=e["_closeTime"],openTime=e["_openTime"],startTime=e["_startTime"],stopTime=e["_stopTime"])
                    self.addElev(elev)
        except IOError as e:
            print("dont work")

    def __str__(self):
        return f"minFloor:{self.minFloor}, maxFloor: {self.maxFloor},number of elevators: {self.numElev}, elevators: \n {self.elevators}"











