filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w38/challenges/a-time-saving-affair/problem

import math
import sys

if  "f" in locals():
	inputA=f
else:
	inputA=sys.stdin


ins=[]
for line in inputA:
	ins.append(line)




n, = map(int , ins[0].strip().split())
k, = map(int , ins[1].strip().split())
m, = map(int , ins[2].strip().split())
dic1={}
res = []
for i in range(n+1):
	res.append([])

def roundValue(n1):
	x1 = n1 /k
	if x1 %2 ==1:
		return (x1+1) *k
	else:
		return n1

def bfs():
	global dic1, res,n
	minValue = 1000000000
	minPoint = 0
	for k,v in dic1.items():
		for x in  res[k]:
			y,v1 = x
			if y not in dic1:
				tmp = roundValue(v) +v1
				if tmp < minValue:
					minValue =tmp
					minPoint = y
	dic1[minPoint] = minValue


## bfs with incremental with effential
def bfsWithP(newP):
	global dic1, res, vstack
	v = dic1[newP]
	for key,value in res[newP]:
		if key not in dic1:
			temp  = roundValue(v) + value
			if vstack[key] > temp:
				vstack[key] = temp
	index = 0
	minValue = 10000000
	for i in range(n+1):
		if vstack[i] < minValue:
			minValue = vstack[i]
			index = i
	dic1[index] = minValue
	vstack[index] = 100000000
	return index

index=3
for i in range(m):
	f,t,v= map(int , ins[index+i].strip().split())
	res[f].append([t,v])
	res[t].append([f,v])
vstack = [10000000] *(n+1) 
dic1[1] = 0
nextP = 1
while n not in dic1:
	nextP = bfsWithP(nextP)
	
print dic1[n]