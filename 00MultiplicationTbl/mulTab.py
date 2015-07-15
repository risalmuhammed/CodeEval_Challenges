for i in range(1,13):
	t =''
	for j in range(1,13):
		width = len(str(i*j))
		t +=  ' '*(4-width)+str(i*j)
	print(t)
