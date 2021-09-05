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


ls ="0"
def revert(k):
	if k == "0":
		return "1"
	else:
		return "0"

def growLS(ls):
	n = len(ls)
	for i in range(n):
		ls = ls + revert(ls[i])
	return ls

n = len(ls)
while n< 2001:
	ls = growLS(ls)
	n = len(ls)
#print ls


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index+i].strip().split())
	print ls[n]