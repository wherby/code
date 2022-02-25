#https://www.hackerrank.com/contests/world-codesprint-7/challenges/gridland-metro
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



n,m,q = map(int , ins[0].strip().split())
index=1
dic={}
for i in range(q):
	line,start, end = map(int , ins[index + i].strip().split())
	if line in dic:
		dic[line].append((start,end))
	else:
		dic[line]=[(start,end)]

def getRange(ranges):
	l1=[]
	for r1 in ranges:
		isMerge = False
		start,end=r1
		for i in range(len(l1)):
			r2 = l1[i]
			start2,end2 = r2
			if not (start >end2 or start2 > end):
				l1[i] = (min(start,start2),max(end,end2))
				isMerge=True
		if isMerge == False:
			l1.append(r1)
	sm=0
	for r in l1:
		start,end = r
		sm = sm + end -start +1
	return sm

mx=0
for (key,value) in dic.items():
	
	mx =  mx +getRange(value)

print(m*n- mx)