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



def findMin(x,ls):
	a=0
	b=len(ls)-1
	while a <b:
		mid= (a +b )/2
		if ls[mid] >=x:
			b = mid
		else:
			a = mid
	return a

def finMax(x,ls):
	a=0
	b=len(ls)-1
	while a <b:
		mid= (a +b )/2
		if ls[mid] >x:
			b = mid
		else:
			a = mid
	return a


q, = map(int , ins[0].strip().split())
ls= map(int , ins[1].strip().split())

def con
