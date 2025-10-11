# 
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/four_in_a_burrow_input.txt"
filename = "input/wrong0000.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


from functools import cache

from collections import defaultdict,deque
g =[]
dirs= []
ds = [(0,1),(1,0),(1,-1),(1,1)]
rst = defaultdict(int)
rdic ={"C":1,"F":2}
gp = defaultdict(list)
@cache
def getAllDir(x,y):
    ls = []
    for i in range(-3,1):
        for dx,dy in ds:
            t = []
            sx,sy =x+dx*i ,y + dy*i 
            for j in range(4):
                nx,ny = sx+j*dx ,sy+j*dy
                t.append((nx,ny))
            ls.append(t)
    return ls
#print(getAllDir(3,3))

def valid(x,y,tls):
    #print(x,y,tls)
    return 0<=x<6 and 0<=y<7 and tls[y]>x

def getResult(lst,tls):
    y,x=lst,tls[lst]
    x -=1
    ls = getAllDir(x,y)
    for item in ls:
        if(all(valid(x,y,tls) for x,y in item)):
            a1,a2,a3,a4 = item
            if g[a1[0]][a1[1]] == g[a2[0]][a2[1]] == g[a3[0]][a3[1]] == g[a4[0]][a4[1]]:
                return rdic[g[a1[0]][a1[1]]]
    return 0
         

@cache
def dfs(state):
    #print(g)
    ls = []
    for i in range(7):
        ls.append((state>>(i*3) )%8)
    # if lst != -1:
    #     C= getResult(lst, ls)
    #     if C:
    #         return C
    t = sum(ls)
    #print(t,ls,state)
    if t == 72:
        return "0"
    if t%2 ==0:
        for i,a in enumerate(ls):
            #print(i,a,g)
            if a <6 and g[a][i] == "C":
                nls = list(ls)
                nls[i]=a+1
                nstate = (state |(7<<(i*3)) ) - ((7- a-1)<<(i*3))
                gp[state].append(nstate)
                rst[nstate] = getResult(i,nls)
                if rst[nstate] ==0:
                    dfs(nstate)
    else:
        for i,a in enumerate(ls):
            #print(i,a,g)
            if a <6 and g[a][i] == "F":
                nls = list(ls)
                nls[i]=a+1
                nstate = (state |(7<<(i*3)) ) - ((7- a-1)<<(i*3))
                rst[nstate] = getResult(i,nls)
                gp[state].append(nstate)
                if rst[nstate] ==0:
                    dfs(nstate)
acc = 0
@cache 
def dfs2(state):
    global acc 
    acc = acc|rst[state]
    for b in gp[state]:
        dfs2(b)

ps = {}
def resolve():
    global g,ps,acc,rst,gp
    rst = defaultdict(int)
    gp = defaultdict(list)
    
    acc =0
    inp = input()
    g =[]
    for _ in range(6):
        ls = input()
        ls = [a for a in ls]
        g.append(list(ls))
    g = g[::-1]
    dfs(0)
    dfs.cache_clear()
    dfs2(0)
    dfs2.cache_clear()
    print(gp[1542])
    #print(acc)
    # for k,v in rst.items():
    #     if v ==1:
    #         print((k,v))
    if acc == 1:
        return "C"
    elif acc ==2:
        return "F"
    elif acc ==3:
        return "?"
    return "0"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)

