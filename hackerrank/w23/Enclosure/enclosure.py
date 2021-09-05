filename = "input/input02.txt"
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


print ins


def generateR(guessR):
	global ls



q, = map(int , ins[0].strip().split())
ls = map(float , ins[1].strip().split())
mx=sum(ls)
print mx
guessR=mx/(2*math.pi)
xls=[x/mx*2*math.pi for x in ls]

print xls


print ls

