import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


mp =[]

def move(cx,cy,dx,dy):
    if mp[cx+dx][cy+dy] ==".":
        return (cx+dx,cy+dy)
    elif mp[cx+dx][cy+dy] =="#":
        return (cx,cy)
    else:
        ccx,ccy =cx,cy
        while mp[cx+dx][cy+dy] =="O":
            cx,cy =cx+dx,cy+dy
        if mp[cx+dx][cy+dy] == ".":
            mp[cx+dx][cy+dy] ="O"
            mp[ccx+dx][ccy+dy] ="."
            return (ccx+dx,ccy+dy)
        else:
            return (ccx,ccy)

def solve():
    a = input()
    while len(a)>1:
        mp.append([b for b in a])
        a = input()
    mvs =[]
    a = input()
    while len(a)>1:
        mvs.append(a)
        a = input()
    mvs ="".join(mvs)
    dirs ={"v":(1,0),"<":(0,-1),">":(0,1),"^":(-1,0)}
    m,n = len(mp),len(mp[0])
    cx,cy =-1,-1
    for i in range(m):
        for j in range(n):
            if mp[i][j] =="@":
                cx,cy = i,j 
                mp[i][j] ="."
    for m1 in mvs:
        dx,dy =dirs[m1]
        cx,cy = move(cx,cy,dx,dy)
    acc =0
    for i in range(m):
        for j in range(n):
            if mp[i][j] =="O":
                acc += i*100+j 
    print(acc)
    
    


solve()