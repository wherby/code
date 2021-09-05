#https://www.hackerrank.com/contests/moodysuniversityhackathon/challenges/distinctly-colored-nodes-in-a-tree
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

q, = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())
dic = {}
for x in ls :
	if x in dic :
		dic[x] = dic[x]+1
	else:
		dic[x] =1

N1=len(dic)
dic2={}
dicL=[]
def get(i):
	global dic
	if dic[i] ==1:
		return 1
	else:
		return 0

for i in range(q):
	dicL.append([{ls[i]:1},get(ls[i])])

def addDic(a1,b1):
	global dic
	a,an=a1
	b,bn=b1
	for k,v in b.items():
		if k in a :
			a[k]=a[k] + b[k]
		else:
			a[k]=v
		if a[k] == dic[k]:
			an=an+1
	return (a,an)


# def addNode(i,dic2):
# 	global ls,dic
# 	t = ls[i-1]
# 	plusOne=0
# 	if t in dic2:
# 		dic2[t]=dic2[t] +1
# 	else:
# 		dic2[t]=1
# 	if dic2[t] == dic[t]:
# 		plusOne=1
# 	return (len(dic2),plusOne)

# def sumNode(sm1,oldlen,newlen,plusOne):
# 	if plusOne == 1:
# 		oldlen=oldlen -1
# 	x1 = oldlen *newlen
# 	sm1 = sm1 +x1
# 	print sm1 ,x1
# 	return (sm1,oldlen)

dicVisted=set()

index=2
sm=0

adjL=[]
for i in range(q):
	adjL.append([])

ccl = [0] * q
for i in range(q-1):
	n= map(int , ins[index+i].strip().split())
	adjL[n[0]-1].append(n[1]-1)
	adjL[n[1]-1].append(n[0]-1)
	ccl[n[0]-1]=ccl[n[0]-1] +1
	ccl[n[1]-1]=ccl[n[1]-1] +1

mini =q
minid=0
for i in range(q):
	t = ccl[i]
	if t <mini:
		mini =t
		minid =i



used=[0]*q
# def dfs1(g,x,ns):
# 	global used
# 	if used[x] ==1 :
# 		return
# 	used[x]=1
# 	for t1 in g[x]:
# 		dfs1(g,t1,ns)
# 	ns.append(x)


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
dfs(adjL,minid,ns)
ns.reverse()
for i in range(q-1):
	t=ns[i]
	q1= adjL[t]
	tmdic = dicL[t]
	for x in q1:
		if x in dicVisted:
			if len(tmdic[0]) < len(dicL[x][0]):
				tmdic = addDic(dicL[x],tmdic)
			else:
				tmdic = addDic(tmdic,dicL[x])
			dicL[x]={}
	L1=len(tmdic[0])
	l2=N1- tmdic[1]
	dicVisted.add(t)
	dicL[t]=tmdic
	sm = sm + L1 *l2
print sm

