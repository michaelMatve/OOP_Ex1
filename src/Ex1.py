import sys

from algo import Algo


if __name__ == '__main__':
        test2_algo=Algo("B3.json","Calls_b.csv","zmichaelchecker.csv")
        test2_algo.CreatFile()
        print(test2_algo.elev_times)



        '''
            if len(sys.argv)==4:
        print("1")
        test= Algo(sys.argv[1],sys.argv[2],sys.argv[3])
        test.CreatFile()
    else:
        
        '''

