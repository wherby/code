filename = "input/input03.txt"
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






q, = map(int , ins[0].strip().split())
ls= map(int , ins[1].strip().split())
ISRMQ =True
qn =q


dic = {}
if ISRMQ == True:
	for i in ls:
		if i in dic:
			dic[i] = dic[i] + 1
		else:
			dic[i]=1


RMQ = [0] * (q*2-1)

def removeLowerLevel(dic,keys):
	for k in keys:
		dic[k] = dic[k]-1
		if dic[k]==0:
			del dic[k]
	return dic


def formLowerLevel(dic,q):
	global RMQ,ISRMQ,qn
	keys = dic.keys()
	keys = sorted(keys)
	keyVisted=[]
	if len(keys) !=q:
		ISRMQ = False
		return (dic,1)
	newDic = removeLowerLevel(dic,keys)
	newKeys= sorted(newDic.keys())
	if q == qn:
		if len(newKeys) !=q/2:
			ISRMQ = False
			return (newDic,1)
		for i in range(len(newKeys)):
			RMQ[q-1 + i *2] = newKeys[i]
			keyVisted.append(newKeys[i])
		keyVisted = set(keyVisted)
		keys2 = filter(lambda x: x not in keyVisted, keys)
		for i in range(len(newKeys)):
			RMQ[q-1 + i *2 +1] =keys2[i]
	else:
		for i in range(len(keys)):
			t=q-1+i
			RMQ[t]= min(RMQ[t*2+1],RMQ[t*2+2])
	return (newDic,q/2)

def getMaxKey(dic):
	mx = 0
	keys=[]
	for k,v in dic.items():
		if dic[k]> mx:
			mx = dic[k]
	for k,v in dic.items():
		if dic[k] == mx:
			keys.append(k)
	return sorted(keys)

def formLowerLevel2(dic,q):
	global RMQ,ISRMQ,qn
	keys = dic.keys()
	if len(keys) !=q:
		ISRMQ = False
		return 
	n=0
	levelStart=0
	while len(getMaxKey(dic))!=0:
		n2 = len(getMaxKey(dic))
		maxKey = getMaxKey(dic)
		if n == 0:
			for k1 in maxKey:
				RMQ [n]=k1
				n = n +1

			levelStart = 0
		else:
			keyVisted =[]
			for i in range(n2/2):
				idex1=levelStart + i*2 +1
				RMQ[idex1] = RMQ[idex1/2]
				keyVisted.append(RMQ[idex1/2])
			keyVisted = set(keyVisted)
			keys2 = filter(lambda x: x not in keyVisted, maxKey)
			keys2 = sorted(keys2)
			dicVisted={}
			for i in range(n2/2):

				j=0
				idex1=levelStart + i*2 +1
				# print keys2, idex1
				# print RMQ
				while keys2[j] < RMQ[idex1] :
					print keys2[j] ,RMQ[idex1]
					j=j+1

				RMQ[idex1 +1] = keys2[j]
				dicVisted[keys2[j]]=0
				#del keys2[j]
			levelStart =levelStart + n2
		dic = removeLowerLevel(dic,maxKey)


newDic = dic

formLowerLevel2(newDic,q)

if ISRMQ == True:
	for i in range(qn-1):
		mx = min(RMQ[i],RMQ[i*2+1],RMQ[i*2+2])
		if mx !=RMQ[i]:
			ISRMQ = False
			print RMQ[i],RMQ[i*2+1],RMQ[i*2+2]
	



if ISRMQ == False:
	print "NO"
else:
	print "YES"
	re= map(str,RMQ)
	print " ".join(re)





