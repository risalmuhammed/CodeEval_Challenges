
import sys
import math
file = open(sys.argv[1],'r')
for line in file:
    try:
        temp = int(line)
        binNum = int(0)
        i = 0
        while(temp != 0):
           binNum = binNum + math.pow(10,i)*(temp%2)
           temp = int(temp/2)
           i = i + 1
        print(int(binNum))
    except:
        pass
