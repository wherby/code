filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w25/challenges/stone-division/editorial


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



dic1={}

# Grundy's theorem and the fact that nimsum #
def getANS(ls,n):
	global dic1
	if n in dic1:
		return dic1[n]
	re = False
	dic1[n] =False
	for i in ls:
		if n%i !=0:
			continue
		elif i%2 ==0:
			re =True
			dic1[n]=re
		elif not getANS(ls,n/i):
			re = True
			dic1[n]=re
	
	return re


n,m = map(int , ins[0].strip().split())
index=1

ls= map(int , ins[1].strip().split())
re = getANS(ls,n)
if re == True :
	print "First"
else:
	print "Second"

