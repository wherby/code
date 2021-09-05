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

def newDay(ls):
	re=[]
	re.append(ls[0])
	n=len(ls)
	for i in range(1,n):
		if ls[i-1]>ls[i]:
			re.append(ls[i])
	return re

q, = map(int , ins[0].strip().split())
ls= map(int , ins[1].strip().split())
days=0
newS=newDay(ls)
ps=len(ls)
while len(newS) != ps:
	ps=len(newS)
	newS=newDay(newS)
	days=days+1
print days
