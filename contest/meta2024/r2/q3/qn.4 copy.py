# 
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/four_in_a_burrow_input.txt"
#filename = "input/wrong0000.txt"
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
#print(len(getAllDir(2,3)))

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
    # if lst != -1:
    #     C= getResult(lst, ls)
    #     if C:
    #         return C
    t = sum(state)
    #print(t,ls,state)
    cnt = 0
    if t == 42:
        return 0
    re1 = 0
    if t%2 ==0:
        for i,a in enumerate(state):
            #print(i,a,g)
            if a <6 and g[a][i] == "C":
                nls = list(state)
                nls[i]=a+1
                nstate = tuple(nls)
                re1 =dfs(nstate)+1
                if re1 + t ==42:
                    cnt = re1
                    gp[state].append(nstate)
                    rst[nstate] = getResult(i,nls)|rst[nstate]
    else:
        for i,a in enumerate(state):
            #print(i,a,g)
            if a <6 and g[a][i] == "F":
                nls = list(state)
                nls[i]=a+1
                nstate = tuple(nls)
                re1 = dfs(nstate) +1
                if re1 + t == 42:
                    cnt =re1
                    gp[state].append(nstate)
                    rst[nstate] = getResult(i,nls)|rst[nstate]
    #print(re1+t,cnt,re1,t)
    return cnt
acc = 0
@cache 
def dfs2(state):
    global acc 
    acc = acc|rst[state]
    
    # if rst[state] ==1:
    #     print(state)
    if rst[state]>0:
        return 
    for b in gp[state]:
        dfs2(b)

def resolve():
    global g,acc,rst,gp
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
    dfs(tuple([0]*7))
    dfs.cache_clear()
    dfs2(tuple([0]*7))
    dfs2.cache_clear()
    
    # for k,v in rst.items():
    #     if v ==1:
    #         print((k,v))
    #print(acc)
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

# CxxF
# CxxF
# CxxF
# CxxC
# FxFC
# CxFCF