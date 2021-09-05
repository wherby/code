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


#print ins
#[LIB]
#find distance of full binary tree
def getDisBinary(a,b):
	a = "{0:b}".format(a)
	b ="{0:b}".format(b)
	n = len(a)
	for i in range(n,0,-1):
		t1 = a[:i]
		if t1 == b[:i]:
			re = len(a) + len(b) -i*2
			return re

		
def getLestDis(start,fd,end):
	global fdl
	t1= fdl[fd-1]
	x1 = map(lambda x: getDisBinary(start,x)+ getDisBinary(x,end),t1)
	return min(x1)

n,m,q = map(int , ins[0].strip().split())
index=1
fdl=[]
for i in range(m):
	ls= map(int , ins[index+i].strip().split())
	fdl.append(ls[1:])
index = index +m
start = 1
re=0
for i in range(q):
	f,d =  map(int , ins[index+i].strip().split())
	x1 = getLestDis(start,f,d)
	re = re +x1
	start = d
print re

