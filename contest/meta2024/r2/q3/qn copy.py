from functools import cache
g =[]


dirs= []
ds = [(0,1),(1,0),(1,-1),(1,1)]

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
                #print(item)
                return g[a1[0]][a1[1]]
         
lst = -1

rets = set([])

@cache
def dfs(state):
    #print(g)
    global lst,rets
    ls = []
    for i in range(7):
        ls.append((state>>(i*3) )%8)
    if lst != -1:
        C= getResult(lst, ls)
        nxx =[]
        for i in range(7):
            if ls[i] <6:
                nxx.append(g[ls[i]][i])
        t = sum(ls)
        isG = True
        nxx= list(set(nxx))
        if len(nxx) > 0:
            if t%2 ==0:
                if len(nxx) ==1 and nxx[0]=="F":
                    isG =False
            else:
                if len(nxx) ==1 and nxx[0]=="C":
                    isG =False
        if C and isG:
            rets.add(C)
            return 
    t = sum(ls)
    if t == 72:
        return "0"
    ret =[]
    if t%2 ==0:
        for i,a in enumerate(ls):
            #print(i,a,g)
            if a <6 and g[a][i] == "C":
                lst = i
                dfs((state |(7<<(i*3)) ) - ((7- a-1)<<(i*3)))
    else:
        for i,a in enumerate(ls):
            #print(i,a,g)
            if a <6 and g[a][i] == "F":
                lst =i
                dfs((state |(7<<(i*3)) ) - ((7- a-1)<<(i*3)))


rets = set([])

def resolve():
    global g,rets
    rets= set([])
    inp = input()
    g =[]
    for _ in range(6):
        ls = input()
        ls = [a for a in ls]
        g.append(ls)
    g = g[::-1]
    cnt = 0 
    #print(g)
    #dfs(43)
    lst =-1
    
    dfs(0)
    ret = set(rets)
    print(ret)
    dfs.cache_clear()
    if len(ret) ==1:
        return list(ret)[0]
    if len(ret) ==2:
        return "?"
    return "0"

def op(caseidx):
    cnt = resolve()
    print("Case #"+str(caseidx+1)+": "+str(cnt))

for i in range(int(input())):
    op(i)