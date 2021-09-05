filename = "input/input001.txt"
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


q = len(ins)

NUM = int(ins[0])
index=1
ls=[]
for i in range(q-1):
	n,= map(int , ins[index+i].strip().split())
	ls.append(n)
ls.sort()
l=0 
r=q-2
FD= False
while(l < r):
	t1= ls[l] + ls[r]
	if t1 > NUM:
		r =r-1
	elif t1 < NUM:
		l = l +1
	else:
		FD = True
		break

if FD == False:
	print 0
else:
	print 1
