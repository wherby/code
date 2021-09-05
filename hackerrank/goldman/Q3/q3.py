filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/gs-codesprint/challenges/trader-profit/problem
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

def comdifLs(ls):
	cmls=[]
	n = len(ls)
	ini=0
	for i in range(n):
		if i ==0 :
			ini = ls[i]
		else:
			if ini * ls[i] >0:
				ini = ini + ls[i]
			else:
				cmls.append(ini)
				ini = ls[i]
	cmls.append(ini)
	#print cmls
	return cmls

def getProssibleMerge(n,ls):
	global mx
	m = len(ls)
	re =[]
	for i in range(m):
		if ls[i] >0 and i >1:
			tls = list(ls)
			tls[i]=sum(tls[i-2:i+1])
			del tls[i-1]
			del tls[i-1]
			if getMxN(n,tls) >= mx:
				re.append(tls)
		if ls[i] > 0 and i < m-2:
			tls = list(ls)
			tls[i] =sum(tls[i:i+3])
			del tls[i+1]
			del tls[i+1]
			if getMxN(n,tls) >= mx:
				re.append(tls)
	return re

def getAllProssible(n,lss):
	global mx
	m = len(lss)
	for i in range(m):
		mxtp = getMxN(n,lss[i])
		if mxtp > mx:
			mx = mxtp
	re = []
	for ls in lss:
		rels = getProssibleMerge(n,ls)
		re.extend(rels)
	return re

def deepFindls(n,ls):
	lss = [ls]
	re =getAllProssible(n,lss)
	while len(re)>0:
		re = getAllProssible(n,re)


def getMxN(n,ls):
	nls = filter(lambda x: x>0,ls)
	nls = sorted(nls)
	return sum(nls[len(nls)-n:])

def getMxNum(n,ls):
	global mx
	nls = filter(lambda x: x>0,ls)
	nls = sorted(nls)
	if len(nls) <n:
		return sum(nls)
	else:
		deepFindls(n,ls)
		return mx

def getNum(n,ls):
	difls =[]
	num = len(ls)
	for i in range(num-1):
		difls.append(ls[i+1] - ls[i])
	cmdls = comdifLs(difls)
	print getMxNum(n,cmdls)
	#getProssibleMerge(n,cmdls)
	
	


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	mx =0
	n,= map(int , ins[index+i*3].strip().split())
	ls = map(int , ins[index+i*3+2].strip().split())
	getNum(n,ls)