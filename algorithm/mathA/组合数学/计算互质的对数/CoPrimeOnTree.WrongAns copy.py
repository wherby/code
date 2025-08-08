# https://www.hackerrank.com/contests/w27/challenges/coprime-paths/problem
# 用DFSN计算非线性的树上莫队
# 结果是错误的
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
filename = "./input/input00.txt"
f=open(filename,'r')

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys

if  "f" in locals():
    inputA=f
else:
    inputA=sys.stdin


ins=[]
for line in inputA:
    ins.append(line)



class DFSTraverser:
    """
    一个用于执行深度优先搜索并记录欧拉环游路径的类。
    """
    def __init__(self, adjacency_list):
        self.n = len(adjacency_list)
        self.Vec = adjacency_list
        self.Fa = {} # 存储父节点
        self.T = [] # 存储遍历序列
        self.depth = 0
        self.L = [-1]*self.n 
        self.R = [-1]*self.n
        self.compute()
    
    def compute(self):
        self.dfs(0,-1)
        for i in range(self.depth ):
            
            if self.L[self.T[i]] == -1:
                self.L[self.T[i]] = i 
            self.R[self.T[i]] = i

    def dfs(self, z, fa):
        """
        递归执行深度优先搜索。
        :param z: 当前节点
        :param fa: 当前节点的父节点
        """
        
        self.T.append(z)
        self.depth += 1
        # 遍历当前节点的所有邻居
        for d in self.Vec[z]:
            if d == fa:
                continue
            
            self.Fa[d] = z
            self.dfs(d, z)
        self.T.append(z)
        self.depth += 1


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
for i in range(index,index + Q):
    a,b =map(int , ins[i].strip().split())
    a,b = a-1,b-1
    querys.append((a,b))

dft = DFSTraverser(edges)
T,L,R =dft.T,dft.L,dft.R
print(T,L,R)
query2= []
for a,b in querys:
    if L[a]>L[b]:
        a,b = b,a 
    print(a,b,"qq")
    if R[a] > L[b]:
        query2.append((L[a],L[b]))
    else:
        query2.append((R[a],L[b]))
    print(query2[-1])


import math
def prepare(M):
    # 初始化数组
    mu = [1] * M  # 莫比乌斯函数
    F = [0] * M   # 最小质因子
    q = []        # 存储质数
    
    mu[1] = 1     # 规定mu[1] = 1
    
    for i in range(2, M):
        if not F[i]:  # i是质数
            F[i] = i
            q.append(i)
            mu[i] = -1  # 质数的mu值为-1
        
        # 用当前已筛出的质数q[j]去标记合数i*q[j]
        for p in q:
            if i * p >= M:
                break
            F[i * p] = p  # 合数i*p的最小质因子是p
            if i % p == 0:
                mu[i * p] = 0  # i*p包含平方因子p^2
                break
            else:
                mu[i * p] = -mu[i]  # 根据mu的定义更新
    
    return mu, F, q

# 示例调用
M = 10**5+1  # 假设上限为20
mu, F, primes = prepare(M)

def CoPrimeQuery(numsIdx,query):
    numsInT = [nums[a] for a in numsIdx]
    n = len(numsInT)
    print(n,numsInT,"b")
    ID = [-1]*M  
    p = [[] for _ in range(n)]
    ret = [-1]*len(query)
    for i,a in enumerate(nums):
        x = a 
        while x >1:
            f = F[x]
            if ID[f] != i :  #用ID 的值来记录循环idx,避免记录重复的质数
                ID[f] =  i 
                p[i].append(f)
            x //=f 
    ID =[0]*M
    ans = 0
    sz = 0
    S = [0]*M 
    S[0] =1
    FOP = [1]*n
    def modify(x,op):
        nonlocal ans,sz
        print("modify:",(x,op))
        if FOP[T[x]] ==1:
            FOP[T[x]] = -1
        else:
            FOP[T[x]] = 1 
            op = -op
        sz +=op 
        print(x,op,p,ans,sz,ID[:10])
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


        cur_li,cur_ri = 0, -1

        ret = [-1] *q

        for li, ri, idx in qIndex:
            print(li,ri,idx,"CCCC",sz)
            while cur_li > li:
                cur_li -=1
                modify(cur_li,1)
            while cur_ri < ri:
                cur_ri +=1
                modify(cur_ri,1)
            while cur_li < li:
                modify(cur_li,-1)
                cur_li +=1
            while cur_ri > ri:
                modify(cur_ri,-1)
                cur_ri -=1
            ret[idx] = sz*(sz -1) //2 + ans
            print(idx,sz,ans, ret[idx],"X1")
        return ret
   
    ret =MoAlgo(numsIdx,query)
    return ret
#num2 = [nums[a] for a in T]
#print(num2,"aa")
ret = CoPrimeQuery(T,query2)
print(ret)
