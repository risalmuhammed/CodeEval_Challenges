import sys

for line in open(sys.argv[1],'r'):
	t =''
	flag = 'False'
	l = line.rstrip('\n').replace(',',' ').split()
	for i in range(len(l[1])):
		t = l[1][len(l[1])-1]+l[1][:len(l[1])-1]
		if(t == l[0]):
			flag = 'True'
			break
		l[1] = t
	print(flag)