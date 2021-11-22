import sys

from algo import Algo
from building import Building
from allCalls import AllCalls
from callForElev import CallForElev
from elevator import Elevator


if __name__ == '__main__':
        if len(sys.argv) == 4:
                test = Algo(sys.argv[1],sys.argv[2],sys.argv[3])
                test.CreatFile()
        else:
                test = Algo("B2.json","Calls_a.csv","test_output.csv")
                test.CreatFile()


