import sys
for line in open(sys.argv[1],'r'):
	l = line.rstrip('\n').split()
	t = list(map(lambda x,y: x.swapcase() if y == '1' else x ,l[0],l[1]))
	print(''.join(t))