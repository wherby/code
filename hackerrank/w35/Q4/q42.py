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

def GetMaxLinkedLine(ls,k):
	mostLeft=ls[k]
	mostRight=ls[k]
	n = len(ls)
	re = [0]*n
	ms = mostRight
	righIndex= k
	leftIndex =k
	for i in range(k+1,n):
		ms = ms + ls[i]
		if ms >= mostRight:
			mostRight = ms
			righIndex =i
	ms = max(mostRight,ms)
	mostLeft = max(mostRight,mostLeft)
	for i in range(k):
		#print "LLLLLLL"
		ms = ms +ls[k-1-i]
		if ms >= mostLeft:
			mostLeft = ms
			leftIndex = k-1-i
		#print i,ms
	for i in range(leftIndex,righIndex +1):
		re[i] = mostLeft
	for i in range(leftIndex):
		re[leftIndex -1 -i] = re[leftIndex -i] + ls [leftIndex -1 -i]
	for i in range(righIndex+1,n):
		re[i] = re[i-1] + ls[i]
	#print ls,k,re,ms,leftIndex,righIndex,mostRight,mostLeft
	return re 


n,m = map(int , ins[0].strip().split())
index=1
MX =[]
MX1 = []
for i in range(n):
	ls= map(int , ins[index+i].strip().split())
	MX.append(ls)

re = [0]*m
for i in range(n):
	tp = MX[i]
	reNext = [-111111111111111] *m
	for j in range(m):
		tp1=[0] *m
		for k in range(m):
			if k != j:
				tp1[k] = tp[k]
			else:
				tp1[k] = tp[k] + re[k]
		reTp = GetMaxLinkedLine(tp1,j)
			#print "XXXX"
			#print tp1,k
		#print reTp,tp1,k
		for k in range(m):
			reNext[k] = max(reNext[k],reTp[k])
	re = reNext
	#print "***"
	#print re, tp 
print max(re)

#print GetMaxLinkedLine(MX[1],1)



