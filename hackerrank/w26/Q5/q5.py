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



n, = map(int , ins[0].strip().split())


def getN(m,n):
	global dic1
	cn=0
	if n == 0 :
		return 0
	for i in range(m+1,n+1):
		if n%i ==0 :
			if i not in dic1:
				dic1[i] =1
				cn = cn +1
	return cn
 
sm =0

for i in range(1,n ):
	dic1={}
	for j in range(1,n/i +1):
		cn = getN(i, n -i*j)
		sm = sm +cn
print sm


