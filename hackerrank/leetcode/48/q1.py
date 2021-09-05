def maxNUm(num):
	al =[]
	while num != 0:
		t1= num %10
		al.append(t1)
		num = num /10
	n = len(al)
	isF= False

	for i in range(n):
		t1= al[n-1-i]
		t2=0
		index =0
		for j in range(n-1-i):
			tp = al[j]
			if tp > t2:
				t2 = tp
				index = j
		if t1 < t2:
			al[index] = t1
			al[n-1-i] =t2
			isF = True
			break
	re =0
	for i in range(n):
		re = re * 10+ al[n-1-i]
	print re

maxNUm(9973)