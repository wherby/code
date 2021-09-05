#https://www.hackerrank.com/contests/world-codesprint-7/challenges/summing-pieces

filename = "input/input02.txt"
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

LLS =[ls[0]]
LLLS =[0]
CONST=1000000007
SEQ=2**0

for i in range(1,q):
	t1 = ls[i]
	t2 = LLS[i-1] *2
	#print LLLS[i-1],ls[i-1]
	t3 = (LLLS[i-1] + ls[i-1] * SEQ )%CONST

	t4 = t1*(SEQ*4 -1)
	#print t3,t4 
	t5 = (t3 +t2 +t4) %CONST
	LLS.append(t5)
	LLLS.append(t3)
	SEQ = (SEQ *2) % CONST

print LLS[-1]
