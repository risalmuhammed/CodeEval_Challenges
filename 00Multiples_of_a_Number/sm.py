import sys

file = open(sys.argv[1],'r')

def sm(x,y):
	count = 1
	t = 0
	while(t<x):
		t = y * count 
		count = count + 1
	return t 

for line in file:
	line = line.rstrip('\n')
	x = int(line[:line.find(',')])
	y = int(line[line.find(',')+1:]) 
	#print(x,y)
	sys.stdout.write(str(sm(x,y)))
	#print(sm(x,y))
