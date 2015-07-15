import sys

for line in open(sys.argv[1],'r'):
	t = ''
	l = list(set(line[:line.find(';')].replace(',',' ').split()) & set(line[line.find(';')+1:].rstrip('\n').replace(',',' ').split()))
	l.sort()
	if(len(l) != 0):
		for item in l:
			t += item+','
		print(t.rstrip(','))
	else:
		print('')