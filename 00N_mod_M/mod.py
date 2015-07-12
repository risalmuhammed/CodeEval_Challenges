import sys

file = open(sys.argv[1],'r')

def findMod(x,y):
	
	while(x > 0):
		x -= y
	if(x==0):
		return 0
	else:
		return x+y

for line in file:
	line = line.rstrip('\n')

	'''
	N mod M
	'''

	n = int(line[:line.find(',')])
	m = int(line[line.find(',')+1:])	

	#print(n,m)

	print(findMod(n,m))
