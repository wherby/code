filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/contests/w26/challenges/best-divisor
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)



def factorizeWithAllDivisor(n):
	factors=[]
	for i in range(1,n+1):
		if i* i > n:
			break
		if n%i ==0:
			factors.append(i)
			if n/i != i :
				factors.append(n/i)
	return factors

def getValue(n):
	s=0
	while n !=0:
		x= n % 10
		s = s +x
		n = n /10
	return s

n = map(int , ins[0].strip().split())
ls= factorizeWithAllDivisor(n[0])
lsv=map(getValue,ls)
mxvalue= max(lsv)
ls = filter(lambda x : getValue(x) == mxvalue, ls)
print min(ls)