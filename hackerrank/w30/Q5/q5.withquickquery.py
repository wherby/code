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





k,q = map(int , ins[0].strip().split())
ls=map(int , ins[1].strip().split())
out=[0]*q
querys=[]
idx=[]
index=2
for i in range(q):
	l,r,x,y= map(int , ins[index+i].strip().split())
	querys.append([x,y])
	idx.append([l,r])
for i in range(q):
	if out[i] ==0:
		x,y = querys[i]
		lsr = map(lambda z: z%x, ls)
		re =[0] * (k+1)
		for j in range(k):
			if lsr[j] == y:
				re[j+1] = re[j]+1
			else:
				re[j+1] =re[j]
		#print re
		for j in range(q):
			qx,qy = querys[j]
			if qx == x and qy == y :
				l,r = idx[j]
				#print l,r
				out[j] = re[r+1]-re[l]
				#print re[r+1] ,re[l]
for i in out:
	print i