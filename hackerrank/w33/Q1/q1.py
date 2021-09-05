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
ar1=map(int , ins[1].strip().split())
ar2=map(int , ins[2].strip().split())
sar1=sorted(ar1)
minx = ar1[0] + ar2[0]
for i in range(q):
	t = ar2[i]
	if sar1[0] == ar1[i]:
		p = t + sar1[1]
	else:
		p = t + sar1[0]
	if p < minx:
		minx = p
print minx