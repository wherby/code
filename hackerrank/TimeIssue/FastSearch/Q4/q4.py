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


#print ins

d1={}

n,m = map(int , ins[0].strip().split())
index=1
ls=[]
lsPick=[]
lsNotPick=[]
for i in range(m):
	a,b,c,d,= map(int , ins[index+i].strip().split())
	tls=[min(a,b),max(a,b),c,d]
	ls.append(tls)

def comp(ls1,ls2):
	#print (float(ls1[2])/ls1[3]) ,(float(ls2[2])/ls2[3])
	if (float(ls1[2])/ls1[3]) < (float(ls2[2])/ls2[3]):
		return 1
	else:
		return -1

ls = sorted(ls,cmp= lambda x,y: comp(x,y))

for i in range(m):
	tls= ls[i]
	if tls[0] == tls[1]:
		continue
	if tls[0] not in d1 or tls[1] not in d1:
		lsPick.append(tls)
		if tls[0] not in d1:
			d1[tls[0]] =1
		if tls[1] not in d1:
			d1[tls[1]]=1
	else:
		lsNotPick.append(tls)

def addKeys(dic2,key, tls):
	if key not in dic2:
		dic2[key]=[tls]
	else:
		dic2[key].append(tls)

def dfsTreeSearch(start,end,dicAdj):
	stack = [(start,[start])]
	visited =set()
	while stack:
		(vertex,path) = stack.pop()
		if vertex not in visited:
			if vertex == end:
				return path
			visited.add(vertex)
			for neighbor in dicAdj[vertex]:
				stack.append((neighbor,path+[neighbor]))





def addToAdjDic(dicAdj, p1,p2):
	if p1 in dicAdj:
		dicAdj[p1].append(p2)
	else:
		dicAdj[p1] = [p2]
	if p2 in dicAdj:
		dicAdj[p2].append(p1)
	else:
		dicAdj[p2] = [p1]
	return dicAdj

def findAffected(tlsReplace):
	global lsPick
	dicA = {}
	for tls in lsPick:
		a1 = (tls[0],tls[1])
		dicA[a1] = tls
	dicAdj={}
	start = tlsReplace[0]
	end = tlsReplace[1]
	for tls in lsPick:
		p1 = tls[0]
		p2 = tls[1]
		dicAdj = addToAdjDic(dicAdj,p1,p2)
	route = dfsTreeSearch(start,end,dicAdj)
	m = len(route)
	routes =[]
	for i in range(1,m):
		b1 = (min(route[i-1], route[i]),max(route[i-1], route[i]))
		routes.append(dicA[b1])
	#print routes
	return routes


def tryLs(tlsReplace):
	global lsNotPick,lsPick
	isChange= False
	affectLs = []
	lsStack=[tlsReplace[0],tlsReplace[1]]
	dic2={}
	visited={}
	# for tls in lsPick:
	# 	addKeys(dic2,tls[0],tls)
	# 	addKeys(dic2,tls[1],tls)
	# while len(lsStack) != 0:
	# 	t1 = lsStack.pop(0)
	# 	if t1 not in visited:
	# 		a1 = dic2[t1]
	# 		affectLs.extend(a1)
	# 		visited[t1] =1
	# 		for ttls in a1:
	# 			if ttls[0] not in visited:
	# 				lsStack.append(ttls[0])
	# 			if ttls[1] not in visited:
	# 				lsStack.append(ttls[1])
	
	affectLs = findAffected(tlsReplace)
	num1 = sum(map(lambda a: a[2],lsPick))
	num2 = sum(map(lambda a: a[3],lsPick))
	d1 = float(num1) /num2

	dicAff = {}
	choose =[]
	for tls in affectLs:
		tnum1 = num1 - tls[2] + tlsReplace[2]
		tnum2 = num2 - tls[3] + tlsReplace[3]
		if d1 < float(tnum1)/tnum2:
			isChange =True
			choose = tls
			d1= float(tnum1)/tnum2

	if isChange == True:
		lsPick.remove(choose)	
		lsPick.append(tlsReplace)
		lsNotPick.append(choose)
		lsNotPick.remove(tlsReplace)
	return isChange





#print ls

def printRs(lsPick):
	num1=0
	num2=0
	for tls in lsPick:
		num1 = tls[2] + num1
		num2 = tls[3] + num2
	reStr = str(num1) + "/" + str(num2)
	print reStr
#print lsPick,lsNotPick
isChange = True
while isChange != False:
	for tls  in lsNotPick:
		isChange = tryLs(tls)
		if isChange == True:
			break
	pass



printRs(lsPick)
#print lsPick,lsNotPick

	
