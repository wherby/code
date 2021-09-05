#https://www.hackerrank.com/contests/moodysuniversityhackathon/challenges/small-risk-trading
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


q,n = map(int , ins[0].strip().split())
index=1
pp= map(float , ins[1].strip().split())
ps= map(float , ins[2].strip().split())
ls=map(float , ins[3].strip().split())
pl= map(lambda x: 1- x, pp)
pw= map(lambda i : pp[i] * ps[i] - pl[i] *ls[i],range(q))

pw=sorted(pw)

px=pw[q-n:]
px= filter(lambda x: x>0,px)
print '%.2f'%sum(px)
