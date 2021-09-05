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

def isLuck(q):
	a1 = q% 1000
	a2 = q/1000
	a3 = a1 %10  + a1/10%10 + a1/10/10 
	a4 = a2 %10 + a2/10%10 + a2/10/10
	if a3 == a4:
		return True
	else:
		return False

q= map(int , ins[0].strip().split())[0]
for x in range(q+1,q+2000):
 if isLuck(x):
 	print x
 	break