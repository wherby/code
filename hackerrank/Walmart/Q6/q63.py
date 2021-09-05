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
CONSTDIC = 100000
dicCONS = [0]* (CONSTDIC+2)
dicCONS[0]=-1
dicCONS[1]=1
dicCONS[2]=1

for i in range(3,CONSTDIC+1):
	a = dicCONS[i-1] + dicCONS[i-2]
	dicCONS[i] = a %CONSTPRIME

ins=[]
for line in inputA:
    ins.append(line)

fibList=[]
fibList.append(1)
fibList.append(1)
dic1={1:1,2:1,0:0}
def getFib(n):
	global dic1,CONSTPRIME,CONSTDIC,dicCONS
	if n> CONSTDIC and n not in dic1:
		if n%2 ==0:
			x1 = n/2
			re = (getFib(x1) *(2* getFib(x1+1) -getFib(x1))) %CONSTPRIME
			dic1[n] =re
			return re
		else:
			x1 = n/2
			x2 =n-x1
			re = (getFib(x1)**2 + getFib(x2)**2)  %CONSTPRIME
			dic1[n] = re 
			return re
	elif n <=CONSTDIC:
		return dicCONS[n]
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
			print t1
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
			pars.append((tp[i] - tp1[j] +CONSTPRIME2) %CONSTPRIME2)
	return pars

def genLSS3(ls):
	#ls = sorted(ls)
	global CONSTPRIME
	CONSTPRIME2= CONSTPRIME *2 +2
	n =len(ls)
	pars=[]
	dic2 = {}
	tp=[0]*10001
	tp1=[0]*10001
	t1=0
	for i in range(n):
		t1=t1+ls[i]
		t1=t1 %CONSTPRIME2
		tp[i]=t1
		tp1[i+1] = t1 
	sm =0
	for i in range(n):
		tpi=tp[i]
		for j in range(i+1):
			t1 = (tpi - tp1[j] ) %CONSTPRIME2
	# 		if t1 not in dic2:
	# 			dic2[t1] = 1
	# 		else:
	# 			dic2[t1] = dic2[t1] +1
	# keys= dic2.keys()
	# for key in keys:
	# 	n = dic2[key]
	# 	sm =( sm + n * getFib(key))%CONSTPRIME
			#sm = (sm + getFib(t1))%CONSTPRIME
			#pars.append((tp[i] - tp1[j] +CONSTPRIME2) %CONSTPRIME2)
	return sm

q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index+i*2].strip().split())
	ls= map(int , ins[index+i*2+1].strip().split())
	re= genLSS3(ls)
	
	print re

ls1 = range(300000000,300001000)
print genLSS3(ls1)

# ls = range(4000000,5000000)
# for i in ls:
# 	x1 = getFib(i)
# 	if i == 0:
# 		print "find " +str(i)
