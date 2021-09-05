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
	if n <= k*b - b*(b-1)/2:
		return True
	else:
		return False

def needLs(n,k,b):
	if n <= k*b - b*(b-1)/2:
		return False
	else:
		return True

def lst(n,k,b):
	re=[]
	md=n/b
	mo=n/b
	ls=n/b
	isMO=True
	b=b-1
	n=n-mo
	re.append(mo)
	if b ==0:
		return re
	while b !=1:
		if isMO == True:
			if mo +1<=k and needLs(n-mo-1,ls,b-1):
				mo=mo+1
				b=b-1
				n=n-mo
				re.append(mo)
				isMO= needLs(n,ls,b)
			else:
				if ls-1>0:
					ls=ls-1
					b=b-1
					n=n-ls
					re.append(ls)
				isMO=needLs(n,ls,b)
		else:
			if ls -1 >0:
				ls=ls-1
				b=b-1
				n=n-ls
				re.append(ls)
				isMO=needLs(n,ls,b)
			else:
				if mo +1 <=k:
					mo=mo+1
					b=b-1
					n=n-mo
					re.append(mo)
				isMO= needLs(n,ls,b)
	if b ==1:
		re.append(n)
	return re




ins=[]
for line in inputA:
    ins.append(line.strip())
q, = map(int , ins[0].strip().split())
index =1
for i in range(q):
	n1,k,b, =map(int , ins[index+i].strip().split())
	if isValid(n1,k,b):
		re=lst(n1,k,b)
		re=sorted(re)
		re =map(str,re)
		print " ".join(re)
	else:
		print -1