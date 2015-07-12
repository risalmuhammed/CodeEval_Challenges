import sys

file = open(sys.argv[1],'r')
list = []

def calc(op):
	if(op == '+'):
		list.append(list.pop() + list.pop())
	elif(op == '*'):
		list.append(list.pop() * list.pop())
	elif(op == '/'):
		list.append(list.pop() / list.pop()) 
	
for line in file:
	input_string = line.rstrip('\n')#.strip(' ')
	for i in range(len(input_string)):
		val = input_string[len(input_string)-1]
		input_string = input_string[:len(input_string)-1]
		if(val.isdigit()):
			list.append(float(val))				
		else:
			calc(val) #operator
	
	sys.stdout.write(str(int(list.pop()))+'\n')	
