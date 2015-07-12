import sys

file =  open(sys.argv[1],'r')
for line in file:
	scrub = line[line.find(',')+1:].strip()
	str = line[:line.find(',')]
	for i in range(len(scrub)):
		str = str.replace(scrub[i],'').strip()
	print(str)

