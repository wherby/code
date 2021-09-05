filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import copy

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin

def PowerSum(k,n):
	global CONSTPRIME
	n = n%CONSTPRIME
	if k ==0:
		return n
	if k ==1:
		return n*(n+1)/2 
	if k ==2:
		return n*(n+1)*(2*n+1)/6
	if k==3:
		return n**2 *(n+1)**2 /4
	if k ==4:
		return n *(n+1) *(2*n +1) *(3*n**2 +3*n -1) /30
	if k ==5:
		return  n**2 * (n+1)**2 *(2*n**2+2*n -1) /12
	if k ==6:
		return n*(n+1) *(2*n +1) *(3*n**4 + 6*n**3 - 3*n +1) /42
	if k ==7:
		return n**2*(n+1)**2 *(3*n**4+6*n**3 -n**2-4*n +2) /24
	if k ==8:
		return n *(n+1) *(2*n +1)*(5*n**6 + 15*n**5+5*n**4 -15*n**3 -n**2 +9 *n -3) /90
	if k==9:
		return n**2 * (n+1)**2 *(n**2 + n -1) *(2*n**4 +4*n**3 -n**2 -3*n +3) /20
	if k ==10:
		return n*(n+1)*(2*n +1) *(n**2 +n -1) *(3 * n**6 +9*n**5 +2*n**4 -11*n**3+3*n**2+10*n-5)/66


ins=[]
for line in inputA:
    ins.append(line)


CONSTPRIME = 1000000007

def multALl(pl,n):
	
	return pl *n


def getLeveUpCombine(pl):
	global ls,dic1,ed
	re=[]
	minX= ed
	tp =set(pl[0])
	for i in ls:
		if i not in tp:
			t1 = multALl(pl[1],i)
			if t1<minX:
				minX=t1
			if t1 not in dic1 and t1 <=ed:
				t2=pl[0][:]+[i]
				re.append([t2,t1])
				dic1[t1] =1
	return (re,minX)

def getValue(pl,n):
	global expon,ed,CONSTPRIME
	res=0
	for i2 in pl:
		i = multALl(i2[1],1)
		ed1 = ed /i
		v1 =PowerSum(expon,ed1) * i**expon % CONSTPRIME
		res =res +v1
	if n >1:
		if n %2 ==0:
			res =res * (-1)
		else:
			res = res 
	return res %CONSTPRIME


def getAllCombine(pl):
	global ls,dic1,ed
	n = len(ls)
	rex=0
	for i in range(n):
		re =[]
		minxLeve=ed +1
		for p1 in pl:
			re1,minX =getLeveUpCombine(p1)
			if minxLeve >minX:
				minxLeve = minX
			if minX > ed:
				continue
			re.extend(re1)
		if minxLeve > ed:
			break
		#print re
		pl = re
		v1 =getValue(pl,i+1)
		rex =rex +v1
		#print v1
	return rex




q, = map(int , ins[0].strip().split())
index=1

for i in range(q):
	dic1={}
	n,expon,ed= map(int , ins[index+i*2].strip().split())
	mx1= PowerSum(expon,ed) %CONSTPRIME
	#print mx1
	ls= map(int , ins[index+i*2 +1].strip().split())
	a1=getAllCombine([[[],1]])  %CONSTPRIME
	print (mx1- a1 + CONSTPRIME)% CONSTPRIME

