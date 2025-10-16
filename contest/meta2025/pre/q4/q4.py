
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filename = "input/input00.txt"
filename = "input/plan_out_validation_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


FILEDEBUG=True

if FILEDEBUG:
    import sys

    orig_stdout = sys.stdout
    f = open('./out.txt', 'w')
    sys.stdout = f

# (1,2) (3,1)
# (2,3) 

from collections import Counter
def resolve():
    N,M = list(map(lambda x: int(x),input().split()))
    lss = []
    g= [[] for _ in range(N)]
    c = Counter()
    for i in range(M):
        a,b = list(map(lambda x: int(x),input().split()))
        a,b = a-1,b-1
        g[a].append((b,i))
        g[b].append((a,i))
        lss.append((a,b,i))
        c[a]+=1
        c[b]+=1
    selcted =[0]*N
    visit ={}
    def dfs(a):
        while g[a] and g[a][-1][-1] in visit:
            g[a].pop()
        if len(g[a]) == 0:
            return []
        visit[g[a][-1][-1]] =1 
        b,i = g[a].pop()
        return [(a,b,i)] + dfs(b)
    choose= [-1]*M
    #print(lss)
    kvs = [(v,k) for k,v in c.items()]
    kvs.sort(reverse=True)
    for v1,k1 in kvs:
        while g[k1] and g[k1][-1][-1] in visit:
            g[k1].pop()
        if len(g[k1]) ==0:
            continue
        a = k1 
        b,i, =g[k1].pop()

        visit[i] =1 
        tmp = [(a,b,i)]
        tmp +=  dfs(b)
        tmp = tmp[::-1]
        tmp +=dfs(a)
        first,last = tmp[0][0],tmp[-1][1]
        if selcted[first] == 0 and selcted[last]!=0:
            tmp = tmp[::-1]
            first,last = last,first
        if c[last] > c[first]:
            tmp = tmp[::-1]
            first,last = last,first
        
        if first == last and len(tmp) %2 ==1:
            a1,b1,i1 = tmp.pop()
            if selcted[a1] + selcted[b1]<0:
                selcted[a1] +=1
                selcted[b1] +=1
                choose[i1] = 1 
            elif selcted[a1] + selcted[b1] > 0:
                selcted[a1] -=1
                selcted[b1] -=1
                choose[i1] =2 
            elif selcted[a1]  < 0:
                selcted[a1] +=1
                selcted[b1] +=1
                choose[i1]=1
            else:
                selcted[a1] -=1
                selcted[b1] -=1
                choose[i1] =2

        if selcted[first]<0:
            selcted[first] +=1
            lastc = 1
            for a1,b1,i1 in tmp:
                choose[i1] = lastc
                lastc = 3-lastc
            if lastc == 1:
                selcted[last] -=1
            else:
                selcted[last] +=1
        else:
            selcted[first] -=1
            lastc =2 
            for a1,b1,i1 in tmp:
                choose[i1] = lastc
                lastc = 3-lastc
            if lastc == 1:
                selcted[last] -=1
            else:
                selcted[last] +=1
    dic = [[0]*N for _ in range(2)]
    for i,c in enumerate(choose):
        a,b,i1 = lss[i]
        dic[c-1][a]+=1
        dic[c-1][b] +=1 
    acc = 0
    for i in range(2):
        for a in dic[i]:
            acc += a**2
    #print(acc,choose,selcted)
    choose = "".join([str(a) for a in choose])
    return str(acc),choose
def op(caseidx):
    acc,choose = resolve()
    print("Case #"+str(caseidx+1)+": "+acc +" "+choose)


for i in range(int(input())):
    op(i)