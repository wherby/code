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
mx =0
for i in range(q):
	ls= map(int , ins[index+i].strip().split())
	ls = sorted(ls)
	t1=ls[1]+ls[2]
	if t1 > mx:
		mx=t1
print mx