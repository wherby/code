#https://www.hackerrank.com/challenges/primsmstsub
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




n,m = map(int , ins[0].strip().split())
index=1
wdic={}
for i in range(m):
	a,b,k= map(int , ins[index+i].strip().split())
	wdic[(a,b)]=k

start,=map(int , ins[m+1].strip().split())
vset=set()
re=[]
mx=1000000
sp=0
wt=0
for (a,b) in wdic.keys():
	if a == start or b ==start:
		if wdic[(a,b)] < mx:
			mx=wdic[(a,b)]
			sp=(a,b)
a,b=sp
wt=wt+mx
vset=vset | set([a]) |set([b])

def getNext(vset,wdic,wt):
	mx=1000000
	sp=0
	for (a,b) in wdic.keys():
		if (a in vset and b not in vset) or (a not in vset and b in vset):
			if wdic[(a,b)] < mx:
				mx =wdic[(a,b)]
				sp=(a,b)
	(a,b)=sp
	vset=vset | set([a]) |set([b])
	wt=wt+mx
	return (vset,wt)

while len(vset) != n:
	vset,wt =getNext(vset,wdic,wt)


print wt