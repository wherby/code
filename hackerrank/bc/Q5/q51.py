filename = "input/input00.txt"
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


def getNextDFS(ls,dic1,dic2):
	global lsb,matchls

	plist = ls
	tp = plist[-1]
	ps =lsb[tp]
	re = []
	#print ps,ls
	for p1 in ps:
		#print p1
		if p1 not in dic2 and matchls[p1] not in dic1:
			tp = list(ls)
			tp.append(p1)
			dic1[p1] =1
			dic2[p1] =1
			#re.append(tp)
			#print dic1
			return (tp,dic1,dic2)
	del dic1[tp]
	if len(plist) == 1 :
		#print "CCCC"
		#print plist
		return (re,{},dic2)
	else:
		return (re,dic1,dic2)
	return (re,dic1,dic2)


def getAllpathFromIDFS(i):
	global lsb
	ls =[i]
	dic1 ={i:1}
	dic2 ={i:1}
	re = []
	re.append(ls)
	next,dic1,dic2 = getNextDFS(ls,dic1,dic2)
	#print next,dic1
	if next not in re and len(next) !=0:
		re.append(next)
	while len(next)!= 0:
		nextre = []
		tnext,dic1,dic2 = getNextDFS(next,dic1,dic2)
		if len(tnext) == 0:
			next = next[:len(next)-1]
		else:
			next = tnext
		#print tnext,dic1
		if next not in re and len(next) !=0:
			re.append(next)
		if len(dic1) == 0  :
			#print "XXX"
			#print dic1,next
			break		
	#print "RREE"
	#print re,dic1
	return re

getAllpathFromIDFS(1)



allLen =0
for i in range(n):
	re1 = getAllpathFromIDFS(i)
	#print re1
	allLen =allLen + len(re1)

print allLen
