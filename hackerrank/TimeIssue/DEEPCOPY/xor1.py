filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import copy

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)
n,m = map(int , ins[0].strip().split())
m=m-1
#m = m%n
index=1
ls = map(int , ins[1].strip().split())

P1= map(lambda  x : set([x]),range(n))
ls3 =copy.deepcopy(ls)


p1 =[0]
def getAllIndex(m,p1):
	global n,ls3
	d=1
	while m !=0:
		d=1
		#ls2=copy.deepcopy(ls3)
		while d*2 <=m:
			d = d *2
		ls2= ls3[d%n :] +ls3[:d%n]

		for i in range(n):
			ls3[i] =ls3[i] ^ ls2[i]
		# p2 = map(lambda x: [x,x+d],p1)
		# r1=[]
		# for p3 in p2:
		# 	r1.extend(p3)
		# # print r1
		# z1=[0]*n
		# for i in r1:
		# 	t = i %n
		# 	z1[t] = z1[t] +1
		# r1=[]
		# for i in range(n):
		# 	t = z1[i]
		# 	if t %2 !=0:
		# 		r1.append(i) 

		# p1 =r1
		m = m -d


getAllIndex(m, p1)
# print p1
re =[]

p1 =sorted(p1)

# def getRange(p1):
# 	ranList=[]
# 	start = 0
# 	i=0
# 	while i < len(p1):
# 		start = p1[i]
# 		j=i
# 		while  j < len(p1)-1 and p1[j+1] == p1[j] +1 :
# 			j = j+1
# 		end =  p1[j] +1
# 		i=j+1
# 		ranList.append((start,end))
# 	return ranList
# ranLen= getRange(p1)


def getC(p1,d, ls):
	global n
	rt=0 
	for i in p1:
		rt = rt ^ ls[(i +d)%n]
	return rt

def getNext(vold,ranLen,i):
	global ls,n
	for start,end in ranLen:
		vold = vold ^ ls[(start + i) %n] ^ ls[(end + i) % n]
	return vold

re=[]
# if len(ranLen) <500:
# 	start = getC(p1,0,ls)
# 	re =[start]
# 	for i in range(n-1):
# 		start = getNext(start,ranLen,i)
# 		re.append(start)
# 	# print len(ranLen)
# 	# print ranLen

# 	# for i in range(n):
# 	# 	re.append(getC(p1,i,ls))
# 	re =map(str,re)
# 	print " ".join(re)
# else:
# 	pass
re =map(str,ls3)
print " ".join(re)
