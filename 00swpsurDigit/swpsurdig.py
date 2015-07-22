import sys

for line in open(sys.argv[1],'r'):
	t = ''
	l =line.rstrip('\n').split()
	for item in l:
		t += item[len(item)-1]+item[1:len(item)-1]+item[0]+' '
	sys.stdout.write(t.rstrip(' ')+'\n')