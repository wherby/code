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


n,k = map(int , ins[0].strip().split())
ls= map(int , ins[1].strip().split())
dp=[]
mxNum=10**14

re = []
for i in range(k+1):
	if (n-i-1-k) %(2*k+1) >= k+1 or (n-i-1-k) %(2*k+1) ==0 :
		t1= ls[i::2*k+1]
		x1=sum(t1)
		re.append(x1)

print min(re)




