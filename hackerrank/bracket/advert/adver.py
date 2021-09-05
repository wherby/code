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
a=5
re=[2]
for i in range(q-1):
	a = a/2 *3
	re.append(a/2)
print sum(re)