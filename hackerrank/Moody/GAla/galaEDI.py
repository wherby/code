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
ls3 =copy.deepcopy(ls)
avg= sum(ls3) /(n *2)
ls3= [x-avg for x in ls3]
ls2 =copy.deepcopy(ls3)

visted=[0]*q
index=2
adjL=[]
dic3={}



def fin(x,frm):
	global fix,fnum,g
	if fix[x] || f[x] == fnum:
		return -1
	f[x] =fnum
	for y in g[x]:
		if fix[x] ==0 && y !=frm:
			if f[y]== fnum:
				return y
			z = fin(x,y)
			if z!= -1:
				return z
	return -1


def finCir(n):
	global fnum
	fnum++
	for i in range(n):
		x = fin(i,0)
		if x != -1:
			return x
	return -1

def findCirclePointS(n):
	global fix
	points=[]
 	x =finCir(n)
 	while x != -1:
 		points.append(x)
 		fix[x] =1
 		x =finCir(n)
 	
 	return points

def go(x,frm):
	global v, f
	yes=v[x]
	no=0
	f[x]=frm
	nyes=0
	nno=0
	for y in g[x]:
		if y!=frm and f[y] !=fnum:
			nyes,nno= go(y,x)
			yes += nno
			no += max(nno,nyes)
	return (yes,no)

def sol(n):
	global f,fnum
	ans =0
	x =0
	y=0
	for i in range(n):
		if f[i] != fnum:
			x,y= go(i,-1)
			ans = max (x,y)

def pro(n):
	global g
	p = findCirclePointS(n):
	ans =0
	BMASK = 1 << len(p)
	for bmask in range(BMASK):
		fnum ++
		for i in range(len(p)):
			if bmask & (1 << i):
				for x in g[p[i]]:
					f[x] =fnum
				else:
					f[p[i]] = fnum
		ans = max(ans,sol(n))
	return ans




for i in range(n):
	adjL.append([])
for i in range(q):
	n1= map(int , ins[index+i].strip().split())
	n2 = (max(n1[0],n1[1]),min(n1[0],n1[1]))

	adjL[n1[0]-1].append(n1[1]-1)
	adjL[n1[1]-1].append(n1[0]-1)



def move(xx):
	ls2 =copy.deepcopy(ls)
	for i in range(n):
		t=ls2[i]
		for x in adjL[i]:
			n1=len(adjL[x])
			v1=ls[x]
			if n1 >1:
				t = t- float(v1)/(n1*xx)
		ls2[i]=t
	dic2 ={}
	for i in range(n):
		x = ls2[i]
		if x in dic2:
			dic2[x].append(i)
		else:
			dic2[x] = [i]
	ls2 =sorted(ls2)
	ls2.reverse()
	sm=0
	for i in range(n):
		t1 = ls2[i]
		n2 = dic2[t1]
		for n1 in n2:
			if visted[n1] == 0:
				sm = sm + ls[n1]
				for x in adjL[n1]:
					if visted[x] ==0:
						visted[x]=1
	return sm
smm=[]
for xx in range(1,6):
	smm.append(move(xx))
print max(smm)