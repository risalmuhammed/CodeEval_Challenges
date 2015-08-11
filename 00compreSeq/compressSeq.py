import sys
for line in open(sys.argv[1],'r'):
	t = ''
	count = 1
	l = line.rstrip('\n').split()
	for i in range(len(l)-1):
		if(l[i] == l[i+1]):
			count += 1
		else:
			t += str(count)+' '+l[i]+' '
			count = 1
		k = l[i+1]
	if(len(l)!=1):
		t += str(count)+' '+ k
	else:
		t += str(count)+' '+ l[0]
	print(t)