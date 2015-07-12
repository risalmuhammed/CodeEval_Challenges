import sys

list = []

file = open(sys.argv[1],'r')
count = int(file.readline())

for line in file:
	list.append(line.rstrip('\n'))

l = 0
for i in range(len(list)):
	for j in range(len(list)-i):
		if(len(list[j])>=l):
			pos = j
			l = len(list[j])	

	if(count):
		print(list[pos])
		list[pos] = ''
		l=0
		count = count - 1
	else:
		break
