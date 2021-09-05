f = open('input/input00.txt')
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
ss=[]
q, = map(int , ins[0].strip().split())
index =1
mx=0
for i in range(q):
    a= map(int , ins[index + i].strip().split())
    if a[0]==1:
    	if len(ss) ==0:
    		mx=a[1]
    	if a[1]> mx:
    		mx=a[1]
    	ss.append((a[1],mx))
    if a[0]==2:
    	ss.pop()
    	if len(ss)>0:
    		mx=ss[-1][1]
    if a[0]==3:
    	print ss[-1][1]

        