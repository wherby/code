#https://www.hackerrank.com/challenges/grid-challenge
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


def very(re, n):
	isOrd=True
	for i in range(n):
		for j in range(n-1):
			if re[j][i] > re[j+1][i]:
				isOrd=False
				print "NO"
				return
			
	print "YES"
	return
	


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	n,= map(int , ins[index].strip().split())
	re=[]
	for j in range(n):
		t1=ins[index + 1 +j].strip()
		t2=[x for x in t1]
		t2= sorted(t2)
		re.append(t2)
	very(re,n)
	index = index + n +1



