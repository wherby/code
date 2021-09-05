#https://www.hackerrank.com/contests/world-codesprint-7/challenges/similar-strings
#Running time error
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

def getListArray(ls):
	dic = {}
	n = len(ls)
	for i in range(n):
		t = ls[i]
		if t in dic:
			dic[t].append(i)
		else:
			dic[t]=[i]
	return dic

def getTransArray(rrs,index):
	keyList = rrs.keys()
	for k,v in rrs.items():
		if v[0] < index:
			del v[0]
			if len(v) ==0:
				del rrs[k]
	keyList = rrs.keys()
	tdic={}
	for k,v in rrs.items():
		tdic[v[0]]=k
	klist=sorted(tdic.keys())
	ttdic={}
	for i in range(len(klist)):
		k1 = tdic[klist[i]]
		ttdic[k1]=i
	return (ttdic,rrs)

def getListFromIndex2(ls,index,tdicList):
	tdic = tdicList
	lv =ls[index:]
	for k,v in tdic.items():
		lv =lv.replace(k,str(v))
	return lv




def compareString(ls1,ls2):	
	if ls1  == ls2 :
		return True
	else:
		return False

def getArray(ls,start,end):
	le= end-start+1
	re = []
	n =len(ls)
	t1=n - end + start
	for i in range(t1):
		re.append(ls[i:i+le])
	return re

n,q = map(int , ins[0].strip().split())
ls = ins[1].strip()

rrs =getListArray(ls)


lls=[]
for i in range(n):
	tdic,rrs = getTransArray(rrs,i)
	t2 = getListFromIndex2(ls, i,tdic)
	lls.append(t2)

index=2
for i in range(q):
	start,end= map(int , ins[index+i].strip().split())
	st1= lls[start-1][0:end-start+1]
	ree = filter(lambda x : x[0:end-start+1] == st1,lls)
	print len(ree)