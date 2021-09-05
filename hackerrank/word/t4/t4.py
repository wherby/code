filename = "input/input00.txt"
f=open(filename,'r')

import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin

def isEq(a1,a2):
	n= len(a2)
	n2=len(a1)
	index=0 
	ft=0
	for i in range(n):
		t1=a2[i]
		for j in range(index,n2):
			if a1[j] == t1:
				index = index +1
				ft=ft+1
				break
			index = index +1
	if ft==n:
		return True
	else:
		return False

ins=[]
for line in inputA:
    ins.append(line.strip())
q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	a1,=ins[index].strip().split()
	a2,=ins[index+1].strip().split()
	a3 =filter(lambda a : a <='Z' and a >='A',a1)
	a1=a1.upper()
	a2=a2.upper()
	if isEq(a1,a2) and isEq(a2,a3):
		print "YES"
	else:
		print "NO"

	index = index + 2

