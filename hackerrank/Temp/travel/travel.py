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

q,m = map(int , ins[0].strip().split())
index=1
LS=[]
for i in range(q):
	T1= map(int , ins[index+i].strip().split())
	LS.append(T1)


re=[]
for i in range(m):
	s=[]
	for j in range(q):
		s.append(LS[j][i])
	s=sorted(s)
	a=s[(q-1)/2]
	re.append(str(a))
print " ".join(re)