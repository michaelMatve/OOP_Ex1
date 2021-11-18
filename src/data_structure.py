from callForElev import CallForElev
class DataStructure:
    def __init__(self, floor:int, id:int, direct:int, go_to_time:int, call:CallForElev):
        self.floor = floor
        self.id = id
        self.direct = direct
        self.call = call
        self.go_to_time = go_to_time
