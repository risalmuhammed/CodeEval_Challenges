import sys

for line in open(sys.argv[1],'r'):
	print(int(line.rstrip('\n'),16))