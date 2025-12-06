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

dp ={">":0,"v":1,"<":2,"^":3}
dir= [(0,1),(1,0),(0,-1),(-1,0)]


def travel(m,n,ls,x,y,cd):
    visit = {}
    vs ={}
    while 0<=x<n and 0<=y<m and (x,y,cd) not in visit:
        visit[(x,y,cd)] =1 
        vs[(x,y)] =1
        nx,ny = x + dir[cd][0], y + dir[cd][1]
        if 0<=nx<n and 0<=ny<m:
            if ls[nx][ny] != "#":
                x,y = nx,ny 
            else:
                cd = (cd+1)%4
        else:
            x,y = nx,ny
    return vs

def travel2(m,n,ls,x,y,cd):
    visit = {}
    vs ={}
    while 0<=x<n and 0<=y<m and (x,y,cd) not in visit:
        visit[(x,y,cd)] =1 
        vs[(x,y)] =1
        nx,ny = x + dir[cd][0], y + dir[cd][1]
        if 0<=nx<n and 0<=ny<m:
            if ls[nx][ny] != "#":
                x,y = nx,ny 
            else:
                cd = (cd+1)%4
        else:
            x,y = nx,ny
    #print(x,y)
    return 0<=x<n and 0<=ny<m

def solve():
    n = 130
    ls = []
    for _ in range(n):
        t1 =input()
        ls.append([a for a in t1])
    m = len(ls[0])
    x,y = -1,-1
    cd = -1
    for i in range(m):
        for j in range(n):
            if ls[i][j] in dp:
                x,y = i,j   
               #print(ls[i][j])
                cd = dp[ls[i][j]]
    vs = travel(m,n,ls,x,y,cd)

    cnt = 0
    for a,b in vs.keys():
        # if a != x and b!=y:
        ls[a][b]="#"
        if travel2(m,n,ls,x,y,cd):
            cnt +=1
            #print(a,b)
        ls[a][b]="."
    # ls[6][3]="#"
    # print(vs.keys(),x,y)
    # travel2(m,n,ls,x,y,cd)


    #print(visit)
    # for a in ls:
    #     print(a)
    print(cnt)

    


solve()