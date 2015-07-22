import sys

for line in open(sys.argv[1],'r'):
	l = line.rstrip('\n').split()
	m = [len(item) for item in l]
	print(l[m.index(max(m))])