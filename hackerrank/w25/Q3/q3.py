filename = "input/input00.txt"
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

def getN(a,b,c):
	if c ==0:
		return 0
	if a ==c or b ==c:
		return 1
	m1 = max(a,b)
	if m1 > c:
		return 2
	else:
		if c%m1 ==0:
			return c /m1
		else:
			return c / m1 +1
q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	a,b,c= map(int , ins[index+i].strip().split())
	print getN(a,b,c)
