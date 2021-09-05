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



def getResult(k,x,d,ls):
	ls2 = map(lambda t1 : max(k*100,x*t1),ls)

	s1 = sum(ls2)

	if s1 > d *100:
		print "upfront"
	else:
		print "fee"



q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,k,x,d= map(int , ins[index+i*2].strip().split())
	ls =  map(int , ins[index+i*2+1].strip().split())
	getResult(k,x,d,ls)