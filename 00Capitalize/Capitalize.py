import sys

for line in open(sys.argv[1],'r'):
	t = '' 
	l = line.rstrip('\n').split()
	for item in l:
		if(ord(item[0]) in range(97,123)):
			t += chr(ord(item[0])-32)
		else:
			t += item[0]
		t+= item[1:]+' '
	print(t.rstrip(' '))
		 