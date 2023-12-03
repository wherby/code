from typing import List, Tuple, Optional
# common include
from typing import List, Tuple, Optional
from collections import defaultdict,deque
import functools
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from bisect import bisect_right,insort_left,bisect_left


class Node:
    __slots__ = ('isTracked','value', 'lazy', 'left', 'right')

    def __init__(
        self,
        isTracked=0,  
        value =0,
        lazy=False,
        left: Optional['Node'] = None,
        right: Optional['Node'] = None,
    ) -> None:
        self.isTracked = isTracked
        self.value = value
        self.lazy = lazy
        self.left = left
        self.right = right


class SegmentTree:
    ## ret value is used for merge function for query, if need to find min value , set ret to max(10**9) else (-10**9)
    def __init__(self,merge=lambda x,y:x+y, basev = 0, basef=lambda x:x,ret=10**9) -> None:
        self._root = Node()
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.MINV = 0
        self.MAXV = int(1e9 + 10) ## node's max value
        self.ret = ret

    def update(self, left: int, right: int, delta: bool) -> None:
        self._update(left, right, self.MINV, self.MAXV, self._root, delta)

    def query(self, left: int, right: int) -> bool:
        return self._query(left, right, self.MINV, self.MAXV, self._root)

    def _update(self, L: int, R: int, l: int, r: int, root: Node, delta: bool) -> None:
        self._pushDown(root,l,r)
        if r < L or R <l:
            return
        if L <= l <= r <= R:
            # applied the delta to current node to update value and set lazy flag
            root.isTracked += delta
            root.lazy = True
            self._pushDown(root,l,r)
            return
        
        
        mid = (l + r) >> 1
        #if L <= mid: Bug version  algorithm\segmentTree\lazyEval\WrongCode1\segmentTreeWithFuctionWithLazyEval.py
        self._update(L, R, l, mid, root.left, delta)
        #if R >= mid + 1:
        self._update(L, R, mid + 1, r, root.right, delta)
        self._pushUp(root)

    def _query(self, L: int, R: int, l: int, r: int, root: Node) -> bool:
        self._pushDown(root,l,r)
        if L <= l <= r <= R:
            return root.value
        mid = (l + r) >> 1
        res = self.ret
        if L <= mid:
            res =self.merge(res, self._query(L, R, l, mid, root.left))
        if R >= mid + 1:
            res = self.merge(res,self._query(L, R, mid + 1, r, root.right))
        return res

    def _pushUp(self, root: Node) -> None:
        root.value = self.merge(root.left.value,root.right.value)

    def _pushDown(self, root: Node,l,r) -> None:
        if not root.left:
            root.left = Node()
        if not root.right:
            root.right = Node()
        if root.lazy:
            # push down change and update the left and right node with pushDown value
            # and set flag
            if l != r:
                root.left.lazy = root.right.lazy = True
                root.left.isTracked = root.left.isTracked +root.isTracked
                root.right.isTracked = root.right.isTracked+root.isTracked
            root.lazy = False
            root.value += root.isTracked
            root.isTracked =0

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        ls = list(zip(nums1,nums2))
        ls.sort()
        qs = []
        for i,(a,b) in enumerate(queries):
            qs.append((a,b,i))
        qs.sort(reverse = True)
        MX = 10**9
        ret = [-1] * len(queries)
        st = SegmentTree(merge=max,basev=0,ret =0)
        for x,y, i in qs:
            while ls and ls[-1][0]>=x:
                a,b = ls.pop()
                c = st.query(b,b)
                if a+b > c:
                    st.update(b,b,a+b-c)
            d = st.query(y,MX)
            if d >0:
                ret[i] =d 
        return ret

re =Solution().maximumSumQueries(nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]])
print(re)