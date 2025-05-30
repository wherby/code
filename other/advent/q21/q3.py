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


from collections import defaultdict,deque
from itertools import pairwise
mp1 = [["7","8","9"],["4","5","6"],["1","2","3"],[-1,"0","A"]]
mp2 = [[-1,"^", "A"],["<","v",">"]]

dir={(-1,0):"^", (0,-1):"<",(1,0):"v",(0,1):">"}



def shortpath(a,b,mp):
    m,n = len(mp),len(mp[0])
    fx,fy = -1,-1
    for i in range(m):
        for j in range(n):
            if mp[i][j] == a :
                fx = i 
                fy = j 
    ret = []

    cand = deque([(fx,fy,[])])
    vs =defaultdict(lambda : 10**10)
    while cand:
        x,y ,t1 = cand.popleft()
        if vs[(x,y)]<len(t1): continue
        vs[(x,y)] =len(t1)
        if mp[x][y] == b:
            if len(ret)== 0 or len(t1) == len(ret[-1]):
                ret.append(t1)
        for dx,dy in dir.keys():
            nx,ny = x+dx,y +dy
            if 0<=nx< m and 0<=ny<n  and mp[nx][ny] != -1:
                t2 = list(t1)
                t2.append(dir[(dx,dy)])
                cand.append((nx,ny,t2))
    return ret





def getMap(mp):
    m,n = len(mp),len(mp[0])
    keys = []
    for i in range(m):
        for j in range(n):
            if mp[i][j] != -1:
                keys.append(mp[i][j])

    sp ={}
    for a in keys:
        for b in keys:
            sp[(a,b)]= shortpath(a,b,mp)
   # print(sp)
    return sp




shortmapN= getMap(mp1 )
shortmapD = getMap(mp2)

#def getLs(ls):
#shortmapD[('A', '<')]= [['v','<',  '<']]
#shortmapD[('<', 'A')]= [['>', '>','^']]
print(shortmapD)


mxdic ={}


N = -1


mxx = []


# def trv(mat):
#     mat =list(zip(*mat))
#     return mat

def dfs(idx,res):
    global N
    if idx ==N:
        tmp = []
        for a in res:
            tmp.append(list(a))
        #tmp = trv(tmp)
        mxx.append(tmp)
        return 
    #print(ddkeys,idx,N)
    for vs in shortmapD[ddkeys[idx]]:
        vs1 =["A"] + vs +["A"]
        tmp = [0]*N
        for a,b in pairwise(vs1):
            tmp[mxdic[(a,b)]] +=1
        res.append(list(tmp))
        dfs(idx+1,res)
        res.pop()
    
    
ddkeys= []
def maxtrixD(map):
    global N,ddkeys
    N =len(map.keys())
    ddkeys = list(map.keys())

    for i,k in enumerate(ddkeys):
        mxdic[k] = i 
    dfs(0,[])
    #print(mxx)


#dmapmax =maxtrixD(shortmapD) 
maxtrixD(shortmapD) 



#print(dmx)
print(len(mxx), "*"*10)

print(mxdic)

def getLine(l1):
    global N,mxx
    #print(l1, "AAA")
    ret = 10**100
    l1 = ["A"] + l1
    ls =[0]*N
    for a,b in pairwise(l1):
        ls[mxdic[(a,b)]]+=1
    lss =[ls]
    for _ in range(25):
        tmp =[]
        for ls in lss:
            tmp.extend(travLine2(ls))
        mn = min([sum(a) for a in tmp])
        tt= []
        for a in tmp:
            if sum(a) == mn:
                tt.append(a)
        lss =tt[:100]
        print(len(tt))
        #print(len(list(lss)))
    
    print(mn ,"*"*100)
    return mn

def travLine2(ls):
    rss=[]
    for dmx in mxx:
        tmp=[0]*N 
        for i,a in enumerate(ls):
            t1 = [a*b for b in  dmx[i]] 

            tmp = [a+b for a,b in zip(tmp,t1)]
            #print(t1)
        rss.append(list(tmp))
    return rss


def processLine(l1):
    l1 = ["A"] + l1

    ret = [[]]
    for a,b in pairwise(l1):
        tmp = []
        for t1 in ret:
            for c in shortmapN[(a,b)]:
                t2 = list(t1) + c +["A"]
                tmp.append(t2)
        ret = tmp
    
    mx =10**100
    #print(mx,ret)
    #print("AAA")
    for l1 in ret:
        e = getLine(l1)
        #print(e,mx,"BB")
        mx = min(mx,e)
    return mx
    # res =[]
    # for i in range(2):
    #     tmp =[]
    #     for l1 in ret:
    #         tmp.extend(processLine2(l1))
    #     res =[len(a) for a in tmp]
    #     ret =tmp
    #     mn = min(res)
    #     ret =filter(lambda a: len(a) ==mn,ret)
    
    

    return res






def processLine2(l1):
    l1 = ["A"] + l1

    ret = [[]]
    for a,b in pairwise(l1):
        tmp = []
        for t1 in ret:
            for c in shortmapD[(a,b)]:
                t2 = list(t1) + c +["A"]
                tmp.append(t2)
        ret = tmp

    return ret


def solve():
    ls=[]
    a = input()

    while len(a)>1:
        ls.append([a for a in a ])
        a = input()
    sm = 0
    for l1 in ls:
        t2 ="".join(l1[:3])
        mn= processLine(l1)
        
        # t1= processLine(l1)
        # mn= min(t1)

        print(mn,"**")

        sm += int(t2)*mn
    print(sm)
    
    

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./.tmp/out2.txt', 'w')
    sys.stdout = f

solve()

if FILEDEBUG:
    sys.stdout = orig_stdout
    f.close()
    