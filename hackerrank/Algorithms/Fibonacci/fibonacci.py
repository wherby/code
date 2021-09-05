#https://www.hackerrank.com/challenges/fibonacci-modified
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


def fibonacci(t0,t1):
	t2=t0+t1**2
	return (t1,t2)

t0,t1,n = map(int , ins[0].strip().split())
for i in range(n-2):
	t0,t1=fibonacci(t0,t1)
print t1
