import sys


file = open(sys.argv[1],'r')
for line in file:
	sum = 0
	temp = int(line.rstrip('\n'))
	while(temp):
		sum = sum + (temp%10)	
		temp = int(temp/10)
	print(sum)
