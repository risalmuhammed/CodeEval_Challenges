import sys

for line in open(sys.argv[1],'r'):
	f = ''
	for item in line.rstrip('\n').split():
		f = item +' '+ f
	print(f)
		