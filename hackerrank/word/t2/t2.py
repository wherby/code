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
n,m, = map(int , ins[0].strip().split())
vs = map(int , ins[1].strip().split())
s1, = map(int , ins[2].strip().split())

sm=0
for i in range(n):
	if i == m :
		pass
	else:
		sm=sm + vs[i]

if sm/2 == s1:
	print "Bon Appetit"
else:
	v = s1 - sm/2
	print v