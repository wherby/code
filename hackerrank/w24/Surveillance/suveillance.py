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

Map1=[]
cn=0
Map2=[]
for i in range(9):
	for j in range(i+1,9):
		t1 = [0]*9
		t1[i]=1
		t1[j]=1
		t1=map(str,t1)
		t2="".join(t1)
		Map1.append(t2)



def verifyde(t):
	a1 = [0,1,2,4,5,6,8,9,10]
	a2 = [4,5,6,8,9,10,12,13,14]
	a3 = [1,2,3,5,6,7,9,10,11]
	a4= [5,6,7,9,10,11,13,14,15]
	b1 =map(lambda y:map(lambda x: t[x],y),[a1,a2,a3,a4])
	b2 = map(lambda y: sum(y),b1)
	if b2[0] ==2 and b2[1] ==2 and b2[2] ==2 and b2[3] ==2:
		return True
	else:
		return False

for i in range(2**25):
	a1=[0]*25
	t1=i
	for j in range(25):
		a1[j]=t1%2
		t1=t1/2

	if verifyde(a1):
		t2=a1
		t2=map(str,t2)
		t2="".join(t2)
		Map2.append(t2)

MAP3=[]





print len(Map2)
# print Map1
trans={}
Rtrans={}
for i in Map1:
	stat= i[:6]
	tras1=i[3:]
	stat2 = i[::3] +i[1::3]
	tras2 =i[1::3] +i[2::3]
	if stat not in trans:
		trans[stat] = [tras1]
	else:
		trans[stat].append(tras1)
	if stat2 not in Rtrans:
		Rtrans[stat2] =[tras2]
	else:
		Rtrans[stat2].append(tras2)

RRTrans={}
print Rtrans
for i in Map2:
	x1=[0,4,8,12,1,5,9,13,2,6,10,14]
	x2=[1,5,9,13,2,6,10,14,3,7,11,15]
	statx1=map(lambda x: i[x],x1)
	statx1="".join(statx1)
	statx2=map(lambda x: i[x],x2)
	statx2="".join(statx2)
	if statx1 in RRTrans:
		RRTrans[statx1].append(statx2)
	else:
		RRTrans[statx1] =[statx2]



def getNum(m,n,dic2,dic3):
	global Map1,trans,Rtrans
	while m!=0:
		tdic={}
		for k,v in dic2.items():
			trlist=trans[k]
			for tr in trlist:
				if tr not in tdic:
					tdic[tr] = v 
				else:
					tdic[tr] = v + tdic[tr]
		# ttdic={}
		# for k,v in tdic.items():
		# 	k1=k[3:]
		# 	ttdic[k1] =v
		dic2 =tdic
		m = m -1
	# dic3 ={}
	# for k,v in tdic.items():
	# 	k1 =k[1::3] +k[2::3]
	# 	dic3[k1] =v
	while n!=0:
		tdic={}
		for k,v in dic3.items():
			trlist=RRTrans[k]
			for tr in trlist:
				if tr not in tdic:
					tdic[tr] = v 
				else:
					tdic[tr] = v + tdic[tr]
		dic3 =tdic
		n = n -1

	rs1=0
	rs2=0
	for k,v in dic2.items():
		rs2 = rs2 +v
	for k,v in dic3.items():
		rs1 = rs1 +v
	return rs1 *rs2





q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	m,n= map(int , ins[index+i].strip().split())
	dic2={}
	re =[]
	for x in Map2:
		m1=[8,9,10,12,13,14]
		m2=[2,6,10,3,7,11]
		xm1=map(lambda y:x[y],m1)
		xm2=map(lambda y:x[y],m2)
		xm1="".join(xm1)
		xm2="".join(xm2)
		x1=[0,4,8,12,1,5,9,13,2,6,10,14]
		statx1=map(lambda y: x[y],x1)
		statx1="".join(statx1)
		#print xm1,xm2
		dic2={xm1:1}
		dic3={statx1:1}
		t1= getNum(m-4,n-4,dic2,dic3)
		re.append(t1)
	#print re
	print sum(re)