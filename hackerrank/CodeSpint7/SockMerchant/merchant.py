#https://www.hackerrank.com/contests/world-codesprint-7/challenges/sock-merchant
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


q, = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())
dic={}
for i in range(q):
	t=ls[i]
	if t in dic:
		dic[t]=dic[t]+1
	else:
		dic[t]=1

num=0
for (key,value) in dic.items():
	num = num + value/2
print num
