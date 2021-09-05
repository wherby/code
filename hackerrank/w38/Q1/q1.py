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


def findN(ls,k):
	index =0
	allc =0
	while k >allc:
		allc =allc + ls[index]
		index = index +1
	return index


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,k,m= map(int , ins[index+i*2].strip().split())
	ls = map(int , ins[index+i*2+1].strip().split())
	print findN(ls,k)
