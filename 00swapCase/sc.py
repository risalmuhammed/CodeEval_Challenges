import sys

file = open(sys.argv[1],'r')

for line in file:
	line = line.rstrip('\n')
	t =''
	for i in range(len(line)):
		if(ord(line[i])>=97 and ord(line[i])<=122 ):
			t+= str(chr(ord(line[i])-32))

		elif(ord(line[i])>=65 and ord(line[i])<=90 ):
			t+=str(chr(ord(line[i])+32))
		else:
			t += line[i]

	print(t)
