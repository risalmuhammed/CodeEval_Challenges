import sys

for line in open(sys.argv[1],'r'):
	t = ''
	w = line.rstrip('\n').split()
	l = list(map(lambda x: len(x), w))
	ind = l.index(max(item for item in l))
	for i in range(len(w[ind])):
		t += '*'*i + w[ind][i]+' '
	print(t.rstrip(' ')) 	
