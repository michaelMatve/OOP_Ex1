
class Elevator:
    def __init__(self,id:int,speed:float,minFloor:int,maxFloor:int,closeTime:float,openTime:float,startTime:float,stopTime:float ):
        self.id=id
        self.speed=speed
        self.minFloor=minFloor
        self.maxFloor=maxFloor
        self.closeTime=closeTime
        self.openTime=openTime
        self.startTime=startTime
        self.stopTime=stopTime

    def __str__(self):
        return f"id: {self.id}, speed: {self.speed}, minFloor: {self.minFloor}, maxFloor: {self.maxFloor}, closeTime:{self.closeTime}, openTime: {self.openTime}, startTime: {self.startTime}, stopTime: {self.stopTime} \n"

    def __repr__(self):
        return f"id: {self.id}, speed: {self.speed}, minFloor: {self.minFloor}, maxFloor: {self.maxFloor}, closeTime:{self.closeTime}, openTime: {self.openTime}, startTime: {self.startTime}, stopTime: {self.stopTime} \n"

