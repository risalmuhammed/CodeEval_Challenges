import sys
import math

for line in open(sys.argv[1],'r'):

	p1 = list(map(lambda x:int(x), line.rstrip('\n')[line.find('(')+1:line.find(')')].replace(',','').split()))
	line = line[line.find(')')+1:]
	p2 = list(map(lambda x:int(x), line.rstrip('\n')[line.find('(')+1:line.find(')')].replace(',','').split()))
	#print(p1,p2)
	
	print(int(math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))))