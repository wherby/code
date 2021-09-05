filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w24/challenges/xor-matrix

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import copy

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)
n,m = map(int , ins[0].strip().split())
#m = m%n
index=1
ls = map(int , ins[1].strip().split())
P1= map(lambda  x : set([x]),range(n))

m=28

def yangTri(m):
	s=1
	b1=m
	s1=1
	re = []
	for i in range(m+1):
		re.append(s)
		s = s * b1 / s1
		s1 = s1 + 1 
		b1 = b1 - 1
	return re

for j in range(m):
	p2 = yangTri(j)
	print j
	print  p2


