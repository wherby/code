filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
from collections import defaultdict

def zero():
    return 0
dd2 = defaultdict(zero)

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)



n,k = map(int , ins[0].strip().split())
ls =  map(int , ins[1].strip().split())


for i in range(n):
    tmp = ls[i] - i *k
    dd2[tmp] =dd2[tmp]+1
minx=n
for k,v in dd2.items():
    tmp = n-v
    if tmp < minx:
        minx =tmp
print minx

