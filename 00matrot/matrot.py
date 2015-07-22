import sys
import math

for line in open(sys.argv[1],'r'):
	lst = line.rstrip('\n').split()
	s = int(math.sqrt(len(''.join(lst))))
	l = []
	t = ''
	for i in xrange(s):
		l.append([])
	for i in xrange(s):
		for j in xrange(s):
			l[i].append(lst[i*s+j])
	for i in xrange(s):
		for j in xrange(s-1,-1,-1):
			t += l[j][i]+' '
	sys.stdout.write(t.rstrip(' ')+'\n')
