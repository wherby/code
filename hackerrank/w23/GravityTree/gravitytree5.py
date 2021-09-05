filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import copy
from collections import deque

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)



	
#[level, parent-list]
n, = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())
dic={}
vt=[1]
pl=[0]*(n+1)
pvl=[0]*(n+1)
for i in range(n+1):
	pl[i]=[]
for i in range(n-1):
	t=ls[i]
	pl[t].append(i+2)
for i in range(n):
	tp=pl[i+1]
	for j in tp:
		pvl[j]=i+1
#print pl
#print pvl

plevel=[1]*(n+1)
LCA=[0]*(n+1)
dicLen={}
pps=[0]*(n+1)
for i in range(n+1):
	pps[i]=[]
pps[1].append(1)

def dfsTreeLCA(pl,dicLen):
	global plevel,LCA,pps
	plt=copy.deepcopy(pl)
	ving=set([1])
	ved=set()
	pstak=[1]
	LCA[1]=1
	while len(pstak)!=0:
		t=pstak[-1]
		level= plevel[t]
		if len(plt[t])!=0:
			x1=plt[t][-1]
			LCA[x1]=x1
			pps[x1]=[x1]
			plt[t].pop()
			plevel[x1]=level+1	
			for v1 in ved|ving:
				lca1=LCA[v1]
				dicLen[(min(v1,x1),max(v1,x1))]=abs(plevel[v1]-plevel[lca1])+abs(plevel[x1]-plevel[lca1])
			ving.add(x1)
			pstak.append(x1)
		else:
			ved.add(t)
			xd= pstak.pop()
			pxd=pvl[xd]
			for tp1 in pps[xd]:
				LCA[tp1]=pxd
				pass
			pps[pxd].extend(pps[xd])
			#LCA=[pxd if x == xd else x for x in LCA]
	#print ving
	#print ved
	#print plevel
	#print dicLen


dfsTreeLCA(pl,dicLen)

spl=[0]*(n+1)
def bfsSPL(indexL,re):
	global pl
	newIndex=[]
	for i in indexL:
		tp=pl[i]
		re.extend(tp)
		newIndex.extend(tp)
	return newIndex
for i in range(1,n+1):
	re=[i]
	indexL=[i]
	newIndex=bfsSPL(indexL,re)
	while len(newIndex)>0:
		newIndex=bfsSPL(newIndex,re)
	spl[i]=re
#print spl


def getWeight(plist,pa):
	global dicLen
	wt=0
	for pt in plist:
		if pa != pt:
			dlevel=dicLen[(min(pt,pa),max(pt,pa))]
			wt=wt+dlevel**2
	print wt

q, = map(int , ins[2].strip().split())
index=3
startSet=set()
endSet=set()
for i in range(q):
	a,b= map(int , ins[index+i].strip().split())
	startSet.add(a)
	endSet.add(b)
	plist= spl[b]
	getWeight(plist,a)