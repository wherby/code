filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin
CONSTPRIME = 1000000007


ins=[]
for line in inputA:
    ins.append(line)

fibList=[]
fibList.append(1)
fibList.append(1)
dic1={1:1,2:1,0:0}
def getFib(n):
	global dic1,CONSTPRIME
	CONST1 = 1000000000
	if n not in dic1:
		if n%2 ==0:
			x1 = n/2
			re = (getFib(x1) *(2* getFib(x1+1) -getFib(x1))) %CONSTPRIME
			if n < CONST1:
				dic1[n] =re
			return re
		else:
			x1 = n/2
			x2 =n-x1
			re = (getFib(x1)**2 + getFib(x2)**2)  %CONSTPRIME
			if n < CONST1:
				dic1[n] = re 
			return re
	else:
		return dic1[n]



# def getRange(i,j):
# 	re= j*(j+1)/2 - i * (i-1)/2
# 	return re

def genLSS(ls):
	#ls = sorted(ls)
	global CONSTPRIME
	CONSTPRIME2= CONSTPRIME *2 +2
	n =len(ls)
	pars=[]
	tp=[]
	t1=0
	for i in range(n):
		t1=t1+ls[i]
		tp.append(t1)
	tp1=[0]+tp[0:n-1]
	sm =0
	for i in range(n):
		for j in range(i+1):
			t1 = (tp[i] - tp1[j] +CONSTPRIME2) %CONSTPRIME2
			sm = (sm + getFib(t1))%CONSTPRIME
			#pars.append((tp[i] - tp1[j] +CONSTPRIME2) %CONSTPRIME2)
	return sm

def genLSS2(ls):
	#ls = sorted(ls)
	global CONSTPRIME
	CONSTPRIME2= CONSTPRIME *2 +2
	n =len(ls)
	pars=[]
	tp=[]
	t1=0
	for i in range(n):
		t1=t1+ls[i]
		tp.append(t1)
	tp1=[0]+tp[0:n-1]
	sm =0
	for i in range(n):
		for j in range(i+1):
			t1 = (tp[i] - tp1[j] +CONSTPRIME2) %CONSTPRIME2
			#sm = (sm + getFib(t1))%CONSTPRIME
			#pars.append((tp[i] - tp1[j] +CONSTPRIME2) %CONSTPRIME2)
	return pars

q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index+i*2].strip().split())
	ls= map(int , ins[index+i*2+1].strip().split())
	re= genLSS(ls)
	
	print re
# print getFib(CONSTPRIME)
# print getFib(CONSTPRIME +1)
# print getFib(CONSTPRIME*2 +2)
# print getFib(CONSTPRIME*2 +3)
# print getFib(CONSTPRIME*2 +4)
# print getFib(CONSTPRIME*2 +5)
# print getFib((CONSTPRIME +1))
# a = CONSTPRIME*2 +2

# for i in range(2,20000000):
# 	a1= a/i
# 	b= getFib(i)
# 	if b == 0: 
# 		print "find: " + str(i)
# print len (dic1)

