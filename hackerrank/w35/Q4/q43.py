filename = "input/input00.txt"
f=open(filename,'r')

import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)


def GetMaxLin(ls):
	n = len(ls)
	re =[0] * n
	for i in range(n):
		re [i] =ls[i]
	mx =ls[0]
	sm = 0
	for i in range(n):
		t =ls[i]
		if sm <0:
			sm =0
			start = i +1
		else:
			start =i
		sm = sm + t
		if sm > mx:
			mx =sm
			for x in range(start,i+1):
				re[x] = sm
		if re[i] < sm:
			re[i] = sm 
	sm = 0
	for i in range(n):
		t =ls[n-1-i]
		if sm <0:
			sm =0
			start = n-1-i-1
		else:
			start =n-1-i
		sm = sm + t
		if sm > mx:
			mx =sm
			for x in range(n-1-i,start+1):
				re[x] = sm
		if re[n-1-i] < sm:
			re[n-1-i] = sm
	for i in range(n):
		if ls[i] >=0:
			j =i+1
			while j < n and  ls[j]>=0:
				j=j +1
			mxv = max(re[i:j])
			for k in range(i,j):
				re[k] = mxv
			i = j 

	return re

n,m = map(int , ins[0].strip().split())
index=1
MX =[]
MX1 = []
for i in range(n):
	ls= map(int , ins[index+i].strip().split())
	MX.append(ls)
for i in range(n):
	re = GetMaxLin(MX[i])
	MX1.append(re)
re = [0] *m
for i in range(n-1):
	for j in range(m):
		re[j] = re[j] + MX1[i][j]
reNext = [-111111111111111] *m
tp = MX[n-1]
for j in range(m):
	tp1=[0] *m
	for k in range(m):
		if k != j:
			tp1[k] = tp[k]
		else:
			tp1[k] = tp[k] + re[k]
	reTp = GetMaxLin(tp1)
	for k in range(m):
		reNext[k] = max(reNext[k],reTp[k])
print reNext[m-1]