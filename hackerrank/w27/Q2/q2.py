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


n,p = map(int , ins[0].strip().split())
ls= map(int , ins[1].strip().split())
ls = sorted(ls)

def getN(ls,p):
	dic1 = {}
	mx=0
	sm =0
	for l in ls:
		t1 = l /p
		if l %p !=0:
			t1 = l/p +1
		if mx >= t1:
			t1 = mx+1
		sm = sm + t1
		mx = t1
	return sm
print getN(ls,p)