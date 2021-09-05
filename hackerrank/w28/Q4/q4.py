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




def getValue(rl):
	dic1={}
	dicLst=[]
	for r1 in rl:
		a,b =r1
		if (a not in dic1) and (b not in dic1):
			dic1[a] = 1
			dic1[b] = 1
			dicTemp = {a:1,b:1}
			dicLst.append([dicTemp,2,1])
		elif (a not in dic1) and (b in dic1):
			dic1[a] =1 
			for dicT in dicLst:
				if b in dicT[0]:
					dicT[0][a]=1
					dicT[1] =dicT[1] +1
					dicT[2] =dicT[2] + 1
		elif (a in dic1) and (b not in dic1):
			dic1[b] =1
			for dicT in dicLst:
				if a in dicT[0]:
					dicT[0][b] =1
					dicT[1] = dicT[1] +1
					dicT[2] =dicT[2] + 1
		elif (a in dic1) and (b in dic1):
			for dicT in dicLst:
				if a in dicT[0]:
					tmpA = dicT
				if b in dicT[0]:
					tmpB = dicT
			if tmpA == tmpB:
				pass
			else:
				for key,value in tmpB[0]:
					tmpA[key] = value
				tmpA[1] = tmpA[1] + tmpB[1]
				dicLst.remove(tmpB)
			tmpA[2] =tmpA[2] + 1
	getMaXValue(dicLst)
	#print dicLst
	
def getMaXValue(dicLst):

	vlist=map(lambda x: [x[1],x[2]],dicLst)
	# mx = [0,0]
	# for v1 in vlist:
	# 	if v1 [0] > mx[0]:
	# 		mx[0] = v1[0]
	# 		mx[1] = v1[1]
	# 	if v1[0] == mx[0]:
	# 		if v1[1] > mx[1]:
	# 			mx[1] = v1[1]
	# vlist = filter(lambda x: not ( x[0] < mx[0] and x[1] < mx[1] ),vlist)
	#v2 = map(getValueM,vlist)
	getMaxListValue(vlist)
	#print sum(v2)



def getMaxListValue(vlist):
	a = sum (map(lambda x: x[0],vlist))
	b = sum(map (lambda x: x[1],vlist))
	n = len(vlist) + b -a
	c = map(lambda x: x[0],vlist)
	sorted(c).reverse()
	pk=0
	cnt = 0
	for i in c:
		
		for j in range(1,i):
			cnt = cnt  + (j) * (j+1) +pk
		pk = pk + i * (i-1)
	cnt = cnt + pk * n
	print cnt

def getValueM(vnode):
	m,n =vnode
	cnt =0 
	for i in range(1,m):
		cnt = cnt + (i) * (i+1)
	for j in range(m-1,n):
		cnt = cnt + m* (m -1)
	return cnt


q, = map(int , ins[0].strip().split())
index=1
for iq in range(q):
	n,m= map(int , ins[index].strip().split())
	rl=[]
	for j in range(m):
		a,b = map(int , ins[index + j +1].strip().split())
		rl.append([a,b])
	getValue(rl)
	index = index + m +1