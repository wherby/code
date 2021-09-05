#https://www.hackerrank.com/challenges/array-splitting
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


def partLs(ls,n):
	zc=filter(lambda x: x!= 0,ls)
	if len(zc)==0:
		return len(ls)-1
	sm= sum(ls)
	sm1=0
	for i in range(n):
		sm1=sm1+ls[i]
		if sm1*2>sm:
			return 0
		elif sm1*2==sm:
			lf=ls[:i+1]
			rt=ls[i+1:]
			return max(partLs(lf,len(lf)),partLs(rt,len(rt))) +1
			break
		else:
			pass
	return -1


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index+i*2].strip().split())
	ls= map(int , ins[index+i*2+1].strip().split())
	cnt =partLs(ls,n)
	print cnt