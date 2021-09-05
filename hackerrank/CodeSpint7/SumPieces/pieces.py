filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)



q, = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())

LLS =[ls[0],(ls[0]+ls[1])*3]
LLLS =[1]

t3=ls[0] + ls[1] *2

for i in range(2,q):
	t1 = ls[i]
	t2 = (LLS[i-1] + t1 * (2 ** (i-1)))*2
	print t2
	print t3
	t3= t3 +t1 *(i +1)
	print t3
	t4= t2 +t3 
	LLS.append(t4)
	LLLS.append(t3)
print LLS
print LLLS
