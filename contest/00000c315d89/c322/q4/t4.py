from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList
class DSU:
    def __init__(self,N):
        self.p  = list(range(N))
        self.rank = [1]*N
    
    def find(self,x):
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if self.rank[xr] <self.rank[yr]:
            xr,yr =yr,xr
        
        self.p[yr] = xr
        if self.rank[xr] == self.rank[yr]:
            self.rank[xr] += 1


class Solution(object):
    def magnificentSets(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        g = [[] for _ in range(n+1)]
        dsu = DSU(n+1)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
            dsu.union(a,b)
        mx = -1
        dic = defaultdict(list)
        for i in range(1,n+1):
            dic[dsu.find(i)].append(i)
        sg = defaultdict(list)
        for a,b in edges:
            sg[dsu.find(a)].append([a,b])
        def bfs(i,sg):
            ind = [-1]*(n+1)
            visit={}
            st =deque([i])
            cnt =0
            acc =0
            while st:
                tmp =set([])
                cnt +=1
                for a in st:
                    if a in visit:continue
                    acc +=1
                    visit[a] =1
                    ind[a] = cnt
                    for b in g[a]:
                        if b in visit:continue
                        tmp.add(b)
                st = tmp
            #print(i,cnt,acc)
            for a,b in sg:
                if abs(ind[a]- ind[b] ) !=1 :
                    #print("aa")
                    return -1 
            return cnt
        vv = {}
        acc =0
        #print(dic)
        for i in range(1,n+1):
            k1 = dsu.find(i)
            if k1 in vv: continue
            else:
                vv[k1] = 1
                cand = dic[k1]
                mx = -1
                for a in cand:
                    mx = max(mx,bfs(a,sg[k1]))
                if mx == -1:
                    return -1
                acc +=mx
        return acc




n=92
edges=[[67,29],[13,29],[77,29],[36,29],[82,29],[54,29],[57,29],[53,29],[68,29],[26,29],[21,29],[46,29],[41,29],[45,29],[56,29],[88,29],[2,29],[7,29],[5,29],[16,29],[37,29],[50,29],[79,29],[91,29],[48,29],[87,29],[25,29],[80,29],[71,29],[9,29],[78,29],[33,29],[4,29],[44,29],[72,29],[65,29],[61,29]]
#re =Solution().magnificentSets(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]])
#re =Solution().magnificentSets(n , edges )
n=26
edges=[[9,16],[8,3],[20,21],[12,16],[14,3],[7,21],[22,3],[22,18],[11,16],[25,4],[2,4],[14,21],[23,3],[17,3],[2,16],[24,16],[13,4],[10,21],[7,4],[9,18],[14,18],[14,4],[14,16],[1,3],[25,18],[17,4],[1,16],[23,4],[2,21],[5,16],[24,18],[20,18],[19,16],[24,21],[9,3],[24,3],[19,18],[25,16],[19,21],[6,3],[26,18],[5,21],[20,16],[2,3],[10,18],[26,16],[8,4],[11,21],[23,16],[13,16],[25,3],[7,18],[19,3],[20,4],[26,3],[23,18],[15,18],[17,18],[10,16],[26,21],[23,21],[7,16],[8,18],[10,4],[24,4],[7,3],[11,18],[9,4],[26,4],[13,21],[22,16],[22,21],[20,3],[6,18],[9,21],[10,3],[22,4],[1,18],[25,21],[11,4],[1,21],[15,3],[1,4],[15,16],[2,18],[13,3],[8,21],[13,18],[11,3],[15,21],[8,16],[17,16],[15,4],[12,3],[6,4],[17,21],[5,18],[6,16],[6,21],[12,4],[19,4],[5,3],[12,21],[5,4]]
re =Solution().magnificentSets(n , edges )
#re =Solution().magnificentSets(30,[[16,8],[6,5]])
print(re)