import sys

for line in open(sys.argv[1],'r'):
	if(len(line.rstrip('\n'))!=0):
		sum = 0
		indx = [i for i,x in enumerate(line.rstrip('\n')) if x=='i']
		for i in indx:
			if(line[i:i+17].find('label')!=-1):
				t = ''.join([item for item in line[i:i+17] if item.isdigit()==True])
				sum += int(t)
		print(sum)