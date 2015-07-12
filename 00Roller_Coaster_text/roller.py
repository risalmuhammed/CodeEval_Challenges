import sys

file = open(sys.argv[1],'r')

for line in file:
	t = ''
	k = 1
	line = line.rstrip('\n')
	for i in range(len(line)):
		if(line[i].isalpha()):
		#	print(line[i])
			if(k == 1):
				t = t + line[i].upper()
				k = 0
			else:
				t = t + line[i].lower()
				k = 1
		else:
			t = t + line[i]
	sys.stdout.write(t +'\n')		
