filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
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


n,= map(int , ins[0].strip().split())
lsb = []
for i in range(n):
	lsb.append([])

ls1 = map(int , ins[1].strip().split())
ls = map(int , ins[2].strip().split())
k = len(ls1)
for i in range(k):
	lsb[i+1].append(ls1[i]-1)
	lsb[ls1[i]-1].append(i+1)

pairdic = {}
for i in range(n):
	t =ls[i]
	if t not in pairdic:
		pairdic[t] = [i]
	else:
		pairdic[t].append(i)
matchls = [0] *n
for key,value in pairdic.items():
	a,b = value
	matchls[a] =b
	matchls[b] =a
#print matchls

def getNext(ls):
	global lsb,matchls
	dic1 ={}
	for i in ls:
		dic1[i] = 1
	plist = ls
	tp = plist[-1]
	ps =lsb[tp]
	re = []
	for p1 in ps:
		if p1 not in dic1 and matchls[p1] not in dic1:
			tp = list(ls)
			tp.append(p1)
			re.append(tp)
	#print re
	return re





def getAllpathFromI(i):
	global lsb
	ls =[i]
	re = []
	re.append(ls)
	next = getNext(ls)
	re.extend(next)
	while len(next)!= 0:
		nextre = []
		for x in next:
			tnext = getNext(x)
			nextre.extend(tnext)
		next = nextre
		re.extend(next)
	#print "RREE"
	#print re
	return re

getAllpathFromI(0)

allLen =0
for i in range(n):
	re1 = getAllpathFromI(i)
	#print re1
	allLen =allLen + len(re1)

print allLen
