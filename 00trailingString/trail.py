import sys

file = open(sys.argv[1],'r')

for line in file:
	flag = 0
	temp = line.rstrip('\n')[line.find(',')+1:]
	ser = line.rstrip('\n')[:line.find(',')]
	l_temp = len(temp)	
	l_ser = len(ser)

	for i in range(l_temp):
		if(temp[l_temp-i-1] != ser[l_ser-i-1]):
			flag = 1
	if(flag == 1):
		print('0')
	else:
		print('1')
			
