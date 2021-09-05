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



def getLineSpan(ls):
	re =[]
	m = len(ls)
	start =0
	sm =0
	for i in range(m):
		tp = ls[i]
		if tp >= 0:
			if start == -1:
				start = i
			sm = sm +tp
			if i == m-1:
				re.append([start,m,sm])
				sm = 0
		else:
			if start >=0 and sm >0:
				end = i 
				re.append([start,end,sm])
				start = -1
				sm =0
			re.append([i,i+1, sm+tp])
			sm =0
			start = i +1
	n = len(re)
	for i in range(n-1):
		span1 = re[i]
		for j in range(i+1,n):
			span2 = re[j]
			sm = sum(ls[span1[0]:span2[1]])
			re.append([span1[0],span2[1],sm])
	return re

def genAllPoss(span1,span2,x):
	global MX
	uper = MX[x]
	downer = MX[x+1]
	re =[]
	start1,end1,v1 = span1
	start2,end2,v2 = span2
	if start1 >= end2:
		for i in range(end2-1,start1+1):
			tsm = sum(uper[i:start1]) + sum(downer[end2:i+1]) + v1 +v2	
			re.append([start2,i+1, tsm])
	elif start2 >= end1:
		for i in range(end1-1,start2 +1):
			tsm = sum(uper[end1:i+1]) + sum(downer[i:start2]) + v1 + v2
			re.append([i,end2,tsm])
	else:
		re.append([start2,end2,v1+v2])
	return re



def interSpan(ls1,ls2,x):
	re =[]
	for span1 in ls1:
		for span2 in ls2:
			tre = genAllPoss(span1,span2,x)
			re.extend(tre)
	return re
			

def SimplySpan(mergerSpan):
	re =[]
	dic1 = {}
	for span in mergerSpan:
		start,end,v = span
		if (start,end) not in dic1:
			dic1[(start,end)] = v
		else:
			k = dic1[(start,end)]
			if k < v:
				dic1[(start,end)] =v
	for key,v in dic1.items():
		start,end = key
		re.append([start,end,v])
	return re


n,m = map(int , ins[0].strip().split())
index=1
MX =[]
for i in range(n):
	ls= map(int , ins[index+i].strip().split())
	MX.append(ls)
MX1 =[]
for i in range(n):
	tp1 = getLineSpan(MX[i])
	MX1.append(tp1)
re= interSpan(MX1[0],MX1[1],0)

tpmerge = MX1[0]
for i in range(1,n):
	tp1 = MX1[i]
	tpmerge = interSpan(tpmerge,tp1,i-1)
	tpmerge = SimplySpan(tpmerge)
Found = False
mxValue =0
for span1 in tpmerge:
	start, end,v = span1
	if end == n:
		if v > mxValue:
			mxValue = v
			Found = True
if Found == False:
	for span1 in tpmerge:
		start,end,v = span1
		tv = v + sum(MX[n-1][end:m]) 
		if tv > mxValue:
			mxValue = tv
print mxValue 
