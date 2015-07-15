import sys

for line in open(sys.argv[1],'r'):
	l = list(map(lambda x :int(x) , line.rstrip('\n').replace(',',' ').split()))
	lo = len('{0:b}'.format(l[0]))
	if('{0:b}'.format(l[0])[lo-l[1]] == '{0:b}'.format(l[0])[lo-l[2]]):
		sys.stdout.write('true\n')
	else:
		sys.stdout.write('false\n')
