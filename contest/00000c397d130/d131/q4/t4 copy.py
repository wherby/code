from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

from bisect import bisect_right,insort_left,bisect_left
from queue import Queue,LifoQueue,PriorityQueue
import math
INF  = math.inf
from itertools import pairwise


from math import ceil, log2

class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:x+y, basev = 0, basef=lambda x:x):
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.n = len(array)
        self.array = array
        self.tree = [0] * ( 2**ceil(log2(len(array))+1) - 1 )
        self.build(array)
    
    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if(l==r):
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l+r)//2
        self.tree[i] = self.merge(self._build_util(l,mid, 2*i+1, a), self._build_util(mid+1, r, 2*i+2, a))
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a)-1, 0, a)

    def _query_util(self, i, ln, rn, l, r):
        if ln>=l and rn<=r:
            return self.tree[i]
        if ln>r or rn<l:
            return self.basev
        return self.merge( self._query_util( 2*i+1, ln, (ln+rn)//2, l, r ), self._query_util( 2*i+2, (ln+rn)//2+1, rn, l, r ) )

    def query(self, l, r):
        return self._query_util( 0, 0, self.n-1, l, r )

    def _update_util(self, i, ln, rn, x, v):
        if x>=ln and x<=rn:
            if ln != rn:
                self._update_util( 2*i+1, ln, (ln+rn)//2, x, v )
                self._update_util( 2*i+2, (ln+rn)//2 + 1, rn, x, v )
                self.tree[i] = self.merge(self.tree[2*i+1], self.tree[2*i+2])
            else:
                self.tree[i] = self.basef(v)

    def update(self, x, v):
        self._update_util( 0, 0, self.n-1, x, v )   
        self.array[x] =v     
        
class DSU:
    def __init__(self,N,rk):
        self.p  = list(range(N))
        self.rank = rk
    
    def find(self,x):
        #print(x,self.p,self.rank)
        if self.p[x] != x:
            self.p[x] =self.find(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        xr = self.find(x)
        yr = self.find(y)
        if xr < yr:
            xr,yr =yr,xr
        self.p[yr] = xr
        self.rank[xr] += self.rank[yr]

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx =0
        qs = queries[::-1]
        xs =set([0])
        for q in qs:
            if q[0] ==1:
                xs.add(q[1])
        xs.add(10**20)
        xs = list(xs)
        xs.sort()
        st =[0]
        rk=[0]
        for a,b in pairwise(xs):
            mx = max(mx,b-a)
            rk.append(b-a)
            st.append(b-a)
        
        dsu = DSU(len(xs),rk)
        #print(st)
        Seg = segment_tree(st,merge=max)
        dic = {}
        for i,a in enumerate(xs):
            dic[a] = i
        ret =[]
        for q in qs:
            if q[0] ==2:
                x,d = q[1],q[2]
                k = bisect_left(xs,x)
                #print(k,dsu.find(k),dsu.rank)
                b = dsu.find(k)
                #print(x,d,b,dsu.rank,xs[b],x,xs)
                t = xs[b] - dsu.rank[b]
                k = bisect_left(xs,t)
                

                #print(xs,k,x,st,Seg.query(0,k),b,dsu.rank)
                #print(x - xs[k] >= d, Seg.query(0,k)>=d,d,x,xs[k],k)
                if x - xs[k] >= d or Seg.query(0,k)>=d:
                    ret.append(True)
                else:
                    ret.append(False)
            else:
                x = q[1]
                k= bisect_left(xs,x)
                #print(k,xs,x)

                a,b = dsu.find(k+1),dsu.find(k)
                #print(a,b)
                if a != b:
                    #print(dsu.rank)
                    dsu.union(a,b)
                    Seg.update(dsu.find(k),dsu.rank[dsu.find(k)])
                    #print(dsu.rank)
            
        return ret[::-1]
                


re =Solution().getResults(queries =  [[1,2],[2,3,3],[2,3,1],[2,2,2]])
print(re)
re =Solution().getResults(queries =   [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]])
print(re)
re =Solution().getResults(queries =  [[2,2,12],[2,11,12],[1,7],[2,2,9]])
print(re)
