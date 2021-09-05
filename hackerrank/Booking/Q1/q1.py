filename = "input/input001.txt"
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


q=len(ins)


index=0
a =0
b =0
c =0
for i in range(q):
	n= map(int , ins[index+i].strip().split())
	if len(n) != 4:
		continue
	if n[0] == n[1] and n[1] == n[2] and n[2] == n[3] and n[0] > 0:
		a =a +1
	elif n[0] ==n[2] and n[1] == n[3] and n[0] * n[1] > 0 and n[0]>0:
		b = b+1
	else:
		c = c+1
print a,b,c