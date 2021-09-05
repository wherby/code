#https://www.hackerrank.com/contests/stryker-codesprint/challenges/point-filtering
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

q, = map(int , ins[0].strip().split())
lsa= map(int , ins[1].strip().split())
lsb= map(int , ins[2].strip().split())
mx=q+1
sa=set(lsa)
sb=set(lsb)
mxs=[]
for i in range(q):
	t1=lsa[i]
	if t1 in sb:
		j=lsb.index(t1)
		if abs(i-j)<mx:
			mx=abs(i-j)
			mxs=[mx,t1]
		if abs(i-j) == mx:
			if t1 < mxs[1]:
				mxs=[mx,t1]
print mxs[1]
