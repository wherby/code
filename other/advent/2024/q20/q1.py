import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
FILEDEBUG=False

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin
from heapq import heapify,heappop,heappush 
from collections import defaultdict,deque



def solve():
    ls = []
    a = input()
    while len(a)>1:
        ls.append([a for a in a ])
        a = input()
    n,m= len(ls),len(ls[0])
    sx,sy,ex,ey = -1,-1,-1,-1
    for i in range(n):
        for j in range(m):
            if ls[i][j] == "S":
                sx,sy = i,j
                ls[i][j] = "." 
            if ls[i][j] =="E":
                ex,ey = i,j
                ls[i][j] = "."
    cand = set([])
    for i in range(m):
        for j in range(n):
            if i ==0 or i == m-1 or j == 0 or j == n-1: continue
            if ls[i][j] == "#":
                if (ls[i-1][j] =="." and ls[i+1][j] ==".") or (ls[i][j-1] =="." and ls[i][j+1] =="."):
                    cand.add((i,j))
    def visit(sx,sy,ex,ey):
        visit ={}
        cand=[(0,sx,sy)]
        while cand:
            c,x,y = heappop(cand)
            if (x,y) in visit:continue
            visit[(x,y)] =c 
            if x ==ex and y == ey:
                return c
            for dx,dy in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if ls[dx][dy] == ".":
                    heappush(cand,(c+1,dx,dy))
    c1 = visit(sx,sy,ex,ey)
    sv = defaultdict(int)
    for cx,cy in cand:
        ls[cx][cy] ="."
        c2 = visit(sx,sy,ex,ey)
        sv[c1-c2] +=1 
        ls[cx][cy] = "#"
    cm = 0 
    for k,v in sv.items():
        if k >=100:
            cm +=v 
    print(cm)
                
    
    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    