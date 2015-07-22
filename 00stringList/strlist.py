import sys
import itertools as it
from collections import OrderedDict as od

for line in open(sys.argv[1],'r'):
	k= ''
	l = line.rstrip('\n').replace(',',' ').split()
	t = tuple(od.fromkeys(tuple(it.product(l[1],repeat=int(l[0]))))) #removing Duplicates 'OrderDict'
	for item in sorted(t):
		k += ''.join(elem for elem in item)+','
	print(k.rstrip(','))