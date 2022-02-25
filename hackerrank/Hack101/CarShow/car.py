filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
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

n,q = map(int , ins[0].strip().split())
ls = map(int , ins[1].strip().split())
vis = [0]*(n+1)
d = [0]*(n+1)
mx = [0]*(n+1)
for i in range(1,n+1):
    d[i] = ls[i-1]
po=1
for i in range(1,n+1):
    #print po
    while po < n+1 and vis[d[po]] ==0:
        vis[d[po]] =1 +vis[d[po]]
        po =po+1
    mx[i] = po-1

    vis[d[i]] = vis[d[i]] -1


