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


n = map(int , ins[0].strip().split())[0]
p = map(int , ins[1].strip().split())[0]
#print n,p


def getN(n,p):
	cnt = 0
	find =n/2 *2
	p = p/2*2
	if find != p and find +1 != p :
		return (find-p)/2
	else:
		return cnt

n1= getN(n,p)
n2 =p/2
n3 = min (n1,n2)
print n3

	


