from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

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
    def __init__(self,merge=lambda x,y:x+y, basev = 0, basef=lambda x:x,ret=0) -> None:
        self._root = Node()
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.MINV = 0
        self.MAXV = int(1e9 + 10) ## node's max value could be change to N(the array length)
        self.ret = ret

    def update(self, left: int, right: int, delta: bool) -> None:
        self._update(left, right, self.MINV, self.MAXV, self._root, delta)

    def query(self, left: int, right: int) -> bool:
        return self._query(left, right, self.MINV, self.MAXV, self._root)

    def _update(self, L: int, R: int, l: int, r: int, root: Node, delta: bool) -> None:
        if L <= l <= r <= R:
            root.isTracked += delta
            root.lazy = True
            ## need to be changed
            # applied the delta to current node to update value and set lazy flag.
            root.value +=delta
            return

        self._pushDown(root,l,r)
        mid = (l + r) >> 1
        if L <= mid:
            self._update(L, R, l, mid, root.left, delta)
        if R >= mid + 1:
            self._update(L, R, mid + 1, r, root.right, delta)
        self._pushUp(root)

    def _query(self, L: int, R: int, l: int, r: int, root: Node) -> bool:
        if L <= l <= r <= R:
            return root.value

        self._pushDown(root,l,r)
        mid = (l + r) >> 1
        ## ## need to be changed, how to merge left,right value 
        ## set the initial res value for merge
        res = self.ret
        if L <= mid:
            res =self.merge(res, self._query(L, R, l, mid, root.left))
        if R >= mid + 1:
            res = self.merge(res,self._query(L, R, mid + 1, r, root.right))
        return res

    def _pushUp(self, root: Node) -> None:
        ## ## need to be changed, how to merge left,right value
        root.value = self.merge(root.left.value,root.right.value)

    def _pushDown(self, root: Node,l,r) -> None:
        if not root.left:
            root.left = Node()
        if not root.right:
            root.right = Node()
        if root.lazy:
            ## need to be changed
            # push down change and update the left and right node with pushDown value
            # and set flag
            root.left.lazy = root.right.lazy = True
            root.left.isTracked = root.left.isTracked +root.isTracked
            root.right.isTracked = root.right.isTracked+root.isTracked
            root.lazy = False
            ## ## need to be changed, of how to applied the tracked value
            root.left.value += root.isTracked
            root.right.value += root.isTracked
            root.isTracked =0

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        st = SegmentTree(merge=max)
        mx = 0
        for i in range(n):
            a,b = nums1[i],nums2[i]
            ac,bc = st.query(0,a),st.query(0,b)
            mx = max(mx,ac+1,bc+1)
            if a != b:
                st.update(a,a,1)
                st.update(b,b,1)
            else:
                st.update(a,a,1)
            print(ac,bc,a,b,i,mx)
        return mx
        




re =Solution().maxNonDecreasingLength(nums1 = [1,3,2,1], nums2 = [2,2,3,4])
print(re)