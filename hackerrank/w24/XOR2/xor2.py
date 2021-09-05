filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w24/challenges/xor-matrix
# help Link http://www.zybang.com/question/8f777b7981f599cdf086996723d7c49c.html 
# 

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



p1 =[0]
def getAllIndex(m,p1):
	global n
	d=1
	while m !=0:
		d=1
		while d*2 <=m:
			d = d *2
		p2 = map(lambda x: [x,x+d],p1)
		r1=[]
		for p3 in p2:
			r1.extend(p3)
		# print r1
		z1=[0]*n
		for i in r1:
			t = i %n
			z1[t] = z1[t] +1
		r1=[]
		for i in range(n):
			t = z1[i]
			if t %2 !=0:
				r1.append(i) 

		p1 =r1
		m = m -d
	return p1

p1= getAllIndex(m, p1)
# print p1
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