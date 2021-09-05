
a = range(100)
b =[2,3,7,11]
re=[]
inc=[]
xx = filter(lambda x: x%2 !=0,a)
for i in range(len(b)):
	t1=b[i]
	a1 =  filter(lambda x: x%t1 ==0,a)

	re.append(a1)

re2=[]
cc=[]

for i in range(1,len(re)):
	t =re[i]
	for j in range(i):
		t = filter(lambda x :x not in re[j],t)
	re2.append(t)
re3=[]
for i in range(1,len(re2)):
	t =filter(lambda x: x not in re2[i-1],re2[i])
	re3.append(t)

for i in range(len(re)):
	print re[i]

for i in range(len(re2)):
	print re2[i]

