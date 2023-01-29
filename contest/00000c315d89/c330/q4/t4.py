from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from sortedcontainers import SortedDict,SortedList


# # https://leetcode-cn.com/problems/range-sum-query-mutable/submissions/   verified time cost more than  setmentTreeImpl2.py
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
    def countQuadruplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        ls = [0]*(n+1)
        st = segment_tree(ls)
        sm = 0
        ls2 = [0]*(n+1)
        st2 = segment_tree(ls2)
        sl = SortedList([])
        sl2 = SortedList([i for i in range(1,n+1)])
        for i,a in enumerate(nums):
            t= sl.bisect_left(a)
            tk = st2.query(a+1,n)
            st2.update(a,st2.array[a]+t)
            st.update(a,st.array[a] +tk)
            sm += st.query(0,a-1)
            sl.add(a)
            print(i,a,sm,sl,st.array)
        return sm




re =Solution().countQuadruplets([1,3,2,4,5])
re =Solution().countQuadruplets([2,5,3,1,4])
print(re)