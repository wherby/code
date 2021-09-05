filename = "input/input01.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
from collections import deque

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)

####Convex hull
#https://blog.csdn.net/anakin7/article/details/53822429
#https://wcipeg.com/wiki/Convex_hull_trick
#https://www.hackerrank.com/contests/w30/challenges/poles/editorial
#####

class Line():
    def __init__(self,slope,xterm):
        self.slope = slope
        self.xterm = xterm
    
    def get(self,x):
        return self.slope *x + self.xterm

def area(a,b,c):
    ax = b.slope - a.slope
    bx = c.xterm - a.xterm
    ay = c.slope - a.slope
    by = b.xterm - a.xterm
    return ax * bx - ay *by

def cw(a,b,c):
    return area(a,b,c) <0

def insert(l, lines):
    while len(lines) >1 and cw(lines[len(lines)-2],lines[len(lines) -1], l):
        lines.pop()
    if len(lines) ==1:
        if lines[0].xterm > l.xterm:
            lines.append(l)
    else:
        lines.append(l)

def query(x,lines):
    if len(lines) ==0:
        return 0
    while len(lines) > 1 and lines[0].get(x) > lines[1].get(x):
        lines.popleft()
    return lines[0].get(x)

##########

MAXN = 5000

weight =[0] *(MAXN+5)
pos =[0] *(MAXN+5)
A = [0] *(MAXN+5)
B = [0] *(MAXN+5)
F = [0] *(MAXN+5)

dp = [[0 for i in range(2)] for j in range(MAXN)]

lines = deque()

num,K= map(int , ins[0].strip().split())
index=1


for i in range(num):
    h,n= map(int , ins[index+i].strip().split())
    pos[num-1 - i] = h
    weight[num -1-i] = n


for i in range(num):
    A[i] = weight[i] + [0, A[i-1]][i > 0]
    B[i] = pos[i] * weight[i] + [0, B[i-1]][i > 0]
    F[i]= dp[i][1]= B[i] -pos[i] *A[i]

for k in range(2,K+1):
    lines.clear()
    l = Line(A[k-2],dp[k-2][(k-1) & 1] -B[k-2])
    insert(l,lines)

    for x in range(k-1,num):
        if x+1 == k:
            dp[x][k&1] =0
        else:
            dp[x][k&1] = F[x] + query(pos[x],lines)
        l = Line(A[x],dp[x][(k-1) & 1] -B[x])
        insert(l,lines)
print dp[num-1][K&1]

    