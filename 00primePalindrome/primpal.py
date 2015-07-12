
def prime(var):
	flag = 0
	for i in range(2,int(var/2)):
		if(var%i==0):
			flag = 1
			break
	if(flag == 0):
		return 1
	else:
		return 0

def pal(var):
	varT = str(var)
	if(str(var) == varT[::-1]):
		return 1
	else:
		return 0

large = 0
for i in range(1000):
	if(prime(i)& pal(i)):
		large = i
print(large)
