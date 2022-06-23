#https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b
from collections import defaultdict
import os
from re import L

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#filename = "input/input01.txt"
# timeout for ts2 for python3.7 
# will pass in pypy3
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008778ec/0000000000b158f8
filename = "input/ts2_input.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

if  "f" in locals():
    sys.stdin = f
else:
    inputA=sys.stdin


from collections import defaultdict,deque
class BipartileWithPriority:
    def __init__(self,m,n,g):
        self.used=[0]*(m+1)
        self.mt =[-1]*(n+1)
        self.g = g
    
    def dfs(self,x):
        if self.used[x]: return False
        self.used[x] = 1
        for y in self.g[x]:
            if self.mt[y] ==-1:
                self.mt[y] = x
                return True
        for y in self.g[x]:
            if self.dfs(self.mt[y]):
                self.mt[y] = x
                return True
        return False

def distance(ch1,cd1):
    return (ch1[0] -cd1[0])**2 + (ch1[1] -cd1[1])**2

def resolve():
    n = int(input())
    ch =[]
    for i in range(n):
        ls = [int(x) for x in input().split(" ")]
        x,y = ls[0],ls[1]
        ch.append((x,y))
    Jerry = [int(x) for x in input().split(" ")]
    cd= []
    for i in range(n):
        ls = [int(x) for x in input().split(" ")]
        x,y = ls[0],ls[1]
        cd.append((x,y))
    g =[[] for _ in range(n+1)]
    gg =[[] for _ in range(n+1)]
    for i in range(n):
        ch1= ch[i]
        t1 = (ch1[0] - Jerry[0])**2 + (ch1[1]-Jerry[1])**2
        for j in range(n):
            cd1 = cd[j]
            cdt = (ch1[0]-cd1[0])**2 + (ch1[1]-cd1[1])**2
            if cdt <= t1:
                gg[i+1].append((cdt, j+1))
    #print(g)
    for i in range(len(gg)):
        g1 = gg[i]
        g1.sort()
        for d,a in g1:
            g[i].append(a)
    kn = BipartileWithPriority(n,n,g)
    for i in range(1,n+1):
        if not kn.dfs(i):
            return []
        else:
            kn.used=[0]*(n+1)

    dic =defaultdict(list)
    manToCandi ={}
    ret =[]

    pos= [0]*(n+1)
    inOrd =[0]*(n+1)
    #print(kn.mt,g)
    for i in range(1,n+1):
        k = kn.mt[i]
        manToCandi[ kn.mt[i]]=i
        #print(k, g[i])
        for a in g[k]:
            #print(a,k,i,cd,ch)
            #print(ch[i-1],cd[a-1],cd[k-1])
            if a !=i and distance(ch[k-1],cd[a-1]) < distance(ch[k-1],cd[i-1]):
                inOrd[k] +=1
                dic[a].append(k)
            elif a ==i:
                break     
    st =deque([])
    #print(g)
    #print(inOrd,kn.mt,dic)
    #print(dic1)
    for i in range(1,n+1):
        if inOrd[kn.mt[i]] ==0:
            st.append([kn.mt[i],i])
    #print(st)
    while st:
        #print(st,inOrd)
        a,b =st.popleft()
        ret.append([a,b])
        #print(dic[b],dic[a],a,b)
        for c in dic[b]:
            inOrd[c] -=1
            if inOrd[c] ==0:
                st.append([c,manToCandi[c]])
        #print(st,inOrd)
    return ret
    

    

def op(caseidx):
    ret= resolve()
    if len(ret) ==0:
        print("Case #"+str(caseidx+1)+": IMPOSSIBLE" )
    else:
        print("Case #"+str(caseidx+1)+": POSSIBLE" )
        for a,b in ret:
            print(str(a)+ " " + str(b+1))
    

for i in range(int(input())):
    op(i)