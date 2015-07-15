import sys
import itertools as it


for line in open(sys.argv[1],'r'):
	t = []
	k = ''
	l = list(it.permutations([item for item in line.rstrip('\n')]))
	for i in range(len(l)):
		for j in range(len(l[i])):
			k += l[i][j]
		t.append(k)
		k = ''
	t.sort()
	
	for item in t:
		k += item+','
	print(k.rstrip(',')) 