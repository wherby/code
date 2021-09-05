#https://www.hackerrank.com/challenges/insertionsort1
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
index=1
ar= map(int , ins[1].strip().split())
t = ar[q-1]
isFinish=False
for i in range(q-2,-2,-1):
	if i <0:
		ar[0] = t
	else:
		if t < ar[i]:
			ar[i+1]=ar[i]
		else:
			ar[i+1]=t
			isFinish=True
	re = map(str,ar)
	print " ".join(re)
	if isFinish == True:
		break