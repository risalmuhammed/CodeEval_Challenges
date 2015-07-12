import sys

file = open(sys.argv[1],'r')
file.seek(0,2)
s = file.tell()
print(s)
