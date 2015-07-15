import sys

for line in open(sys.argv[1],'r'):
	l = line.rstrip('\n').split()
	print(l[len(l)-2])