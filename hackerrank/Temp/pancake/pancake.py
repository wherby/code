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



q,n = map(int , ins[0].strip().split())
index=1
x=0
y=0
p=0
for i in range(n):
	a,b= map(int , ins[index+i].strip().split())
	if p==0:
		if a ==1:
			x=x+b
		else:
			y= b-x
			x=0
			p=1
	else:
		if a ==1:
			y=y+b
		else:
			x=b-y
			y= 0
			p=0


if p!=0:
	print "2 " +str (y%q)
else:
	print "1 " + str(q-x%q)