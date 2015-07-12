import sys

file = open(sys.argv[1],'r')
for line in file:
	t = '' 
	for i in range(len(line.rstrip('\n'))):
		if(ord(line[i])>=65 and ord(line[i])<=90):
			t = t + str(chr(ord(line[i])+32))
		else:
			t = t + line[i] 	
	print(t)
