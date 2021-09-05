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


#print ins

d1={}

n,m = map(int , ins[0].strip().split())
index=1
ls=[]
lsPick=[]
lsNotPick=[]
p=[]
col=[]
md=[]
for i in range(m):
	a,b,c,d,= map(int , ins[index+i].strip().split())
	tls=[min(a,b),max(a,b),c,d]
	ls.append(tls)
	p.append(i)
	col.append(i)
	md.append(c*1.00000/d)

#print md
md = sorted(md)
l =md[0]
r =md[-1]
#print md

A=0
B=0
rk = [1] *m
w=[0]*m

def get(u):
	global col
	if col[u] == u:
		return u
	col[u] = get(col[u])
	return col[u]

def swap(u,v):
	return v,u

def join(u,v):
	global rk
	u =get(u)
	v =get(v)
	#print u,v
	if u == v:
		#print "ccc"
		return False
	if rk[u] > rk[v]:
		#print u,v
		u,v = swap(u,v)
		#print "after", u ,v
	rk[v] = rk[u] + rk[v]
	col[u] =v
	#print col
	return True


def cmp1(x,y):
	if x> y:
		return -1
	else:
		return 1

def check(mid):
	global ls,m,p,col,A,B,rk,w
	w=[0] *m

	for i in range(m):
		p[i]= i
		w[i] = ls[i][2] - ls[i][3] * mid
	#print p
	p=sorted(p,cmp = lambda x,y:cmp1(w[x],w[y]))
	#print w
	#print p
	for i in range(m):
		col[i] = i
	rk = [1] *m
	A =0
	B =0
	for i in range(m):
		xid = p[i]

		#print ls[xid][0],ls[xid][1]
		if join(ls[xid][0],ls[xid][1]) == True:

			#print A,B
			A = A+ ls[xid][2]
			B = B + ls[xid][3]
			
	return A >= B *mid

for x in range(100):
	mid= (l +r) /2
	#print mid
	if check(mid) > 0:
		l = mid
	else:
		r = mid

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

def printRs(num1,num2):
	gd=gcd(num1,num2)
	reStr = str(num1/gd) + "/" + str(num2/gd)
	print reStr

printRs(A,B)	
