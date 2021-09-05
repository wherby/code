filename = "input/input02.txt"
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
for i in range(n):
	adjL.append([])
for i in range(q):
	n1= map(int , ins[index+i].strip().split())
	n2 = (max(n1[0],n1[1]),min(n1[0],n1[1]))
	if n2 not in dic3:
		adjL[n1[0]-1].append(n1[1]-1)
		adjL[n1[1]-1].append(n1[0]-1)
		dic3[n2]=1

starter=set()
for i in range(n):
	if len(adjL[i]) >2:
		starter.add(i)
		visted[i]=2
starterCopy=copy.deepcopy(starter)

if len(starter) ==0:
	starter=[0]
path={}
# 00 01 10 11
def visitNode(x,tdic):
	global visted,adjL
	nextP= adjL[x][0]
	if visted[x]==0:
		t1 =ls[x]
		if str(x) == tdic[4] :
			t00=0
		# elif visted[nextP]==0:
		# 	t00=max(tdic[0]+t1,tdic[1])
		else:
			t00 =max(tdic[0],tdic[1])
		if visted[nextP]==0:
			t01=max(tdic[0]+t1,tdic[1])
		else:
			t01=max(tdic[0],tdic[1])
		if str(x) == tdic[4]:
			t10=0
		else:
			t10 =max(tdic[2],tdic[3])
		if str(x) == tdic[4]:
			t11=0
		elif visted[nextP]==0:
			t11=max(tdic[2]+t1,tdic[3])
		else:
			t11=max(tdic[2],tdic[3])
		visted[x]=1
		tdic = [t00,t01,t10,t11,tdic[4]]

	return tdic

def dfsOnePath(x,tdic):
	global visted,adjL
	stack = [x]
	while len(stack)>0:
		tp=stack.pop()
		a1=adjL[tp]
		for a2 in a1:
			if visted[a2]==0:
				stack.append(a2)
		tdic =visitNode(tp,tdic)
	return tdic

endDic={}
while starter:
	a=starter.pop()

	for x in adjL[a]:
		t1=ls[x]
		tdic=[0,0,0,0,str(x)]
		tdic=dfsOnePath(x,tdic)
		endDic[tdic[4]]=tdic[0:4]
sm =0
a00=0
a01=0
a10=0
a11=0
starterNum=0
for j in starterCopy:
	x = adjL[j]
	t1 = ls[j]
	starterNum=starterNum+ t1

	re =[]
	for a1 in x:
		ret = endDic[str(a1)]
		re.append(ret)

	for a1 in re:
		a00 = a1[0] + a00
		a01=a1[1] +a01
		a10=a1[2] +a10
		a11 = a1[3] +a11
mx = max(a00 ,a01,a10+starterNum,a11)
sm = sm +mx

print sm

		


