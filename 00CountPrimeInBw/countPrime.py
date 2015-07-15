import sys

for line in open(sys.argv[1],'r'):
	l = list(map(lambda x: int(x),line.rstrip('\n').replace(',',' ').split()))
	p = [item for item in range(l[0],l[1]+1) if item>1 and len([i for i in range(2,int(item/2)+1) if item%i == 0])==0]
	print(len(p))