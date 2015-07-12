import sys


file = open(sys.argv[1],'r')
for line in file:
	line = line.rstrip('\n')
	temp = int(line)
	if(temp%2==0):
		print('1')
	else:
		print('0')
