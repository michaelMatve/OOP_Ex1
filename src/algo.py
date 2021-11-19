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
            self.elev_tarck.append([DataStructure(floor=0,id=-1,direct=0,go_to_time=0,call=None)])
            self.elev_time.append(0.0)

    def CreatFile(self):
        for i in range (0,self.call_a.num_call):
            best_time, best_list = self.checkcall(0,self.call_a.calls[i])
            best_elev=0
            for x in range(1,self.build_a.numElev):
                temp_time, temp_list = self.checkcall(x, self.call_a.calls[i])
                temp_elev = x
                if(temp_time<best_time):
                    best_time=temp_time
                    best_list= temp_list.copy()
                    best_elev=temp_elev
            self.elev_time[best_elev]=self.elev_time[best_elev]+best_time
            self.elev_tarck[best_elev]=best_list.copy()
            self.call_a.calls[i].elev=best_elev
            for i in range(0, self.build_a.numElev):
                for x in range(1, len(self.elev_tarck[i])):
                    print("time: ", self.elev_tarck[i][x].call.time, " go_to:",
                          self.elev_tarck[i][x].go_to_time, "id:", self.elev_tarck[i][x].id, "src",
                          self.elev_tarck[i][x].call.src, "dest", self.elev_tarck[i][x].call.dest, "elev", self.elev_tarck[i][x].call.elev)
                print("*************************************************")
        self.call_a.saveTocsv(self.out)

    def checkcall(self,elev_i:int,call:CallForElev):
        temp_list = self.elev_tarck[elev_i].copy()
        temp_list1 = self.addcall(calls_list=temp_list,elev_number=elev_i,call=call)
        change_time = self.calcwaittime(temp_list1)-self.elev_time[elev_i]
        return (change_time,temp_list1)

    def addcall(self,calls_list:list, elev_number:int, call:CallForElev):
        i = 0
        flag1=False
        flag2=False
        while i < len(calls_list):
            if calls_list[i].go_to_time > call.time:
                break
            i += 1
        while i < len(calls_list):
            if calls_list[i-1].direct == 0:
                i += 1
            else:
                if calls_list[i-1].direct == 1:
                    if call.src <= calls_list[i-1].floor: # note
                        i += 1
                    else:
                        if call.src > calls_list[i].floor:
                            if calls_list[i].direct == -1:
                                calc_go = abs(calls_list[i].floor - call.src) / self.build_a.elevators[elev_number].speed
                                calc_go += self.build_a.elevators[elev_number].timefloor()
                                calc_go += calls_list[i].go_to_time
                                temp_src1 = DataStructure(floor=call.src, id=0, direct=-1, go_to_time=calc_go,call=call)
                                calls_list[i].direct = 1
                                calls_list.insert(i + 1, temp_src1)
                                calls_list=self.calclate(t_list=calls_list, index_elev=elev_number, index_change=i+1, type=1)
                                flag1 = True
                                break
                            i += 1
                        else:
                            if call.src == calls_list[i].floor:
                                flag1 = True
                                break
                            temp_go_to=abs(calls_list[i-1].floor - call.src) / self.build_a.elevators[elev_number].speed
                            temp_go_to+= calls_list[i - 1].go_to_time
                            temp_go_to+=self.build_a.elevators[elev_number].timefloor()
                            if temp_go_to > call.time:
                                temp_src1 = DataStructure(floor=call.src, id=0, direct=1, go_to_time=temp_go_to,call=call)
                                calls_list.insert(i, temp_src1)
                                calls_list = self.calclate(t_list=calls_list, index_elev=elev_number,index_change=i, type=-1)
                                flag1 = True
                                break
                            i += 1
                else:
                    if call.src >= calls_list[i-1].floor: # note
                        i += 1
                    else:
                        if call.src < calls_list[i].floor:
                            if calls_list[i].direct == 1:
                                calc_go = abs(calls_list[i].floor - call.src) / self.build_a.elevators[elev_number].speed
                                calc_go += self.build_a.elevators[elev_number].timefloor()
                                calc_go += calls_list[i].go_to_time
                                temp_src1 = DataStructure(floor=call.src, id=0, direct=1, go_to_time=calc_go,call=call)
                                calls_list[i].direct = -1
                                calls_list.insert(i + 1, temp_src1)
                                calls_list = self.calclate(t_list=calls_list, index_elev=elev_number,index_change=i + 1, type=1)
                                flag1 = True
                                break
                            i += 1
                        else:
                            if call.src == calls_list[i].floor:
                                flag1 = True
                                break
                            temp_go_to = calls_list[i - 1].go_to_time
                            temp_go_to += abs(calls_list[i - 1].floor - call.src) / self.build_a.elevators[elev_number].speed
                            temp_go_to += self.build_a.elevators[elev_number].timefloor()
                            if temp_go_to > call.time:
                                temp_src1 = DataStructure(floor=call.src, id=0, direct=-1, go_to_time=temp_go_to,call=call)
                                calls_list.insert(i, temp_src1)
                                flag1 = True
                                calls_list = self.calclate(t_list=calls_list, index_elev=elev_number, index_change=i,type=-1)
                                break
                            i += 1

        while i < len(calls_list):
            if calls_list[i - 1].direct == 0:
                i += 1
            else:
                if calls_list[i - 1].direct == 1:
                    if call.dest <= calls_list[i - 1].floor:  # note
                        i += 1
                    else:
                        if call.dest > calls_list[i].floor:
                            if calls_list[i].direct == -1:
                                calc_go=abs(calls_list[i].floor-call.dest)/self.build_a.elevators[elev_number].speed
                                calc_go+=self.build_a.elevators[elev_number].timefloor()
                                calc_go+=calls_list[i].go_to_time
                                temp_dest1=DataStructure(floor=call.dest, id=1, direct=-1,go_to_time=calc_go,call=call)
                                calls_list[i].direct=1
                                i=i+1
                                calls_list.insert(i,temp_dest1)
                                calls_list = self.calclate(t_list=calls_list, index_elev=elev_number,index_change=i, type=1)
                                flag2 = True
                                break
                            i += 1
                        else:
                            if call.dest == calls_list[i].floor:
                                temp_dest1=DataStructure(floor=calls_list[i].floor,id=1,direct=0,go_to_time=calls_list[i].go_to_time,call=call)
                                calls_list.insert(i,temp_dest1)
                                flag2 = True
                                break
                            flag2 = True
                            calc_go = self.build_a.elevators[elev_number].timefloor()
                            calc_go += calls_list[i].go_to_time
                            temp_dest1 = DataStructure(floor=call.dest, id=1, direct=1, go_to_time=calc_go, call=call)
                            calls_list.insert(i, temp_dest1)
                            calls_list = self.calclate(t_list=calls_list, index_elev=elev_number, index_change=i,type=-1)
                            break
                else:
                    if call.dest >= calls_list[i - 1].floor:  # note
                        i += 1
                    else:
                        if call.dest < calls_list[i].floor:
                            if calls_list[i].direct == 1:
                                calc_go = abs(calls_list[i].floor - call.dest) / self.build_a.elevators[elev_number].speed
                                calc_go += self.build_a.elevators[elev_number].timefloor()
                                calc_go += calls_list[i].go_to_time
                                temp_dest1 = DataStructure(floor=call.dest, id=1, direct=1, go_to_time=calc_go,call=call)
                                calls_list[i].direct = -1
                                calls_list.insert(i + 1, temp_dest1)
                                calls_list = self.calclate(t_list=calls_list, index_elev=elev_number,index_change=i + 1, type=1)
                                flag2 = True
                                break
                            i += 1
                        else:
                            if call.dest == calls_list[i].floor:
                                temp_dest1 = DataStructure(floor=calls_list[i].floor, id=1, direct=0,go_to_time=calls_list[i].go_to_time, call=call)
                                calls_list.insert(i, temp_dest1)
                                flag2 = True
                                break
                            flag2 = True
                            calc_go = self.build_a.elevators[elev_number].timefloor()
                            calc_go += calls_list[i].go_to_time
                            temp_dest1 = DataStructure(floor=call.dest, id=1, direct=-1, go_to_time=calc_go, call=call)
                            calls_list.insert(i, temp_dest1)
                            calls_list = self.calclate(t_list=calls_list, index_elev=elev_number, index_change=i,type=-1)
                            break

        if flag1==False:
                calc_go1 = abs(calls_list[i-1].floor - call.src) / self.build_a.elevators[elev_number].speed
                if calc_go1!=0:
                    calc_go1 += self.build_a.elevators[elev_number].timefloor()
                calc_go1 += max(calls_list[i-1].go_to_time,call.time)
                dir1=-1
                if call.src>calls_list[i-1].floor:
                   dir1=1
                temp_dest1 = DataStructure(floor=call.src, id=0, direct=dir1, go_to_time=calc_go1, call=call)
                calls_list.insert(i,temp_dest1)
                i+=1
        if flag2==False:
            calc_go2 = abs(calls_list[i-1].floor - call.dest) / self.build_a.elevators[elev_number].speed
            calc_go2 += self.build_a.elevators[elev_number].timefloor()
            calc_go2 += calls_list[i-1].go_to_time
            dir2=-1
            if call.dest>calls_list[i-1].floor:
                dir2=1
            temp_dest1 = DataStructure(floor=call.dest, id=1, direct=dir2, go_to_time=calc_go2, call=call)
            calls_list.insert(i,temp_dest1)
            i+=1
        return calls_list





    def calcwaittime(self,t_list:list):
        total_wait=0.0
        for v in t_list:
            if v.id==1:
                total_wait+=(v.go_to_time-v.call.time)
        return total_wait


    def calclate(self,t_list:list,index_elev:int,index_change:int,type:int):
        if type==-1:
            for v in range(index_change+1,len(t_list)):
                t_list[v].go_to_time+=self.build_a.elevators[index_elev].timefloor()
        else:
            if index_change!=(len(t_list)-1):
                time_change= (abs(t_list[index_change].floor-t_list[index_change+1].floor))/self.build_a.elevators[index_elev].speed
                time_change+=self.build_a.elevators[index_elev].timefloor()
                for x in range(index_change+1,len(t_list)):
                    t_list[x].go_to_time +=time_change
        return t_list



