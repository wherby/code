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

q, = map(str , ins[0].strip().split())
n,= map(int , ins[1].strip().split())
al=[]

def getA(al,n):
	re =0
	for i in range(n):
		if i in al:
			re=re +1
	return re

for i in range(len(q)):
	if q[i]=='a':
		al.append(i)
sl=len(q)

re = n/sl *len(al) +getA(al,n%sl)
print re
