import sys

for line in open(sys.argv[1],'r'):
	for item in line.rstrip('\n'):
		if(item.isalpha()==False):
			line = line.replace(item,' ')
	print(' '.join(line.split()).rstrip(' ').lower())