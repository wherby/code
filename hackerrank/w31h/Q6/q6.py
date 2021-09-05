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


#print ins


def indexForLS(ls,indexLs):
	n = len(ls)
	for i in range(n):
		indexLs.append([])
	for i in range(n):
		t = ls[i]
		indexLs[t].append(i)
	#print indexLs



def queryls(ls,l,r,x,indexLs):
	find=-1
	n=len(ls)
	for i in range(n):
		#print indexLs
		tls = filter(lambda x : x>=l and x <=r, indexLs[i])
		if len(tls) ==x:
			find = i
			break
		#print tls
	print find


q, = map(int , ins[0].strip().split())
index=1
for i in range(q):
	indexLs=[]
	ls= map(int , ins[index+1].strip().split())
	indexForLS(ls,indexLs)
	#print ls
	qn,=map(int , ins[index+2].strip().split())
	for j in range(qn):
		l,r,x =map(int , ins[index+3+j].strip().split())
		queryls(ls,l,r,x,indexLs)
		#print l,r,x

	index = index + 3 +qn