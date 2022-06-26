import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

m,n =0,0
f =[[-10**9]*(301) for _ in range(301)]
sons = [[] for _ in range(301)]
vs = [0]*(301)

def dp(x):
    global m
    #print(x)
    f[x][0] = 0
    for y in sons[x]:
        dp(y)
        for t in range(m,-1,-1):
            for j in range(0,t+1):
                f[x][t] =max(f[x][t],f[x][t-j] +f[y][j])
    if x !=0:
        for t in range(m,0,-1):
            f[x][t] = f[x][t-1] + vs[x]
    

def resolve():
    global m,n
    n,m = tuple(map(lambda x: int(x),input().split()))
    
    for i in range(1,n+1):
        p,x = tuple(map(lambda x: int(x),input().split()))
        vs[i] = x 
        sons[p].append(i)
   
    dp(0)
    return f[0][m]
    

re =resolve()
print(re)
# print(f[0][:6])
# print(f[1][:6])
# print(f[2][:6])
# print(f[3][:6])
# print(f[4][:6])