import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin

from functools import cache

def solve():
    ls = []
    a = input()
    while len(a)>1:
        ls.append([int(b) if b.isdigit() else -1 for b in a])
        a = input()
    m,n = len(ls),len(ls[0])
    
    st=set([])

    @cache
    def dfs(i,j):
        if ls[i][j] ==9:
            return 1
        nxt = ls[i][j]+1
        ret =0
        for ni,nj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
            if 0<=ni<n and 0<=nj<m and ls[ni][nj] == nxt:
                ret +=dfs(ni,nj)
        return ret
    start =()
    acc = 0
    for i in range(m):
        for j in range(n):
            if ls[i][j] == 0:
                start =(i,j) 
                acc+=dfs(i,j)
                #print(i,j, dfs(i,j),"aa")
    #print(st)
    print(acc)
    return acc

solve()