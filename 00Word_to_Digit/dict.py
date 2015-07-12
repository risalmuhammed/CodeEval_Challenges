import sys

file = open(sys.argv[1],'r')
dic = {
	'zero' : '0',
	'one' : '1',
	'two' : '2',
	'three' : '3',
	'four' : '4',
	'five' : '5',
	'six' : '6',
	'seven' : '7',
	'eight' : '8',
	'nine' : '9'

}

for line in file:
	line = line.rstrip('\n').replace(';',' ') + ' '
	#print(line)
	t = ''
		
	while(line):
		t += dic[line[:line.find(' ')]]
		line = line[line.find(' ')+1:]	
	print(t)
