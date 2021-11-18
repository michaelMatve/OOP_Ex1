from building import Building
from allCalls import AllCalls
from callForElev import CallForElev

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
            self.elev_tarck.append([])
            self.elev_time.append(0)

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


