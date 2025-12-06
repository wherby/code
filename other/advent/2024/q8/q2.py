import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')
from collections import defaultdict,deque
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
    dic = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if ls[i][j]!= ".":
                dic[ls[i][j]].append((i,j))
    sm =0
    vs ={}
    for k,v in dic.items():
        a1 = len(v)
        for i in range(a1):
            x1,y1= v[i]
            for j in range(a1):
                x2,y2=v[j]
                dx ,dy = x2-x1,y2-y1
                for k in range(n):
                    nx,ny = x2+k*dx, y2 +k*dy 
                    if 0<=nx<m and 0<=ny<n and ls[nx][ny] != k:
                        vs[(nx,ny)] =1
    print(len(vs))
    


solve()