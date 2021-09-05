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

Map1=[]
cn=0
for i in range(9):
	for j in range(i+1,9):
		t1 = [0]*12
		t1[i]=1
		t1[j]=1
		if i <3 and j <3:
			t1[9]=1
			t1[10]=1
			t1=map(str,t1)
			t2="".join(t1)
			Map1.append(t2)
			t1[9]=0
			t1[10]=1
			t1[11]=1
			t1=map(int,t1)
			t1=map(str,t1)
			t2="".join(t1)
			Map1.append(t2)
			t1[9]=1
			t1[10]=0
			t1[11]=1
			t1=map(int,t1)
			t1=map(str,t1)
			t2="".join(t1)
			Map1.append(t2)
		if i >5 and j >5:
			t1=map(str,t1)
			t2="".join(t1)
			Map1.append(t2)
		if (i <3 and j > 3) or (i>3 and j <3):
			t1[9]=1
			t1=map(str,t1)
			t2="".join(t1)
			Map1.append(t2)
			t1=map(int,t1)
			
			t1[9]=0
			t1[10]=1
			t1=map(str,t1)
			t2="".join(t1)
			Map1.append(t2)
			t1=map(int,t1)
			t1[10]=0
			t1[11]=1
			t1=map(str,t1)
			t2="".join(t1)
			Map1.append(t2)
print len(Map1)

# print Map1
trans={}
Rtrans={}
for i in Map1:
	stat= i[:6]
	tras1=i[3:9]
	stat2 = i[::3] +i[1::3]
	tras2 = i[1::3] +i[2::3]
	if stat not in trans:
		trans[stat] = [tras1]
	else:
		trans[stat].append(tras1)
	if stat2 not in Rtrans:
		Rtrans[stat2] =[tras2]
	else:
		Rtrans[stat2].append(tras2)




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
		dic2 =tdic
		m = m -1
	while n!=0:
		tdic={}
		for k,v in dic3.items():
			trlist=Rtrans[k]
			for tr in trlist:
				if tr not in tdic:
					tdic[tr] = v 
				else:
					tdic[tr] = v + tdic[tr]
		dic3 =tdic
		n = n -1
	# print dic2
	rs=0
	for k,v in dic2.items():
		rs = rs +v
	rs1=0
	for k,v in dic3.items():
		rs1 = rs1 +v
	return rs *rs1





q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	m,n= map(int , ins[index+i].strip().split())
	dic2={}
	re =[]
	for x in Map1:
		dic2={x[3:]:1}
		dic3={x[1::3] +x[2::3] :1}
		t1= getNum(m-3,n-3,dic2,dic2)
		re.append(t1)
	print sum(re)