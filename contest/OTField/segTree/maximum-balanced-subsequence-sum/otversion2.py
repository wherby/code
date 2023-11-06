from testInput import *

from typing import List, Tuple, Optional

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
        self.MAXV = int(2e9 + 10) ## node's max value
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
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        mx = 0
        sg = SegmentTree(merge=max,ret=0)
        start = 10**9+2
        mmx = max(nums)
        if mmx<=0:
            return mmx
        for i,a in enumerate(nums):
            if a <=0:continue
            tm = sg.query(0,start+a-i)
            mx =max(mx,tm + a )
            tp = sg.query(start+a-i,start+a-i)
            if tp < tm+a:
                sg.update(start+a-i,start+a-i,tm+a-tp)
        return mx


import time

start = time.time()
re =Solution().maxBalancedSubsequenceSum(nums)
print(re)
end = time.time()
print(end - start)
