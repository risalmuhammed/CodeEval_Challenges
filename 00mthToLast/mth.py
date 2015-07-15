import sys

file = open(sys.argv[1],'r')
for line in file:
	line = line.rstrip('\n').split()
	t = int(line[len(line)-1])
	del line[len(line)-1]
	if(t>len(line)):
		pass
	else:
		sys.stdout.write(line[len(line)-t] + '\n')


