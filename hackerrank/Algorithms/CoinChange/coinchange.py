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



def change(ls,mrx,i):
	n1=len(ls)
	print i
	for j in range(n1):
		if i>=ls[j]:
			t=i-ls[j]
			if len(mrx[t])==0:
				mrx[i]=[[ls[j]]]
			else:
				tp=[t1.append(ls[j]) for t1 in mrx[t]]
				if len(mrx[i])==0:
					print mrx[i]
					mrx[i]=tp
				else:
					mrx[i].append(tp)
					print mrx[i]
	print mrx

N,m = map(int , ins[0].strip().split())
mrx=[[]]*(N+1)

ls= map(int , ins[1].strip().split())
for i in range(N+1):
	change(ls,mrx,i)

print mrx[3]


