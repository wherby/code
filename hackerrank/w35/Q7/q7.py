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

def leftOrRight(ordlst, dic1,d ,index):
	leftIndex = index -1
	rightIndex = index 
	leftValue = ordlst[leftIndex]
	rightValue = ordlst[rightIndex]
	leftWeight = dic1[leftValue]
	righWeight = dic1[rightValue]
	dis = rightValue -leftValue
	cost = 0
	n = len(ordlst)
	while dis < d and cost <d:
		if leftWeight <= righWeight:
			#move left
			#print "move left" + str(dis)
			if leftIndex == 0:
				#move max
				cost = (d - dis) * leftWeight + cost
				dis = d
			else:
				#print "LEft:::;"
				#print leftIndex,index
				mvLenth = leftValue - ordlst[leftIndex -1]
				if mvLenth < d -dis:
					dis = dis + leftIndex - ordlst[leftIndex -1]
					cost = cost + (leftIndex - ordlst[leftIndex -1]) * leftWeight
					leftWeight = leftWeight + dic1[ordlst[leftIndex -1]]
					leftIndex = leftIndex -1
				else:
					cost = cost +(d -dis) * leftWeight
					dis = d
		else:
			#move Right
			if rightIndex == n-1:
				cost =cost + (d -dis) * righWeight
				dis = d
			else:
				mvLenth = ordlst[rightIndex +1] - ordlst[rightIndex]
				if mvLenth < d -dis:
					dis = dis + ordlst[rightIndex + 1] -rightIndex
					cost = cost + (ordlst[rightIndex + 1] -rightIndex) * righWeight
					righWeight = righWeight + dic1[ordlst[rightIndex +1]]
					rightIndex = rightIndex +1
				else:
					cost = cost +(d -dis) * righWeight
					dis =d
	#print "COST:::"
	#print cost,dis,ordlst,dic1,index
	return cost

def getMin(ordlst,dic1,d, va):
	global MinLst
	if len(dic1) == 1:
		for k,v in dic1.items():
			if v == 1:
				return 0	
	if len(ordlst) == 1:
		return d
 	n = len(ordlst)
 	mx = d
 	if n <=20:
	 	for i in range(1,n):
	 		cost = leftOrRight(ordlst, dic1,d ,i)
	 		if n == 20:
	 			MinLst[ordlst[i]] =cost
	 		if cost < mx:
	 			mx = cost
	else:
		leftIndex = bisect.bisect_left(ordlst, va-d)
		rightIndex = bisect.bisect_right(ordlst, va +d)
		#print leftIndex,rightIndex
		if leftIndex == 0:
			leftIndex =1
		for i in range(leftIndex,rightIndex):
	 		cost = leftOrRight(ordlst, dic1,d ,i)
	 		MinLst[ordlst[i]] =cost
	 	for key,value in MinLst.items():
	 		if mx > value:
	 			mx = value
 	return mx
 		

		


def BruteCom(ls,d):
	dic1 ={}
	re =[]
	ordlst =[]

	for i in ls:
		if i not in dic1:
			dic1[i] =1
			bisect.insort_left(ordlst,i)
		else:
			dic1[i] = dic1[i] +1
		r1 =getMin(ordlst,dic1,d,i)
		re.append(r1)
	return re


q, = map(int , ins[0].strip().split())
index=1
MinLst = {}
for i in range(q):
	n,d= map(int , ins[index+i*2].strip().split())
	ls= map(int , ins[index+i*2+1].strip().split())
	re =BruteCom(ls,d)
	re =map(str,re)
	res = " ".join(re)
	print res