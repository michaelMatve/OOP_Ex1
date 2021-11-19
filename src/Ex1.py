import sys

from algo import Algo


if __name__ == '__main__':
    if len(sys.argv)==4:
        test= Algo(sys.argv[1],sys.argv[2],sys.argv[3])
        test.CreatFile()

