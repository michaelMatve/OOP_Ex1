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

    def CreatFile(self):
        for i in range(0,self.call_a.num_call):
            self.call_a.calls[i].elev=1
        self.call_a.saveTocsv(self.out)




