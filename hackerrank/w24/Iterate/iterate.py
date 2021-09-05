filename = "input/input01.txt"
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

def gcd(a, b):
 if a < b:
  a, b = b, a
 while b != 0:
  temp = a % b
  a = b
  b = temp
 return a


def step(ls):
	nls =set(ls)
	nls =sorted(nls)
	
	m =len(nls)
	if m ==1:
		return False
	re=set()
	for i in range(m):
		for j in range(i+1,m):
			re = re | set([abs(nls[i] -nls[j])])
	re =sorted(re)
	m =len(re)
	g1=nls[0]
	for i in range(m):
		g1= gcd(g1,re[i])
		if g1 == 1:
			break
	if g1 !=1:
		for i in range(m):
			re[i] = re[i] / g1
	print re
	return re


# def step2(ls):
# 	nls =set(ls)
# 	nls =sorted(nls)

# 	g1=nls[0]
# 	m =len(nls)
# 	re=set()
# 	if m >300000:
# 		knls=nls[:10] + nls[-10:]
# 		m2= len(knls)
# 		for i in range(m2):
# 			for j in range(i+1,m2):
# 				re = re +set(abs(knls[i] -knls[j]))
# 	if m ==1:
# 		return False
	
# 	for i in range(m-1):
# 		re.append(abs(nls[i] - nls[i+1]))
	
# 	return set(re)

def getStep(ls):
	c=0
	nls =set(ls)
	nls =sorted(nls)
	m =len(nls)
	g1=nls[0]
	for i in range(m):
		g1= gcd(g1,nls[i])
		if g1 == 1:
			break
	if g1 !=1:
		for i in range(m):
			nls[i] = nls[i] / g1
	for i in range(m-1,0,-1):
		if nls[i] - nls[i-1] ==1:
			return nls[m-1] -nls[0] +1
	if nls[0]==1 and  nls[m-1] -nls[m-2] ==1:
			return nls[m-1] +c
	while len(step(ls)) !=1:
		ls =step(ls)
		c = c +1
		nls =sorted(ls)
		m =len(nls)
		for i in range(m-1,0,-1):
			if nls[i] - nls[i-1] ==1:
				return nls[m-1] -nls[0] +1 +c
	return c +2

q, = map(int , ins[0].strip().split())

ls= map(int , ins[1].strip().split())
c =0
print getStep(ls)
