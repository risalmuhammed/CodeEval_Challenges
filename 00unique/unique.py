import sys
from collections import OrderedDict as od

for line in open(sys.argv[1],'r'):
	t = ''
	l = tuple(od.fromkeys(line.rstrip('\n').replace(',',' ').split()))
	#print(l)	
	for item in l:t+=item+','
	print(t.rstrip(','))