import sys

file = open(sys.argv[1],'r')
list = []
for line in file:
	count = int(line[:line.find(';')])
	line = line[line.find(';')+1:].rstrip('\n')
	line = line + ','
	for i in range(count):
		list.append(line[:line.find(',')])
		line = line[line.find(',')+1:]
	
	for i in range(count):
		c = 0
		for j in range(count):
			if(int(list[j]) == i):
				c = c + 1
				if(c == 2):
					print(i)
					break
				
	list = []
