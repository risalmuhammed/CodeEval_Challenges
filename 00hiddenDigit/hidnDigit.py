import sys

dic = {
	'a': 0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9
}

for line in open(sys.argv[1],'r'):
	t = ''
	for letter in line.rstrip('\n'):
		if(letter in dic):
			t += str(dic[letter])
		elif(letter.isdigit() == True):
			t +=letter
	if(len(t)!=0):
		print(t)
	else:
		print('NONE')