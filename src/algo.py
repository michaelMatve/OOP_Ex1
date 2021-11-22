from building import Building
from allCalls import AllCalls
from callForElev import CallForElev
from elevator import Elevator


class Algo:

    def __init__(self,file_b:str,file_c:str,file_o:str):
        self.build_a= Building()
        self.build_a.load_json(file_b)
        self.call_a=AllCalls()
        self.call_a.loadFromcsv(file_c)
        self.out=file_o
        self.elev_order = []
        self.elev_times = []
        if self.build_a.numElev==1:
            self.ratio=0
        else:
            self.ratio = int(self.call_a.num_call/(self.build_a.numElev*self.build_a.numElev*(self.build_a.numElev-1)))
        for i in range(0, self.build_a.numElev):
            self.elev_order.append([])
            self.elev_times.append(0)

    def CreatFile(self):
        for i in range(0, self.call_a.num_call):
            elev_number = 0
            best_time_finish = self.calcfinishtime(elev_number)
            for t in range(1, len(self.elev_times)):
                temp_time_finish = self.calcfinishtime(t)
                if best_time_finish > temp_time_finish:
                    best_time_finish = temp_time_finish
                    elev_number = t
            if self.call_a.calls[i].elev == -1:
                self.call_a.calls[i].elev = elev_number
                not_add_yet = True
                time_finish = self.calcfinishtime(elev_number)
                if time_finish < self.call_a.calls[i].time:
                    self.elev_times[elev_number] = self.call_a.calls[i].time
                else:
                    self.elev_times[elev_number] = time_finish
                if len(self.elev_order[elev_number]) != 0:
                    dir = -1
                    if self.elev_order[elev_number][0]<self.elev_order[elev_number][-1]:
                        dir = 1
                    if (dir == 1)and(self.elev_order[elev_number][0]<self.call_a.calls[i].src < self.elev_order[elev_number][-1]):
                        arr_temp = [self.elev_order[elev_number][-1], self.call_a.calls[i].dest]
                        self.elev_order[elev_number]=arr_temp.copy()
                        not_add_yet = False
                    if(dir == -1) and (self.elev_order[elev_number][0] > self.call_a.calls[i].src > self.elev_order[elev_number][-1]):
                        arr_temp = [self.elev_order[elev_number][-1], self.call_a.calls[i].dest]
                        self.elev_order[elev_number] = arr_temp.copy()
                        not_add_yet = False
                if not_add_yet:
                    self.elev_order[elev_number]=[]
                    self.elev_order[elev_number].append(self.call_a.calls[i].src)
                    self.elev_order[elev_number].append(self.call_a.calls[i].dest)

                flage=True
                counter = 0
                while flage:
                    flage = False
                    for m in range(i+1,self.call_a.num_call):
                        if counter < self.ratio:
                            dir = -1
                            if self.elev_order[elev_number][-1] > self.elev_order[elev_number][0]:
                                dir = 1
                            if (self.call_a.calls[m].elev==-1)and(dir==self.call_a.calls[m].state_of_call()):
                                if (dir == 1) and (self.elev_order[elev_number][0] < self.call_a.calls[m].src < self.elev_order[elev_number][-1]):
                                    time = self.calctime(dir, elev_number, self.call_a.calls[m])
                                    if time > self.call_a.calls[m].time:
                                        self.addcall(dir, elev_number, self.call_a.calls[m])
                                        self.call_a.calls[m].elev=elev_number
                                        flage = True
                                        counter+=1
                                if (dir == -1) and (self.elev_order[elev_number][0] > self.call_a.calls[m].src > self.elev_order[elev_number][-1]):
                                    time = self.calctime(dir, elev_number, self.call_a.calls[m])
                                    if time>self.call_a.calls[m].time:
                                        self.addcall(dir, elev_number, self.call_a.calls[m])
                                        self.call_a.calls[m].elev=elev_number
                                        flage = True
                                        counter += 1
        self.call_a.saveTocsv(self.out)

    def calctime(self,dir:int,elev_index:int,call:CallForElev):
        i=1
        time= (abs(call.src-self.elev_order[elev_index][0]))/self.build_a.elevators[elev_index].speed
        if dir == 1:
            while self.elev_order[elev_index][i] < call.src:
                time+=self.build_a.elevators[elev_index].timefloor()
                i += 1
        else:
            while self.elev_order[elev_index][i] > call.src:
                time += self.build_a.elevators[elev_index].timefloor()
                i += 1
        time += self.elev_times[elev_index]
        return time
    def addcall(self,dir:int,elev_index:int,call:CallForElev):
        i = 1
        if dir == 1:
            while self.elev_order[elev_index][i] < call.src:
                i+=1
            self.elev_order[elev_index].insert(i,call.src)
            while (i < len( self.elev_order[elev_index]))and(self.elev_order[elev_index][i] < call.dest):
                i+=1
            self.elev_order[elev_index].insert(i, call.dest)
        else:
            while self.elev_order[elev_index][i] > call.src:
                i+=1
            while (i < len( self.elev_order[elev_index]))and(self.elev_order[elev_index][i] > call.dest):
                i+=1
            self.elev_order[elev_index].insert(i, call.dest)
    def calcfinishtime(self,elev_index:int):
        if len(self.elev_order[elev_index])== 0:
            return 0
        time = (abs(self.elev_order[elev_index][0]-self.elev_order[elev_index][-1]))/self.build_a.elevators[elev_index].speed
        time = time + ((len(self.elev_order[elev_index])-1)*self.build_a.elevators[elev_index].timefloor())
        time=time+self.elev_times[elev_index]
        return time
