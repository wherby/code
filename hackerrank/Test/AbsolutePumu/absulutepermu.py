#https://www.hackerrank.com/challenges/absolute-permutation
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



q, = map(int , ins[0].strip().split())
index =1

def getReorder(m,n):
	org=[i+1 for i in range(n)]
	re=[]
	bs=True
	if m==0:
		return org
	if n %(2*m) !=0:
		return [-1]
	else:
		i=0
		while(i<n):
			for j in range(m):
				re.append(i+m+1)
				i=i+1
			for j in range(m):
				re.append(i+1-m)
				i=i+1

	return re




for i in range(q):
	n,m = map(int , ins[index +i].strip().split())
	re= getReorder(m,n )
	re =map(str,re)
	print " ".join(re)
	pass
