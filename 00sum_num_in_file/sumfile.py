import sys
sum = 0
file = open(sys.argv[1],'r')
for line in file:
	line = line.rstrip('\n')
	temp = int(line)
	sum = sum + temp
print(sum)
