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



dic1={}
pl=[]
cl=[]

def verify(ls,cl):
	ls2 = sorted(ls)
	ls2 = ls2.reverse()
	re =[]
	for i in ls2:
		if t /i > 1 and t %i ==0 and t != cl:
			t =t/i


	
def analcl(ls,cl):
	ls2 = sorted(ls)
	ls2 = ls2.reverse()
	re = []
	t = cl


def search(ls,n,k):
	global pl,cl
	t =n
	re =[]
	for i in pl:
		while t / i > 0 and t %i ==0:
			re.append(i)
			t = t / i
	#print re
	if len(cl) ==0 and len(re) %2 ==1:
		return 1
	if len(cl) ==0 and len(re) %2 ==0:
		return 0
	if len(cl) > 1:
		return 1



def getANS(ls,n):
	for i in ls:
		if i %2==0 and n%i == 0:
			return 1
	if n ==1:
		return 0
	re =search(ls,n,1)
	return re

def getDic(ls,n):
	global dic1
	t1 =n
	for i in ls:
		t1=n
		c =0
		while t1 %i ==0:
			c = c+1
			t1 = t1/i
		dic1[i] =c
	return dic

dic2={}
def getPL(ls):
	global dic2,pl,cl
	for i in ls:
		p=[]
		for j in ls:
			if i/j >1 and i% j ==0:
				p.append(j)
		dic2[i]=p
	for k,v in dic2.items():
		if len(v) > 0:
			cl.append(k)
		else:
			pl.append(k)


n,m = map(int , ins[0].strip().split())
index=1

ls= map(int , ins[1].strip().split())
getPL(ls)
re = getANS(ls,n)
if re == 1 :
	print "First"
else:

	print "Second"

