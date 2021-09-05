f = open('input/input00.txt')
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
q, = map(int , ins[0].strip().split())
index =1
ls = map(int , ins[1].strip().split())
mx=0
al=[]
def updateLs(dic,mx,v):
	re={}
	n=len(dic)
	kl=dic.keys()
	for i in range(n):
		t1,ns=kl[i],dic[kl[i]]
		if t1 <= v:
			re[t1]=ns+1
		else:
			mxt=t1*ns
			if mx <mxt:
				mx=mxt
			if v not in dic:
				if v not in re:
					re[v]=ns+1
				else:
					rev=re[v]
					if rev < ns+1:
						re[v]=ns+1
	if v not in re:
		re[v]=1
	return (re,mx)

def getMax(dic,mx):
	n=len(dic)
	kl=dic.keys()
	for i in range(n):
		t1,ns=kl[i],dic[kl[i]]
		mxt=mxt=t1*ns
		if mx <mxt:
			mx=mxt
	return mx


dic={}
mx=0
for i in range(q):
	t1=ls[i]
	dic,mx=updateLs(dic,mx,t1)

mx=getMax(dic,mx)
print mx
