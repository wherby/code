filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
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

maxn=100100
ordL=[]

def pre(u):
	global used,adjL,ordL
	used[u] = 1
	for v in adjL[u]:
		if used[v] != 1:
			pre(v)
	ordL.append(u)

def puti(u,x):
	pass



n,m,q = map(int , ins[0].strip().split())
ls= [0]*(n+1)
dic1={}
grapPart=[]
dic2={}
index=1
grap=[]
adjL=[]
for i in range(n+1):
	adjL.append([])
for i in range(m):
	s1,e1= map(int , ins[index+i].strip().split())
	grap.append((s1,e1))
	adjL[s1].append(e1)
grap=sorted(grap,key = lambda x: x[0])

partitian(ls,grap)

getStartPoint(grap)

llst=[]
for i in range(n+1):
	t = LinkedList()
	t.insert(i)
	llst.append(t)
generateLinListTree(grap)

for i in range(n+1):
	print llst[i]

print grapPart
print ls