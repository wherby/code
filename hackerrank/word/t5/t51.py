filename = "input/input00.txt"
f=open(filename,'r')

import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin

def isValid(n,k,b):
	if b>k or b ==0:
		return False
	if b==k and n != k*b - b*(b-1)/2:
		return False
	if n <= k*b - b*(b-1)/2:
		return True
	else:
		return False


def lst(n,k,b):
	re=[]
	res=n
	for i in range(b):
		re.append(i+1)
		res=res-i-1
	if res <0:
		return [-1]
	for i in range(b):
		idx = b-1-i
		ki=k-i
		tp=k-b
		if res >tp:
			res = res -tp
			re[idx] = re[idx] +tp
		else:
			re[idx]=re[idx]+ res
			res=0
	if res !=0:
		re=[-1]
	return re




ins=[]
for line in inputA:
    ins.append(line.strip())
q, = map(int , ins[0].strip().split())
index =1
for i in range(q):
	n1,k,b, =map(int , ins[index+i].strip().split())

	re=lst(n1,k,b)
	re=sorted(re)
	re =map(str,re)
	if re[0] !=-1:
		print " ".join(re)
	else:
		print -1
	