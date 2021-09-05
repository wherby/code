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





k,q = map(int , ins[0].strip().split())
ls=map(int , ins[1].strip().split())
index=2
for i in range(q):
	l,r,x,y= map(int , ins[index+i].strip().split())
	tp= ls[l:r+1]
	ltp = filter(lambda z: z % x ==y,tp)

	print len(ltp)