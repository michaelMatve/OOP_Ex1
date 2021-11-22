import csv
from callForElev import CallForElev
class AllCalls:
    def __init__(self):
        self.calls = []
        self.num_call=0

    def loadFromcsv(self,file_name):
        try:
            with open(file_name) as file_csv:
                csvreader=csv.reader(file_csv)
                for v in csvreader:
                    temp_call=CallForElev(time=v[1],src=v[2],dest=v[3],status=v[4],elev=v[5])
                    self.addCall(temp_call)
        except IOError as e:
            print("csv fail")

    def saveTocsv(self,file_name):
        temp_arr= []
        for x in self.calls:
            temp_arr.append(x.__dict__.values())
        try:
            with open(file_name, 'w', newline="") as newCsv:
                newWrite=csv.writer(newCsv)
                newWrite.writerows(temp_arr)
        except IOError as e:
            print ("dont creat")

    def addCall(self,tcall:CallForElev):
        self.calls.append(tcall)
        self.num_call+=1

    def __str__(self):
        return f"numofcall: {self.num_call}, calls: {self.calls}"

