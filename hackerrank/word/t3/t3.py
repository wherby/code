filename = "input/input00.txt"
f=open(filename,'r')

import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin

def sumMx(m, n ):
	s=0
	n2=n*2-1
	for i in range(n):
		for j in range(n):
			a = max(m[i][j],m[n2-i][j],m[i][n2-j],m[n2-i][n2-j])
			s=s+a
	return s

ins=[]
for line in inputA:
    ins.append(line.strip())
q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index].strip().split())
	mx=[]
	index= index +1
	for j in range(n*2):
		t1=map(int , ins[index+j].strip().split())
		mx.append(t1)
	re = sumMx(mx,n)
	print re
	index = index + n*2