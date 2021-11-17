from building import Building
from allCalls import AllCalls


if __name__ == '__main__':
    checkb=Building()
    print(checkb)
    checkb.load_json("C:\\Users\\Dell\\PycharmProjects\\OOP_Ex1\\data\\Ex1_input\\Ex1_Buildings\\B2.json")
    print(checkb)
    checkcall=AllCalls()
    print(checkcall)
    checkcall.loadFromcsv("C:\\Users\\Dell\\PycharmProjects\\OOP_Ex1\\data\\Ex1_input\\Ex1_Calls\\Calls_a.csv")
    print(checkcall)
    checkcall.saveTocsv("outnew.csv")
