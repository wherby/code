__author__ = 'sware'

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://codepair.hackerrank.com/paper/JPcczN20?b=eyJyb2xlIjoiY2FuZGlkYXRlIiwibmFtZSI6ImgxODcyMjU1NzciLCJlbWFpbCI6IjE4NzIyNTU3N0BxcS5jb20ifQ%3D%3D

import math
import sys
import time

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)



n, = map(int , ins[0].strip().split())

st = time.clock()



divisors = [[1] for i in xrange(n)]

for i in xrange(2,n):
    for j in xrange(i, n, i):
        divisors[j].append(i)
    divisors[i].reverse()

#print divisors
#print time.clock() - st

tups = 0

for i in xrange(1, n):
    divs = set()
    for j in xrange(i, n, i):
        divisors[j].pop()
    for j in xrange(i, n, i):
        divs.update(divisors[n-j])
    #print divs
    tups += len(divs)

print tups
#print time.clock() - st