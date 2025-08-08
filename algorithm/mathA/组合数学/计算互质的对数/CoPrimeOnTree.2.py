# https://www.hackerrank.com/contests/w27/challenges/coprime-paths/problem
# https://www.hackerrank.com/contests/w27/challenges/coprime-paths/submissions/code/1395597144
# 用DFSN计算非线性的树上莫队
# 结果是错误的
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
filename = "./input/input02.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

import sys
sys.setrecursionlimit(10000000)
if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)



class EulerTour:
    def __init__(self,  adj):
        self.n =n= len(adj)
        self.adj = adj
        self.in_time = [0] * n  
        self.out_time = [0] * n
        self.time = 0
        self.tour = [] 
        self.Fa = [-1]*n        
        

    def run(self, root):
        self._dfs(root, -1)
        return self.tour, self.in_time, self.out_time

    def _dfs(self, u, parent):
        self.in_time[u] = self.time
        self.time += 1
        self.tour.append(u)
        
        for v in self.adj[u]:
            if v != parent:
                self.Fa[v]=u
                self._dfs(v, u)
                self.tour.append(u)
                self.time += 1
        if parent !=-1:
            self.out_time[u] = self.time - 1

N,Q = map(int , ins[0].strip().split())

nums = list(map(int , ins[1].strip().split()))

index=2
edges = [[] for _ in range(N)]
for i in range(index ,index+N-1):
    a,b = map(int , ins[i].strip().split())
    a,b = a-1,b-1 
    edges[a].append(b)
    edges[b].append(a)
index = index+N-1
querys = []

dft = EulerTour(edges)
T,L,R =dft.run(0)
FA = dft.Fa
for i in range(index,index + Q):
    a,b =map(int , ins[i].strip().split())
    a,b = a-1,b-1
    querys.append((L[a],L[b]))




import math
def prepare(M):
    mu = [1] * M  
    F = [0] * M   
    q = []       
    
    mu[1] = 1   
    
    for i in range(2, M):
        if not F[i]:  
            F[i] = i
            q.append(i)
            mu[i] = -1  

        for p in q:
            if i * p >= M:
                break
            F[i * p] = p 
            if i % p == 0:
                mu[i * p] = 0  
                break
            else:
                mu[i * p] = -mu[i] 
    
    return mu, F, q

M = 10**7+1  
mu, F, primes = prepare(M)

def CoPrimeQuery(numsIdx,query):
    n = len(nums)
    ID = [-1]*M  
    p = [[] for _ in range(n)]
    ret = [-1]*len(query)
    for i,a in enumerate(nums):
        x = a 
        while x >1:
            f = F[x]
            if ID[f] != i : 
                ID[f] =  i 
                p[i].append(f)
            x //=f 
    ID =[0]*M
    ans = 0
    sz = 0
    S = [0]*M 
    S[0] =1
    Flag=[0]*M
    def deal(u,v,x):
        if v == FA[u]:
            u,v = v,u 
        if L[x] >= L[v] and R[x] <= R[v]:
            modify(u,-1 if Flag[v] else 1)
        else:
            modify(v,-1 if Flag[v] else 1)
        Flag[v] ^=1

    def modify(x,op):
        nonlocal ans,sz
        sz +=op 
        for s in range(1,1<<len(p[x])):
            _s = s -(s&-s)
            S[s] = S[_s]*p[x][(s&-s).bit_length() -1]
            if op == 1:
                ans += mu[S[s]] * ID[S[s]]
                ID[S[s]] +=1
            else:
                ID[S[s]] -=1
                ans -=mu[S[s]] * ID[S[s]]
        

    def MoAlgo(nums,query):
        n = len(nums)
        q = len(query)
        block_size = int(math.sqrt(n)) +1

        qIndex = [(*query,i) for i,query in enumerate(query)]

        def mo_cmp(query):
            li,ri, = query[0],query[1] 
            block = li // block_size
            if block %2 == 0:
                return (block,ri)
            else:
                return (block,-ri)
        qIndex.sort(key=mo_cmp)


        cur_li,cur_ri = 0, 0

        ret = [-1] *q
        modify(0,1)
        for li, ri, idx in qIndex:
            while cur_li < li:
                deal(numsIdx[cur_li],numsIdx[cur_li +1],numsIdx[cur_ri])
                cur_li +=1
            while cur_li > li:
                deal(numsIdx[cur_li],numsIdx[cur_li -1],numsIdx[cur_ri])
                cur_li -=1
            while cur_ri > ri:
                deal(numsIdx[cur_ri],numsIdx[cur_ri -1],numsIdx[cur_li])
                cur_ri -=1
            while cur_ri < ri:
                deal(numsIdx[cur_ri],numsIdx[cur_ri +1],numsIdx[cur_li])
                cur_ri +=1
           
            
            ret[idx] = sz*(sz -1) //2 + ans
        return ret
   
    ret =MoAlgo(numsIdx,query)
    return ret

ret = CoPrimeQuery(T,querys)
for a in ret:
    print(a)
