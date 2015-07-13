import sys
step = 0

def cal(x):
	global step
	temp = x+int(str(x)[::-1])
	step += 1 
	if(str(temp) == str(temp)[::-1]):
		print(str(step)+' '+str(temp))
	else:
		cal(temp)
		

for line in open(sys.argv[1],'r'):
	step = 0
	val = int(line.rstrip('\n'))
	cal(val)
