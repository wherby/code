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

def XorAll(ls):
	re=0
	n = len(ls)
	for l1 in ls:
		re = re ^ (l1 - 1  ^1) +1
	if re ==0:
		print 'W'
	else:
		print 'L'



q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	ls= map(int , ins[index+i*2 +1].strip().split())
	XorAll(ls)
