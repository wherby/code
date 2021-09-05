filename = "input/input01.txt"
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


def getNext(tr1):
	global mx1
	ls, val = tr1
	n = len(ls)
	mxval = 0
	re =0
	for i in range(q):
		if i not in ls:
			for j in range(n-1):
				tls =list(ls)
				start =tls[j]
				end = tls[j+1]
				tls.insert(j+1,i)
				tpval = val * mx1[start][i] * mx1[i][end] / mx1[start][end]
				if tpval > mxval:
					re = (tls,tpval)
					mxval = tpval
	return re


def transMatrix(k):
	global mtran,q
	for i in range(q):
		for j in range(q):
			if i != j:
				tr = mtran[i][j]
				tr1 = tr[k]
				re =getNext(tr1)
				mtran[i][j][k+1]=re

def findMostValue(tr1,tr2):
	mv=0
	re =(([],[]),1)
	for t1 in tr1:
		for t2 in tr2:
			if t1 !=0 and t2 !=0:
				ls1,v1 = t1
				ls2,v2 = t2
				n = len(ls1) + len(ls2) -2
				pv = (v1 * v2) **(1.0/n)
				if pv > mv:
					mv = pv 
					re = ((list(ls1),list(ls2)),pv)
				if abs(pv-mv) < 0.00001 and len(ls1) +len(ls2) < len(re[0][0]) + len(re[0][1]):
					mv = pv 
					re = ((list(ls1),list(ls2)),pv)
	return re


def findMostEffCir():
	global mtran,q,mostC,mostCircle,mx1,circleValue
	re = 0
	for i in range(q):
		for j in range(q):
			if i != j:
				tr1 =mtran[i][j]
				tr2 =mtran[j][i]
				re = findMostValue(tr1,tr2)
				mostC[i][j] = re
	mpv =0
	for i in range(q):
		for j in range(q):
			if i !=j:
				tp = mostC[i][j]
				lss,pv = tp
				if pv > mpv:
					mostCircle = lss
					mpv = pv
	ls1,ls2 = mostCircle
	ls1=list(ls1[0:len(ls1)-1])
	mostCircle = ls1 +ls2
	n = len(mostCircle)
	va = 1
	CONST = 1000000007
	for i in range(n-1):
		va = va * mx1[mostCircle[i]][mostCircle[i+1]] %CONST
	circleValue = va




q, = map(int , ins[0].strip().split())
x,s,f,m = map(int , ins[1].strip().split())
index = 2
mx1 = []
mtran = []
mostC =[]
mostCircle=[0,1,0]
circleValue=0
for i in range(q):
	ls= map(int , ins[index+i].strip().split())
	mx1.append(ls)
	ls2 = [0]*q
	mtran.append(ls2)
	ls3 =[0]*q
	mostC.append(ls3)
for i in range(q):
	for j in range(q):
		tp =[0] *q
		tp[0] =([i,j],mx1[i][j])
		mtran[i][j] = tp
#print mtran
#print mx1
for i in range(q-1):
	transMatrix(i)

findMostEffCir()

def findStepM(s,f,m):
	global mtran,q
	mx =0
	for i in range(q):
		if i !=s and i !=f:
			tr1 = mtran[s][i]
			tr2 = mtran[i][f]
			for t1 in tr1:
				for t2 in tr2:
					if t1 !=0 and t2 !=0:
						ls1,v1 = t1
						ls2,v2 =t2
						if len(ls1) +len(ls2)-2 ==m:
							tv = v1*v2
							if tv> mx:
								mx = tv
	tr1 = mtran[s][f]
	for t1 in tr1:
		if t1 != 0:
			ls1,v1 = t1
			if len(ls1) -1 == m:
				if v1 > mx:
					mx = v1
	return mx

def findStepMInCircle(s,f,m):
	global mtran,q,mostCircle
	mx =0
	for i in mostCircle:
		if i !=s and i !=f:
			tr1 = mtran[s][i]
			tr2 = mtran[i][f]
			for t1 in tr1:
				for t2 in tr2:
					if t1 !=0 and t2 !=0:
						ls1,v1 = t1
						ls2,v2 =t2
						if len(ls1) +len(ls2)-2 ==m:
							tv = v1*v2
							if tv> mx:
								mx = tv
	tr1 = mtran[s][f]
	for t1 in tr1:
		if t1 != 0:
			ls1,v1 = t1
			if len(ls1) -1 == m:
				if v1 > mx:
					mx = v1
	return mx

def exponen(base,exponent):
	CONST = 1000000007
	if base == 1:
		return 1
	result =1
	while exponent >0:
		if exponent &1:
			result=result *base %CONST
		exponent =exponent >>1
		base =base **2 %CONST
	return result %CONST

def resolve():
	global x,s,f,m,mostCircle,circleValue,mx1,mtran,q
	CONST = 1000000007
	v =1
	if m <q:
		v = findStepM(s,f,m) * x % CONST	
	else:
		if s in mostCircle or f in mostCircle:
			pc = (m-1)/(len(mostCircle)-1)
			rd = m - (len(mostCircle)-1) *pc
			v =exponen(circleValue,pc)
			v2 =findStepM(s,f,rd)
			v = v * v2 *x %CONST
			pc2 = (m-1)/(len(mostCircle)-1)-2
			rd2 = m - (len(mostCircle)-1) *pc2
			v2 = exponen(circleValue,pc2)
			v22 =findStepM(s,f,rd2)
			v3 = v2 * v22 *x %CONST
			if v3 > v:
				v = v3
		if s not in mostCircle and f not in mostCircle:
			pc = (m-2) /(len(mostCircle) -1)
			rd = m - (len(mostCircle)-1) *pc
			v = exponen(circleValue,pc)
			v2 = findStepMInCircle(s,f,rd)
			v = v * v2 *x %CONST
			pc2 = (m-2)/(len(mostCircle)-1)-2
			rd2 = m - (len(mostCircle)-1) *pc2
			v2 = exponen(circleValue,pc2)
			v22 =findStepM(s,f,rd2)
			v3 = v2 * v22 *x %CONST
			if v3 > v:
				v = v3
	print v
	#print len(mostCircle)-1
resolve()







# for i in range(q):
# 	for j in range(q):
# 		print mtran[i][j]
#print findStepM(s,f,m)
#print mtran

#print mostCircle,circleValue

