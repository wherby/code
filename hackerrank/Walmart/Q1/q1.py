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
n,= map(int , ins[1].strip().split())

def getNumber(n):
	sm=0
	tp=1
	for i in range(n,0,-1):
		tp= tp * i /(n-i +1)
		sm =sm +tp
	return sm
a1 = getNumber(q)
if a1>= n:
	print a1-n
else:
	print n-a1