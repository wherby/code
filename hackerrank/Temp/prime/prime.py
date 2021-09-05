filename ="input/input00.txt"
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


def getPrimesInN(n,pl):
	for i in range(2,n):
		isPrime = True
		for j in range(len(pl)):
			t=pl[j]
			if i%t == 0:
				isPrime = False
				break
		if isPrime == True:
			pl.append(i)
	return

def getNum(n):
	c=1
	i=0
	while c<=n:
		c=c *pl[i]
		i = i +1
	print i-1

q, = map(int , ins[0].strip().split())
pl=[]
getPrimesInN(10000,pl)
index=1
for i in range(q):
	n,= map(int , ins[index+i].strip().split())
	getNum(n)

	