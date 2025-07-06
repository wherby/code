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


from math import ceil, log2

@cache
def gcd1(a,b):
    return math.gcd(a,b)

class segment_tree:
    # merge(left, right): function used to merge the two halves
    # basef(value): function applied on individual values
    # basev: identity for merge function, merger(value, basev) = value 
    # update(node_value, old, new): function to update the nodes
    def __init__(self, array, merge=lambda x,y:gcd1(x,y), basev = 0, basef=lambda x:x):
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
    @cache
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
    def minStable(self, nums: List[int], maxC: int) -> int:
        t1 =len([a for a in nums if a != 1])
        if t1 -maxC <=0:
            return 0
        n = len(nums)
        dic ={}
        st = segment_tree(nums)
        lstl = 0
        for i in range(n):
            if nums[i]!=1:
                l,r = lstl,i 
                while l<r:
                    md = (l+r)>>1
                    if st.query(md,i) ==1:
                        l= md+1 
                    else:
                        r = md
                dic[i] = l
                lstl = l
            else:
                dic[i] = i 
                lstl = i

        #print(dic)
        def verify(md,c):
            lst = -1
            for i in range(n):
                if min(i- dic[i] +1,i-lst) > md:
                    if c:
                        c -=1
                        lst =i
                    else:
                        return False
            return True
        l ,r  = 0, n+1
        while l < r:
            md = (l+r)>>1
            #rint(md,verify(md,maxC))
            if verify(md,maxC):
                r = md 
            else:
                l = md +1
        return l



from input import nums

re =Solution().minStable(nums,maxC = 0)
print(re)