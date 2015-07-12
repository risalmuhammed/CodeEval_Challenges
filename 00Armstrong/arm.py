import sys
import math
temp = 0

file = open(sys.argv[1],'r')
for line in file:
	sum = 0
	line = line.rstrip('\n')
	n = len(line)
	temp = int(line)
	while(temp):
		sum = sum + int(math.pow((temp%10),n))
		temp = int(temp/10)
	if(sum == int(line)):
		print('True')
	else:
		print('False')
