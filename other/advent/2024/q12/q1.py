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


def solve():
    ls = []
    a = input()
    while len(a)>1:
        ls.append(a)
        a = input()
    m,n = len(ls),len(ls[0])
    visit={}
    res=[]
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
        acc = 0
        for x,y in tl:
            acc +=4 
            for nx,ny in (x+1,y),(x,y+1),(x-1,y),(x,y-1):
                #print(nx,ny,x,y)
                if 0<=nx<m and 0<=ny<n and ls[nx][ny] == ls[x][y]:
                    acc -=1
        sm += acc*a
    print(sm)


solve()