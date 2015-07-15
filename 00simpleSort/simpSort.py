import sys

for line in open(sys.argv[1],'r'):
	t = ''
	l = list(map(lambda x : float(x), line.rstrip('\n').split()))
	for i in range(len(l)):
		for j in range(len(l)):
			if(l[i]<l[j]):
				l[i],l[j] = l[j],l[i]
		
	for item in l:
		item = '%.3f'%item
		t += str(item)+' '
	print(t.rstrip(' '))
