import sys

class stack:
	
	def __init__(self):
		self.list = []
	
	def push_op(self,item):
		self.list.append(item)
	
	def pop_op(self,pos):
		return self.list[pos]

d = stack()

for line in open(sys.argv[1],'r'):
	d.list = []
	t = ''
	for item in line.rstrip('\n').split():
		d.push_op(item)
	d.list.reverse()		
	for i in range(0,len(d.list),2):
		t += ' '+d.pop_op(i)

	sys.stdout.write(t+'\n')
