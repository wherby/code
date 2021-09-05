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


q=len(ins)


index=0
for i in range(q):
	
	n= map(int , ins[index+i].strip().split())
	sb=[n[0]]
	m = len(n)
	for j in range(m-1):
		t1= n[j+1]-n[j]
		if t1 < -127 or t1 > 127:
			sb.append(-128)
		sb.append(t1)
	sb = map(str,sb)
	print " ".join(sb)