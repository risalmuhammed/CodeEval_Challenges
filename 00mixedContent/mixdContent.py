import sys

for line in open(sys.argv[1],'r'):
	t = ''
	line = line.rstrip('\n').replace(',',' ').split()
	nums = [item for item in line if item.isalpha() == False]
	words = [item for item in line if item.isalpha() == True]

	for item in words: t += item + ','
	if(len(t)!=0 and len(nums)!=0): t = t.rstrip(',')+'|'	
	for item in nums: t += item + ','
	print(t.rstrip(','))