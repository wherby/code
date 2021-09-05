filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import copy

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


n,q = map(int , ins[0].strip().split())
ls =  map(int , ins[1].strip().split())
ls2 =copy.deepcopy(ls)


visted=[0]*q
index=2
adjL=[]
dic3={}
wt=[0] * (2 *n)
lins=[]
for i in range(n):
	adjL.append([])
for i in range(q):
	n1= map(int , ins[index+i].strip().split())
	n2 = (max(n1[0],n1[1]),min(n1[0],n1[1]))
	if n2 not in dic3:
		lins.append([n1[0]-1,n1[1]-1])
		adjL[n1[0]-1].append(n1[1]-1)
		adjL[n1[1]-1].append(n1[0]-1)
		dic3[n2]=1

starter=[]
for i in range(n):
	if len(adjL[i])>2:
		starter.append(i)


def dfs(graph, start,ns):
    global used
    stack=[start]
    used[start]=1
    while len(stack)>0:
    	tp = stack.pop()
    	ns.append(tp)
    	for x in graph[tp]:
    		if used[x] !=1:
    			stack.append(x)
    			used[x]=1

ns=[]
used =[0]*n
dfs(adjL,0,ns)

def vistB(b,re):
	global visted,wt,adjL,ls,starter,dic3
	print "in"
	print re
	if visted[b] ==0:
		visted[b]=1
		wb=ls[b]
		bn=adjL[b]
		withouB=0
		withB=0
		for i in bn:
			if wt[i*2]>=withouB:
				withouB=max(wt[i*2],re[0])
				print wt[i*2],wt[i*2+1],re[0]
			if wt[i*2+1] > withB:
				withB =max(wt[i*2+1],re[1])
		wt[b*2 +1] = withouB
		wt[b*2] =withB +wb
		# for i in starter:
		# 	if visted[i] !=0:
		# 		a1=(max(i,b),min(i,b))
		# 		if i !=b and i not in bn:
		# 			wt[i*2] =wt[i*2]+wb
		# 			wt[i*2+1] = wt[i*2+1] +wb
	return [wt[2*b],wt[2*b+1]]

privious=-1
re =[0,0]
for i in range(n):

	re=vistB(ns[n-i-1],re)
	print re
	privious=i
print max(wt)

	




