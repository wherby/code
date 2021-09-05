filename = "input/input00.txt"
f=open(filename,'r')
#https://www.hackerrank.com/contests/w24/challenges/happy-ladybugs
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
index=1
for i in range(q):
	n,= map(int , ins[index + i *2 ].strip().split())
	ls= ins[index + i *2 + 1].strip()
	isEmpty= ls.find('_')
	isHappy=True
	if isEmpty >=0:
		dic ={}
		for j in range(n):
			if ls[j] != '_':
				t = ls[j]
				if t in dic:
					dic[t] = dic[t] + 1
				else:
					dic[t] =1
		for k,v in dic.items():
			if v <2:
				isHappy=False
	else:
		m  = len(ls)
		if m == 1:
			isHappy=False
		for j in range(1,m-1):
			t = ls[j]
			if t != ls[j-1] and t != ls[j+1]:
				isHappy=False
	if isHappy ==True:
		print "YES"
	else:
		print "NO"