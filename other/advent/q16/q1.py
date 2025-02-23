import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import defaultdict,deque
from heapq import heapify,heappop,heappush 

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin




def solve():
    mp =[]
    a = input()
    while len(a)>1:
        mp.append([a for a in a])
        a = input()
    m,n = len(mp),len(mp[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    visit = defaultdict(lambda : 10**10)
    sx,sy,tx,ty = -1,-1,-1,-1
    for i in range(m):
        for j in range(n):
            if mp[i][j] == "S":
                sx,sy = i,j 
                mp[i][j] ="."
            if mp[i][j] == "E":
                tx,ty =i,j
                mp[i][j] ="."
    st = [(0,sx,sy,0),(1000,sx,sy,1),(2000,sx,sy,2),(1000,sx,sy,3)]
    while st:
        c,x,y,d= heappop(st)
        #print(c,x,y,d)
        if visit[(x,y,d)] <=c:continue
        visit[(x,y,d)] =c
        if x == tx and y ==ty:
            print(c)
            return c
        for i,(dx,dy) in enumerate(dirs):
            if i ==d:
                cc =1 
            elif abs(i-d)%4==2:
                cc =2001
            else:
                cc = 1001
            nx,ny =x+dx,y+dy
            if 0<=x+dx<m and 0<=y+dy<n and mp[nx][ny]!="#":
                heappush(st,(c+cc,nx,ny,i))
    

solve()