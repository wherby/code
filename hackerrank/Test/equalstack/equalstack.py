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

n1,n2,n3 = map(int , ins[0].strip().split())
index=1
dic={}
for i in range(3):
	lt= map(int , ins[index+i].strip().split())
	lt.reverse()
	st=0
	nt=len(lt)
	for i in range(nt):
		st=st + lt[i]
		sts=st
		if sts in dic:
			dic[sts]=dic[sts]+1
		else:
			dic[sts]=1
mx=0
for (key,value) in dic.items():
	if value==3:
		if key>mx:
			mx=key
print mx

#https://www.hackerrank.com/challenges/equal-stacks


