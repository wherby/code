#https://www.hackerrank.com/challenges/maxsubarray
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

def getContiguousSum(ls):
	re=[]
	s=0
	n= len(ls)
	for i in range(n):
		s=s+ls[i]
		if s<0:
			s=0
		else:
			re.append(s)
	if len(re)==0:
		return max(ls)
	mx= max(re)
	return mx

def getNoContiguousSum(ls):
	re=filter(lambda x: x>0,ls)
	mx= sum(re)
	if len(re)==0:
		return max(ls)
	return mx


q, = map(int , ins[0].strip().split())
index=1

for i in range(q):
	ls= map(int , ins[index+i*2+1].strip().split())
	csm=getContiguousSum(ls)
	ncsm=getNoContiguousSum(ls)
	print str(csm)+" " + str(ncsm)