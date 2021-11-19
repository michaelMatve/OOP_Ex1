

class CallForElev:
    def __init__(self,time:float,src:int,dest:int,status:int,elev:int):
        self.name = "Elevator call"
        self.time=float(time)
        self.src=int(src)
        self.dest=int(dest)
        self.status=int(status)
        self.elev=int(elev)

    def __str__(self):
        return f"name: {self.name}, time: {self.time}, src: {self.src}, dest: {self.dest}, status: {self.status}, elev: {self.elev} \n"

    def __repr__(self):
        return f"name: {self.name}, time: {self.time}, src: {self.src}, dest: {self.dest}, status: {self.status}, elev: {self.elev} \n"

