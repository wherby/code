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



	

n, = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())
pl=[0]*(n+1)
for i in range(n+1):
	pl[i]=[]
for i in range(n-1):
	t=ls[i]
	pl[t].append(i+2)
print pl
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
print spl

def bfsTreeLevel(mxdic,indexL,level):
	global pl
	newIndex=[]
	for i in indexL:
		tp1=pl[i]
		for j in tp1:
			mxdic[j]=[level,i]
		newIndex.extend(pl[i])
	return (newIndex,level+1)

mxdic={}
mxdic[1]=[1,0] #[level,parent]
indexL=[1]
level=1
newIndex,level=bfsTreeLevel(mxdic,indexL,level+1)

while len(newIndex)>0:
	newIndex,level=bfsTreeLevel(mxdic,newIndex,level)
#print mxdic


def getWeight(plist,pa):
	global mxdic
	wt=0
	for p in plist:
		pt=mxdic[p]
		dlevel=pt[0]-pa[0]
		wt=wt+dlevel**2
	print wt

q, = map(int , ins[2].strip().split())
index=3
for i in range(q):
	a,b= map(int , ins[index+i].strip().split())
	pa=mxdic[a][0]
	plist= spl[b]
	pt=[mxdic[i][0]-pa for i in plist]
	sm= sum([x**2 for x in pt])
	print sm
	#getWeight(plist,pa)
	#print mxdic