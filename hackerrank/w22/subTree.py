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
    ins.append(line.strip())
n, = map(int , ins[1].strip().split())

al = []
for i in range(len(ins)):
	al.append(ins[2+i])
print al

ve=map(int ,al[0].split())
ve1=
ve2=map(int ,al[1].split())


print sum(ve2)/float(sum(ve))