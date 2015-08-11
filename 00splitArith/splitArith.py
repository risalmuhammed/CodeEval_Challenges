import sys

for line in open(sys.argv[1],'r'):
	l = line.rstrip('\n').split()
	num,pat = l[0],l[1]

	if(pat.find('+')!=-1):idx = pat.index('+');op = 'add'
	if(pat.find('-')!=-1):idx = pat.index('-');op = 'sub'
	if(op == 'add'):print(int(num[:idx])+int(num[idx:]))
	else:print(int(num[:idx])-int(num[idx:]))