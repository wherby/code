filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
CONSTPRIME = 1000000007

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

ls =[1]*2002
ls[2]=2
def getN():
	global ls
	for i in range(3,2001):
		ls[i]=ls[i-1] *(4*i -2) /(i+1) 
	#print ls
getN()
#print ls[10]
#print sum(ls[1:11])

q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index+i].strip().split())
	n= n/2 +1
	print sum(ls[1:n])%CONSTPRIME