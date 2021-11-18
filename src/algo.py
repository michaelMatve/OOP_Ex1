from building import Building
from allCalls import AllCalls
from callForElev import CallForElev
from data_structure import DataStructure

class Algo:

    def __init__(self,file_b:str,file_c:str,file_o:str):
        self.build_a= Building()
        self.build_a.load_json(file_b)
        self.call_a=AllCalls()
        self.call_a.loadFromcsv(file_c)
        self.out=file_o
        self.elev_tarck= []
        self.elev_time = []
        for i in range(0,self.build_a.numElev):
            self.elev_tarck.append([DataStructure(floor=0,id=-1,direct=0,go_to_time=0)])
            self.elev_time.append(0.0)

    def CreatFile(self):
        for i in self.call_a:
            best_time, best_list = self.checkcall(0,i)
            best_elev=0
            for x in range(1,self.build_a.numElev):
                temp_time, temp_list = self.checkcall(0, i)
                temp_elev = 0
                if(temp_time<best_time):
                    best_time=temp_time
                    best_list= temp_list.copy()
                    best_elev=temp_elev
            self.elev_time[best_elev]=self.elev_time[best_elev]+best_time
            self.elev_tarck[best_elev]=best_list.copy()
        self.call_a.saveTocsv(self.out)

    def checkcall(self,elev_i:int,call:CallForElev):
        temp_list = self.elev_tarck[elev_i].copy()
        temp_list = self.addcall(temp_list,call)
        change_time = self.calwaittime(temp_list)-self.elev_time[elev_i]
        return (change_time,temp_list)

    def addcall(self,calls_list:list, call:CallForElev):



    def calcwaittime(self,t_list:list):
        total_wait=0.0
        for v in t_list:
            if v.id==1:
                total_wait+=v.go_to_time-v.call.time
        return total_wait


    def calclate(self,t_list:list,index_elev:int,index_change:int,type:int):
        if type==-1:
            for v in range(index_change+1,len(t_list)):
                t_list[v].go_to_time+=self.build_a.elevators[index_elev].timefloor()
        else:
            time_change= (abs(t_list[index_change].floor-t_list[index_change+1].floor))/self.build_a.elevators[index_elev].spead
            time_change+=self.build_a.elevators[index_elev].timefloor()
            for x in range(index_change+1,len(t_list)):
                t_list[x].go_to_time +=time_change



