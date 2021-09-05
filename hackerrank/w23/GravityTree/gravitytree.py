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



n, = map(int , ins[0].strip().split())
mx=[0]*(n)
mx[0]=[1,1,0] # [index,level,parent]
ls = map(int , ins[1].strip().split())
for i in range(1,n):
	t=ls[i-1]
	level=0
	mx[i]=[i+1,0,t]

def bfsTreeLevel(mx,indexL,level):
	newIndex=[]
	for t in mx:
		if t[2] in indexL:
			mx[t[0]-1][1]=level
			newIndex.append(t[0])
	return (newIndex,level+1)
indexL=[1]
level=1
newIndex,level=bfsTreeLevel(mx,indexL,level+1)
while len(newIndex)>0:
	newIndex,level=bfsTreeLevel(mx,newIndex,level)
	pass

def bfsTree(mx,indexL,res):
	newIndex=[]
	for t in mx:
		if t[2] in indexL:
			res.append(t)
			newIndex.append(t[0])
	return (newIndex,res)

def getSubTree(mx,index):
	indexL=[index]
	res=[]
	res.append(mx[index-1])
	newIndex,res=bfsTree(mx,indexL,res)
	while len(newIndex)>0:
		newIndex,res=bfsTree(mx,newIndex,res)
	return res

def getWeight(plist,pa):
	wt=0
	for pt in plist:
		dlevel=pt[1]-pa[1]
		wt=wt+dlevel**2
	print wt

q, = map(int , ins[2].strip().split())
index=3
for i in range(q):
	a,b= map(int , ins[index+i].strip().split())
	pa=mx[a-1]
	plist= getSubTree(mx,b)
	getWeight(plist,pa)