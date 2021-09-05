filename = "input/input11.txt"
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
CONST=220

class SCC:
	def __init__(self,g,n):

		self.used = [0]*CONST
		self.g2 = []
		for i in range(CONST):
			self.g2.append([])
		

	def create(self,g,n):
		ns=[]
		ret=[]
		for i in range(1,n+1):
			self.dfs1(g,i,ns)
		for i in range(n-1,-1,-1):
			if self.used[ns[i]] !=2:
				re=[]
				self.dfs2(ns[i],re)
				ret.append(re)
		return ret

	def dfs1(self,g,x,ns):
		if self.used[x] ==1 :
			return
		self.used[x]=1
		for t1 in g[x]:
			self.g2[t1].append(x)
			self.dfs1(g,t1,ns)
		ns.append(x)

	def dfs2(self,x,co):
		if self.used[x] ==2 :
			return
		self.used[x] =2
		co.append(x)
		for t1 in self.g2[x]:
			self.dfs2(t1,co)


def overlap(l,r,a,b):
	if r < a :
		return 0
	if b < l :
		return 0
	return 1

def no(a,b):
	global g
	g[a].append(b^1)
	g[b].append(a^1)

def solve(l,r):
	global mx,g,CONST
	g =[]
	for i in range(CONST):
		g.append([])
	for i in range(l,r+1):
		for j in range(i+1,r+1):
			t1 = mx[i]
			t2 = mx[j]
			if overlap(t1[0],t1[1],t2[0],t2[1]):
				no(i*2,j*2)
			if overlap(t1[0],t1[1],t2[2],t2[3]):
				no(i*2,j*2+1)
			if overlap(t1[2],t1[3],t2[0],t2[1]):
				no(i*2+1,j*2)
			if overlap(t1[2],t1[3],t2[2],t2[3]):
				no(i*2+1,j*2+1)
	scc = SCC(g,CONST-2)
	ret =scc.create(g,CONST-2)
	for re in ret:
		re= sorted(re)

		for i in range(1,len(re)):
			if re[i] == (re[i-1] ^ 1):
				return 0
	return 1

q, = map(int , ins[0].strip().split())
index=1
mx=[]
g=[]
for i in range(q):
	n1, = map(int , ins[index].strip().split())
	CONST = n1*2 +4
	mx=[[]]
	g =[]
	for i in range(CONST):
		g.append([])
	for j in range(n1):
		ls= map(int , ins[index+j+1].strip().split())
		mx.append([ls[0], ls[1], ls[2], ls[3]])
	r = 1
	mxl=0
	st=1
	for x in range(1,n1+1):
		while r+1 <=n1 and solve(x,r +1):
			r = r+1
		if r-x >mxl:
			mxl=r -x
			st =x
		if r == n1 :
			break
	print st,st +mxl
	index = index + n1 +1

	