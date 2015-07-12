import sys

file = open(sys.argv[1],'r')
for line in file:
	l = []
	line = line.rstrip('\n')
	l = [item for item in line]
	
	for i in range(len(l)):
		if l.count(l[i])==1 : print(l[i]) ;break
	
	
		
