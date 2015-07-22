import sys

for line in open(sys.argv[1],'r'):
	t = ''
	l = list(map(lambda x: int(x),line.rstrip('\n').split()))
	for i in range(1,l[2]+1):
		if(i%l[0]==0 and i%l[1]==0):t += 'FB'+' '
		elif(i%l[0]==0):t += 'F'+' '
		elif(i%l[1]==0):t += 'B'+' '
		else: t += str(i)+' '
	print(t.rstrip(' '))