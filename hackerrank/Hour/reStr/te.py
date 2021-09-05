import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


print ins



q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	a,b=map(int , ins[index+i*2].strip().split())
	n= map(int , ins[index+i*2+1].strip().split())
	no1=filter(lambda x:x==1,n)
	al=sum(n) +no1 +a
	if al%2==1:
		print "Second"
	else:
		print "First"