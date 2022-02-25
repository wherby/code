# https://www.hackerrank.com/contests/projecteuler/challenges/euler082/problem
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
# import os
print(os.getcwd())
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import heapq

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin
#inputA =["1","1"]

ins=[]
for line in inputA:
    ins.append(line)
n = int(ins[0])
gird = []
for i in range(n):
    line = ins[i+1]
    line =list(map(lambda x : int(x),line.split(" ")))  
    gird.append(line)
start,end=n*n, n*n+1
g = [[] for _ in range(n*n+2)]

for i in range(n):
    for j in range(n):
        k = i*n +j
        if j ==0:
            g[n*n].append(k)
        if j == n-1:
            g[k].append(n*n+1)
        if i >0:
            k1 = (i-1)*n +j
            g[k].append(k1)
        if i<n-1:
            k1 = (i+1)*n +j
            g[k].append(k1)
        if j <n-1:
            k1 = k+1
            g[k].append(k1)
#print(g)
visisted= [0]*(n*n+2)
st = [(0,start)]
ans = -1
def getCost(a):
    if a >=n*n:
        return 0
    x,y = a//n, a %n
    return gird[x][y]
while st:
    #print(st)
    cost,num = heapq.heappop(st)
    if num ==end:
        ans = cost
        break
    for a in g[num]:
        if visisted[a] ==0:
            visisted[a] =1
            heapq.heappush(st,(cost+getCost(a),a))
print(ans)

