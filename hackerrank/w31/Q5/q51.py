filename = "input/input01.txt"
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

n,k = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())

s =0
t = 0
for i in range(n):
	s = s + ls[i] * ls[i]
	t = t + ls[i]

t = t * t -s

prob = float(0)
allP = float(1)
m = n
for i in range(k):
	cur = float(2) / m /(m-1)
	prob = cur * allP + prob
	allP  = (1-cur) * allP
	m  = m -1
#print prob,allP
re = (prob * t + s) * math.pi
print re 



