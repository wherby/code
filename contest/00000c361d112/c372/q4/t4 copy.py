from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf

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
        self.qr = -1
    
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

    def query(self, l, r,value):
        self.qr =-1
        return self._query_util( 0, 0, self.n-1, l, r,value )

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

class Solution:
    def leftmostBuildingQueries(self, hs: List[int], queries: List[List[int]]) -> List[int]:
        sg = segment_tree(hs,merge=max)
        n = len(hs)
        st = []
        rmx = [-1]*n
        for i,a in enumerate(hs):
            while st and st[-1]<a:
                rmx[st[-1]]=i
                st.pop()
            st.append(i)
        ret = [-1]*len(queries)
        for idx,(a,b) in enumerate(queries):
            a,b = min(a,b),max(a,b)
            if hs[a]<hs[b]:
                ret[idx] = b 
            elif a ==b:
                ret[idx] = a 
            else:
                
                l,r = b+1,n-1
                if sg.query(l,r)<= hs[a]:
                    continue
                while l<r:
                    mid = (l+r)>>1
                    if sg.query(l,mid)<=hs[a]:
                        l = mid+1
                    else:
                        r=mid 
                ret[idx] = l
        return ret





re =Solution().leftmostBuildingQueries(hs = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]])
print(re)