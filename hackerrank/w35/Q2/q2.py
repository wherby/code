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

n,m,k = map(int , ins[0].strip().split())
re =[]
for i in range(n):
	t = [0]*n
	re.append(t)
t1=m
for i in range(n):
	re[i][i] = t1
	t1 = t1 +k
for i in range(n):
	for j in range(n):
		if i==j:
			pass
		elif i > j:
			re[i][j] = re[i-1][j] -1
		else:
			re[i][j] = re[i][j-1] -1

for i in range(n):
	tp = map(lambda x:str(x), re[i])
	rs=""
	print " ".join(tp)