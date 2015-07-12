import sys

file = open(sys.argv[1],'r')
for line in file:
	l = len(line.rstrip('\n'))
	countSmall = 0
	countLarge = 0
	for i in range(l):
		if(ord(line[i])>=97 and ord(line[i])<=122):
			countSmall = countSmall + 1
		if(ord(line[i])>=65 and ord(line[i])<=90):
			countLarge = countLarge + 1
	sPer = float(countSmall*100)/l
	cPer = float(countLarge*100)/l	
	#print(l,countSmall,countLarge)
	print('lowercase: '+str('%.2f'%sPer)+' uppercase: '+str('%.2f'%cPer))

