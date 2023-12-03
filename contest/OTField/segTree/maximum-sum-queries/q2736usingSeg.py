from typing import List, Tuple, Optional
# common include
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left

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

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        ls = list(zip(nums1,nums2))
        ls.sort()
        qs = []
        for i,(a,b) in enumerate(queries):
            qs.append((a,b,i))
        qs.sort(reverse = True)
        ret = [-1] * len(queries)
        n2s = list(set(nums2))
        n2s.sort()
        n2d = {k:v for v,k in enumerate(n2s)}
        m = len(n2s)
        arr = [-1]*m
        st = segment_tree(arr, merge=max)
        for x,y, i in qs:
            while ls and ls[-1][0]>=x:
                a,b = ls.pop()
                c = st.array[n2d[b]]
                if a+b > c:
                    #print(a+b,n2d[b],st.array)
                    st.update(n2d[b],a+b)
            try:
                k = bisect_left(n2s,y)
                #print(n2s,y,k,st.query(n2s[k],m-1),m-1)
                if k <m:
                    d = st.query(k,m-1)
                    if d >0:
                        ret[i] =d 
            except:
                print(y)
        return ret


import time
from testInput import *
start = time.time()
#re =Solution().maximumSumQueries(nums1 , nums2 ,queries )
re =Solution().maximumSumQueries(nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]] )
print(re)
end = time.time()
print(end - start)