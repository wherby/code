filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import bisect 

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)




def indexForLS(ls,indexLs):
	n = len(ls)
	for i in range(n):
		indexLs.append([])
	for i in range(n):
		t = ls[i]
		indexLs[t].append(i)




def removeDic(dic,x):
	global dicfd,preX
	v=dic[x]
	del dicfd[v][x/1000][x]
	if v-1 != 0:
		dicfd[v-1][x/1000][x] =1
	# if v != 0:
	# 	del dicfd[v][bisect.bisect_left(dicfd[v], x)] 
	# bisect.insort(dicfd[v-1], x)
	#print dic,x
	dic[x] = dic[x] -1
	if dic[x] == 0:
		del dic[x]

	#print dic

def addDic(dic,x):
	global dicfd,preX
	#print dic
	if x not in dic:
		dic[x] =1
	else:
		dic[x] = dic[x] +1
	#if dic[x] == preX:
		#bisect.insort(dicfd, x)
		#pass
	v = dic[x]
	#print x
	dicfd[v][x/1000][x] = 1
	if v-1 != 0:
		del dicfd[v-1][x/1000][x]
	# bisect.insort(dicfd[v], x)
	# if v-1 != 0:
	# 	del dicfd[v-1][bisect.bisect_left(dicfd[v-1], x)] 

def findMin(dicfdFind):
	global n
	for i in range(100):
		if len(dicfdFind[i]) != 0:
			return min(dicfdFind[i])
			break
	return -1



def queryls2(ls,l,r,x):
	global ll,rl,dic
	if ll == -1:
		ll =l
		rl = r
		for i in range(l,r+1):
			addDic(dic,ls[i])
	if l >ll:
		for i in range(ll,l):
			#print ll,l
			removeDic(dic,ls[i])
	else:
		for i in range(l,ll):
			addDic(dic,ls[i])
	if r > rl:
		for i in range(rl+1,r+1):
			addDic(dic,ls[i])
	else:
		for i in range(r+1,rl+1):
			removeDic(dic,ls[i])

	if len(dicfd[x])== 0:
		return -1
	else:
		return findMin(dicfd[x])#min(dicfd[x])
	return 1

def cmpQ(i,j):
	global  queryLS
	if queryLS[i][0] > queryLS[j][0]:
		return -1
	elif queryLS[i][0] < queryLS[j][0]:
		return 1
	elif queryLS[i][0] == queryLS [j][0]:
		if queryLS[i][1] > queryLS[j][1]:
			return -1
		else:
			return 1

q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	indexLs=[]
	ls= map(int , ins[index+1].strip().split())
	indexForLS(ls,indexLs)
	#print lsp
	qn,=map(int , ins[index+2].strip().split())

	dic = {}
	ll=-1
	rl=-1
	#print "XXXXXXX"
	queryLS=[]
	qord=[]
	dicfd=[]
	n= len(ls)
	for i in range(n):
		dicfd.append([])
		for j in range(100):
			dicfd[i].append({})
	#print dicfd[0]
	re=[0] *qn
	for j in range(qn):
		l,r,x =map(int , ins[index+3+j].strip().split())
		queryLS.append([l,r,x])
		qord.append(j)
	qord= sorted(qord,cmp = lambda x,y: cmpQ(x,y))
	preX=-1
	for j in range(qn):
		t = qord[j]
		#print t
		l,r,x = queryLS[t]
		# if x != preX:
		# 	dic={}
		# 	ll = -1
		# 	rl = -1
		# 	dicfd=[]
		# 	prex  = x
		#print "l R Pair: " + str(l) + " , " +str(r)
		req=queryls2(ls,l,r,x)
		#print req
		re[t] = req
		ll =l
		rl =r
		#print l,r,x
	#print "YYYYYYYYYYYYYYYYYYY"
	for x in re:
		#pass
		print x
	index = index + 3 +qn