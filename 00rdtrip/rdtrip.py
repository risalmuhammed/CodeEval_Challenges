import sys

for line in open(sys.argv[1],'r'):
	l = sorted(list(map(lambda x:int(x),[item for item in line.rstrip('\n').replace(',',' ').replace(';','').split() if item.isalpha()==False])))
	t = str(l[0])
	c = 0
	for i in range(1,len(l)):
		t += ','+str(l[i]-l[i-1])
	print(t)		