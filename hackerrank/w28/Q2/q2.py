filename = "input/input10.txt"
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



def getN(m):
	cnt=0
	n=m
	while n != 0:
		n = n/2
		cnt = cnt +1
	an= 1<<cnt
	print an-m -1


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index+i].strip().split())
	getN(n)