from typing import List, Tuple, Optional


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
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        mx = 0
        mmx = max(nums)
        if mmx <0:
            return mmx
        ls = set([])
        for i,a in enumerate(nums):
            ls.add(a-i)
        ls = list(ls)
        ls.sort()
        dic ={}
        for i,a in enumerate(ls):
            dic[a] = i
        lss = [0]*len(ls)
        sg = segment_tree(lss,merge=max)
        for i,a in enumerate(nums):
            if a <=0:continue
            t = dic[a-i]
            tm = sg.query(0,t)
            mx =max(mx,tm + a )
            #if tp < tm+a:
            sg.update(t,tm + a)
            #sg.updateRange(t,n-1,a)
            #print(i,a,mx,tm,0,t)
        return mx


import time
from testInput import *
start = time.time()
re =Solution().maxBalancedSubsequenceSum(nums)
print(re)
end = time.time()
print(end - start)
