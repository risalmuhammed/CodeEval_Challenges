'''
If you have the equation of the circle,
simply plug in the x and y from your point (x,y).
After working out the problem, check to see whether
your added values are greater than, less than, or equal
to the r^2 value. If it is greater, then the point
lies outside of the circle.

(x-h)^2+(y-k)^2 = r^2

'''

import sys
import math


for line in open(sys.argv[1],'r'):
	l = []
	line = line.rstrip('\n')+';'
	for i in range(3):
		l.append(line[line.find(':')+1:line.find(';')])
		line = line[line.find(';')+1:]
	for item in l:
		if(l.index(item)==0):
			c = list(map(lambda x:float(x),item[item.find('(')+1:item.find(')')].replace(',','').split()))
		elif(l.index(item)==1):
			r = float(item.strip())
		else:
			p = list(map(lambda x:float(x),item[item.find('(')+1:item.find(')')].replace(',','').split()))

	check = math.pow(p[0]-c[0],2) + math.pow(p[1]-c[1],2)
	if(check<=pow(r,2)):
		print('true')
	else:
		print('false')