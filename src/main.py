from building import Building



if __name__ == '__main__':
    checkb=Building()
    print(checkb)
    checkb.load_json("C:\\Users\\eylon\\PycharmProjects\\OOP_Ex1\\data\\Ex1_input\\Ex1_Buildings\\B2.json")
    print(checkb)