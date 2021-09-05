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

n,m = map(int , ins[0].strip().split())
al= map(int , ins[1].strip().split())
al=sorted(al)

def picker(al):
	le=1
	rt=1
	lw=0
	rw=0
	n=len(al)
	i=0
	while i!=n-1:
		Tlw=lw + (al[i+1] - al[i])*le
		Trw=rw +(al[n-1]-al[n-2])*rt
		if Tlw > Trw:
			rw=Trw
			rt=rt+1
			n=n-1
		else:
			lw=Tlw
			le=le+1
			i=i+1
	return i

ax=[]
for j in range(m):
	t1=picker(al)
	ax.append(al[t1])
	del al[t1]
mx=0
for i in range(len(al)):
	t1=al[i]
	for j in range(len(ax)):
		t2=ax[j]
		mx=abs(t1-t2) +mx

print mx
