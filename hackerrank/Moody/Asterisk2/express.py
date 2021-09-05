#https://www.hackerrank.com/contests/moodysuniversityhackathon/challenges/asterisk-expressions
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
VALID= True
def exponen(base,exponent):
	global CONST
	if base == 1:
		return 1
	result =1
	while exponent >0:
		if exponent &1:
			result=result *base %CONST
		exponent =exponent >>1
		base =base **2 %CONST
	return result


CONST = 1000000007
# def eval2(left,right,op):
# 	#print left,right,op
# 	#print len(left),len(right)
# 	if len(left) ==0:
# 		return -1
# 	if len(right) ==0 :
# 		return -1
# 	left = int(left)
# 	right = int(right)
# 	if op == "**":
# 		left=exponen(left,right)
# 	else:
# 		left =left * right %CONST
# 	return left


# def eval(exp):
# 	vlist = exp.split('*')
# 	n = len(vlist)
# 	left=vlist[0]
# 	i=0
# 	re=1
# 	op=""
# 	while i<n:
# 		if len(vlist[i]) ==0:
# 			if i ==0 or i == n-1:
# 				re=-1
# 			else:
# 				rt=eval2(vlist[i-1],vlist[i+1],"**")
# 				if rt == -1:
# 					re = -1
# 				x1=vlist[:i-1]
# 				y1=vlist[i+2:]
# 				x1.append(str(rt))
# 				x1.extend(y1) 
# 				vlist=x1
# 				n=n-2
# 		else:
# 			i=i+1
# 	n = len(vlist)
# 	i=1
# 	while i <n and re >0:
# 		if len(vlist[i]) >0:
# 			re=eval2(left,vlist[i],"*")
# 			left =str(re) 
# 			i = i +1
# 		else:
# 			re = eval2(left,vlist[i+1],"**")
# 			left =str(re) 
# 			i=i+2
# 	if re == -1:
# 		print "Syntax Error"
# 	else:
# 		print re % CONST

def getNumber(ls, i,n):
	global VALID
	if ls[i] == '*':
		VALID=False
	num=0
	while i < n and ls[i] != '*' :
		num = num *10 + int(ls[i])
		i = i +1
	return (num,i)

def spliter(ls):
	global VALID,CONST
	VALID = True
	i=0
	cls=[]
	n = len(ls)
	if ls[n-1] =='*':
		VALID= False
	state=0 
	(num,i) =getNumber(ls,i,n)
	cls.append(num)
	while i<n and VALID==True:
		if ls[i]== '*' and state ==0 :
			state =1
			i=i+1
		elif ls[i]=='*' and state ==1:
			left = cls.pop()
			i =i +1
			(num,i) =getNumber(ls,i,n)
			left =exponen(left,num)
			cls.append(left)
			state =0
		elif ls[i] != '*' and state ==1:
			(num,i)=getNumber(ls,i,n)
			cls.append(num)
			state =0
		else:
			VALID=False
	if VALID == True:
		sms=1
		m = len(cls)
		for i in range(m):
			sms= sms *cls[i]
		print sms %CONST
	else:
		print "Syntax Error"

q, = map(int , ins[0].strip().split())
index=1

for i in range(q):
	ls= ins[index+i].strip()
	spliter(ls)