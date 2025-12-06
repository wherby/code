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
from collections import defaultdict,deque

def solve():
    ls = []
    a = input()
    while len(a)>1:
        ls.append(a)
        a = input()
    m,n = len(ls),len(ls[0])
    visit={}
    res=[]

    def getSlide(tls):
        tset =defaultdict(int)
        target = ls[tls[0][0]][tls[0][1]]
        #print(target,tls) 
        st =set(tls)
        for x,y in tls:
            tset[(x,y,x+1,y)]+=1
            tset[(x,y,x,y+1)] +=1
            tset[(x+1,y,x+1,y+1)] +=1
            tset[(x,y+1,x+1,y+1)] +=1
        sps = {}
        for x,y in tset.items():
            if y ==1:
                sps[x] =1 
        acc =0 
        print(sps)
        for x1,y1,x2,y2 in sps.keys():
            if x1 ==x2:
                if (x1-1,y1,x1,y1) in sps :
                    acc +=1
                if (x1,y1,x1+1,y1) in sps :
                    acc +=1
                if (x1-1,y1,x1,y1) in sps  and (x1,y1,x1+1,y1) in sps:
                    acc -=1
                if (x2-1,y2,x2,y2) in sps :
                    acc +=1
                if (x2,y2,x2+1,y2) in sps :
                    acc +=1
                if (x2-1,y2,x2,y2) in sps and (x2,y2,x2+1,y2) in sps :
                    acc -=1
            else:
                if (x1,y1-1,x1,y1) in sps:
                    acc+=1
                if (x1,y1,x1,y1+1) in sps:
                    acc  +=1
                if (x1,y1-1,x1,y1) in sps and (x1,y1,x1,y1+1) in sps:
                    acc -=1 
                if (x2,y2-1,x2,y2) in sps:
                    acc +=1
                if (x2,y2,x2,y2+1) in sps :
                    acc +=1
                if (x2,y2-1,x2,y2) in sps and (x2,y2,x2,y2+1) in sps:
                    acc -=1
        return acc

    def dfs(x,y):
        if (x,y) not in visit:
            visit[(x,y)] =1
            ret.append((x,y))
            for nx,ny in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
                if 0<=nx<m and 0<=ny<n and ls[nx][ny] == ls[x][y]:
                    dfs(nx,ny) 
        else:
            return 
    for i in range(m):
        for j in range(n):
            if (i,j) not in visit:
                ret =[]
                dfs(i,j)
                res.append(ret)
    sm = 0
    for tl in res:
        a = len(tl)

        tt=  getSlide(tl)
        print(tl,tt)
        sm += a*tt//2
    print(sm)


solve()

# Wrong ans : too high 845014