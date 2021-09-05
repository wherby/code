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



p,d,m,s = map(int , ins[0].strip().split())
ls =[]
p1 = p
t2 =0
for i in range(p):
	if p1 > m:
		t2 = t2+ p1
		if t2 > s:
			break
		ls.append(p1)
		p1=p1-d
	else:
		break
if s < t2  :
	print len(ls)
else:
	n = (s-t2 ) /m + len(ls)
	print n
