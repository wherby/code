filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w24/challenges/xor-matrix

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
#m = m%n
index=1
ls = map(int , ins[1].strip().split())
P1= map(lambda  x : set([x]),range(n))

d =1 
while d*2 < m:
	d = d*2


def merge(l1):
	global n
	l2 = set( map(lambda x: (x +1) %n, l1) )
	l3 =l1 ^l2
	return l3

def getStr(se):
	a =copy.deepcopy(se)
	a=sorted(a)
	a=map(str,a)
	return " ".join(a)

p1 =set([0,d])
p1V = getStr(p1)


p1Set={p1V:1}
plList=[sorted(p1)]
num =1

redC= m
firstV=m
for i in range(m-1):
	p1 = merge(p1)
	num = num +1
	p1V = getStr(p1)


	if p1V not in p1Set:
		p1Set[p1V] =num
		plList.append(sorted(p1))
	else:
		redC = num - p1Set[p1V]
		p1Set[p1V] =num
		firstV = num
		break
	pass
m1 = (m -firstV)%redC

p1= plList[firstV-redC + m1 -1]


print p1
#print p1
re =[]

def getC(p1,d, ls):
	global n
	rt=0 
	for i in p1:
		rt = rt ^ ls[(i +d)%n]
	return rt
for i in range(n):
	re.append(getC(p1,i,ls))
re =map(str,re)
print " ".join(re)