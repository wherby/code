filename = "input/input00.txt"
f=open(filename,'r')

import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line.strip())
l1 = map(int , ins[0].strip().split())
l2 = map(int , ins[1].strip().split())
s=0
for i in range(5):
	t1=l1[i]
	t2=l2[i]
	n= abs(t1-t2)
	if n <5:
		s=s+n
	else:
		s=s +10- n
print s