f = open('input/input02.txt')
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

n, = map(int , ins[0].strip().split())
bl = map(int , ins[1].strip().split())
m, = map(int , ins[2].strip().split())
cl = map(int , ins[3].strip().split())

cl.sort()
x = 1
for j in range(len(cl)):
	c = cl[j]
	y = c > n and n or c
	for i in range(x-1,y-1):
		b=bl[i]
		if c > i+1 and c < b +i +1:
			bl[i]=c-i-1
	x = y

re=sum(bl)
print re
