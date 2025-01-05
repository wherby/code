# https://leetcode.cn/problems/minimum-cost-to-split-an-array/
# https://leetcode.cn/problems/minimum-cost-to-split-an-array/solution/by-endlesscheng-05s0/
# https://leetcode.cn/problems/minimum-cost-to-split-an-array/submissions/
# Wrong ans for https://leetcode.cn/contest/weekly-contest-431/problems/maximum-coins-from-k-consecutive-bags/submissions/591207377/
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
        self.MAXV = int(1e9 + 10) ## node's max value
        self.ret = ret

    def update(self, left: int, right: int, delta: bool) -> None:
        self._update(left, right, self.MINV, self.MAXV, self._root, delta)

    def query(self, left: int, right: int) -> bool:
        return self._query(left, right, self.MINV, self.MAXV, self._root)

    def _update(self, L: int, R: int, l: int, r: int, root: Node, delta: bool) -> None:
        if L <= l <= r <= R:
            # applied the delta to current node to update value and set lazy flag
            root.isTracked += delta  
            root.lazy = True
            root.value +=delta*(r-l+1) ## need change if not sum
            return

        self._pushDown(root)
        mid = (l + r) >> 1
        if L <= mid:
            self._update(L, R, l, mid, root.left, delta)
        if R >= mid + 1:
            self._update(L, R, mid + 1, r, root.right, delta)
        self._pushUp(root)

    def _query(self, L: int, R: int, l: int, r: int, root: Node) -> bool:
        self._pushDown(root)
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

    def _pushDown(self, root: Node) -> None:
        if not root.left:
            root.left = Node()
        if not root.right:
            root.right = Node()
        if root.lazy:
            # push down change and update the left and right node with pushDown value
            # and set flag
            root.left.lazy = root.right.lazy = True
            root.left.isTracked = root.left.isTracked +root.isTracked
            root.right.isTracked = root.right.isTracked+root.isTracked
            root.lazy = False
            root.left.value += root.isTracked
            root.right.value += root.isTracked
            root.isTracked =0
            

class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        sgt = SegmentTree(ret=0)
        for f,t,c in coins:
            sgt.update(f,t,c)
        
        ret = 0
        for f,t,c in coins:
            t1 = f+k-1
            ret = max(ret,sgt.query(f,t1))
            #print(sgt.query(f,t1),f,t1)
            f1 =t-k+1
            ret = max(ret,sgt.query(f1,t))
        return ret
            





#re =Solution().maximumCoins(coins = [[30,49,12]], k = 28)
re =Solution().maximumCoins(coins =[[21,23,10],[43,45,12],[1,11,1],[48,50,6],[14,16,11],[19,20,14],[29,33,18]], k = 28)
print(re,187)