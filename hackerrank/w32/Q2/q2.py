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

def getn(m,hit):
	n = m /hit
	if n * hit == m :
		return n 
	else: 
		return n +1

def getCNT(nls,t):
	cnt=0
	n = len(nls)
	for i in range(n):
		if t >= nls[i]:
			cnt = cnt +1
			t = t - nls[i]
		else:
			break
	return cnt


n,hit,t = map(int , ins[0].strip().split())
ls= map(int , ins[1].strip().split())

ls = sorted(ls)
#print ls
nls = map(lambda x: getn(x,hit),ls)
#print nls
print getCNT(nls,t)