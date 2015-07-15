import sys

for line in open(sys.argv[1],'r'):
	t = ''
	l = list(map(lambda x:int(x),line[:line.rstrip('\n').find('|')].split()))
	r = list(map(lambda x:int(x),line[line.find('|')+1:].split()))
	for item in map(lambda x,y:x*y ,l,r):
		t += str(item)+' ' 
	print(t.rstrip(' '))