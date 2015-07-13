import sys
import string

file = open(sys.argv[1],'r')
t = string.ascii_lowercase

for line in file:
	f = ''
	line = line.lower().replace(' ','').rstrip('\n')
	#temp = map(lambda x:line.find(x),t) 
	ind = [i for i, x in enumerate(map(lambda x:line.find(x),t)) if x == -1]
	if(len(ind)==0):
		f = 'NULL'
	else:
		for item in ind : f+=t[item] 
	print(f)