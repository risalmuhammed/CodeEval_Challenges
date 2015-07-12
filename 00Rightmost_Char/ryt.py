import sys

file = open(sys.argv[1],'r')

for line in file:
	line = line.rstrip('\n')
	source = line[:line.find(',')] 
	st = line[line.find(',')+1:]

	pos = (len(source)-source[::-1].find(st)-1 if source[::-1].find(st)!=-1 else (-1))

	print(pos)
