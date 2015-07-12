
import sys

def prime(var):
	flag = 0
	if(var == 4):
		return 0
	for i in range(2,int(var/2)):
		if(var%i==0):
			flag = 1
			break
	if(flag == 0):
		return 1
	else:
		return 0

file = open(sys.argv[1],'r')
for line in file:
	t = ''
	count = int(line.rstrip('\n'))
	i = 2 
	
	while(i<count):
		if(prime(i)):
			t = t + str(i)+','			
		i = i + 1
	print(t.rstrip(','))
