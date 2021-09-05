#https://www.hackerrank.com/challenges/xor-subsequence
filename = "input/input11.txt"
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
index=1

lst=[]
for i in range(q):
	n,= map(int , ins[index+i].strip().split())
	lst.append(n)
dica={}
def addTodic(n,dic):
	if n in dic:
		dic[n] = dic[n]+1
	else:
		dic[n]=1

for i in range(q):
	tmp=lst[i]
	addTodic(tmp,dica)
	for j in range(i+1,q):
		tmp=tmp ^ lst[j]
		addTodic(tmp,dica)
kdic=dica.keys()
kdic=sorted(kdic)
mx=0
mxk=0
for k in kdic:
	tp=dica[k]
	if tp>mx:
		mx=tp
		mxk=k
print str(mxk) + " " +str(mx)


