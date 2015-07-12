
def prime(var):
	flag = 0
	if(var == 4):
		return 0
	for i in range(2,int(var/2)):
		if(var%i==0):
			flag = 1
			break
	if(flag == 0):
		return 1
	else:
		return 0
i = 2 
sum = 0
count = 1000
while(i>0 and count>0):
	if(prime(i)):
		sum = sum + i
		count = count - 1
	i = i + 1
print(sum)
