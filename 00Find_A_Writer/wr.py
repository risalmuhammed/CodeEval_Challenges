import sys

file = open(sys.argv[1],'r')


for line in file:
	line = line.rstrip('\n')
	left = line[:line.find('|')]
	right = line[line.find('|')+2:]+' '	
	t = ''
	#print(left,right)
	
	while(right):
		pos = int(right[:right.find(' ')])
		t += left[pos-1]
		
		right = right[right.find(' ')+1:]
	print(t)	
