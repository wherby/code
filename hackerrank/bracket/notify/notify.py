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

dic1={}
for i in range(202):
	dic1[i] =0

def addToDic(n):
	global dic1
	if n in dic1:
		dic1[n] = dic1[n] +1
	else:
		dic1[n] =1

def removeDic(n):
	global dic1
	dic1[n] = dic1[n] -1



def findMid(st,ed):
	global ls,dic1
	if st !=0:
		removeDic(ls[st-1])
		addToDic(ls[ed-1])
	m = ed -st
	c =0
	fdS=0
	if m %2 ==0:
		fdS =m/2
	else:
		fdS =m/2 +1

	for i in range(201):
		c = c + dic1[i]
		if c >=fdS:
			if m%2!=0:
				return i *2
			else:
				a1=i
				if c < fdS +1:
					while c <fdS +1:
						i = i +1
						c =c +dic1[i]
					return a1+i
				else:
					return i*2


def isGreat(st,ed):
	global ls
	v1=ls[ed]
	v2 = findMid(st,ed)
	if v1 >=v2:
		return v1
	else:
		return 0

q,m = map(int , ins[0].strip().split())
ls= map(int , ins[1].strip().split())
re =[]

for i in range(m):
	addToDic(ls[i])
for i in range(q-m):
	t = isGreat(i,i+m)
	re.append(t)
re =filter(lambda x: x >0,re )
print len(re)
