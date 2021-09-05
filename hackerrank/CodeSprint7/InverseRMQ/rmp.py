filename = "input/input02.txt"
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
if qn > 10000000:
	ISRMQ = False

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
	global RMQ,ISRMQ
	keys = dic.keys()
	keys = sorted(keys)
	if len(keys) !=q:
		ISRMQ = False
		return (dic,1)
	newDic = removeLowerLevel(dic,keys)
	newKeys= sorted(newDic.keys())
	if len(newKeys) !=q/2:
		ISRMQ = False
		return (newDic,1)
	for i in range(len(newKeys)):
		RMQ[q-1 + i *2] = newKeys[i]
		keys.remove(newKeys[i])
	for i in range(len(newKeys)):
		RMQ[q-1 + i *2 +1] =keys[i]
	return (newDic,q/2)

newDic = dic
newDic,q =formLowerLevel(newDic,q)
while q > 1 and ISRMQ == True:
	newDic,q =formLowerLevel(newDic,q)
RMQ[0] = newDic.keys()[0]
if ISRMQ == True:
	for i in range(qn-1):
		mx = min(RMQ[i],RMQ[i*2+1],RMQ[i*2+2])
		if mx !=RMQ[i]:
			ISRMQ = False
	



if ISRMQ == False:
	print "NO"
else:
	print "YES"
	re= map(str,RMQ)
	print " ".join(re)



