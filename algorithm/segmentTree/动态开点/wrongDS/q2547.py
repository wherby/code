# https://leetcode.cn/problems/range-module/solution/python-dong-tai-kai-dian-xian-duan-shu-b-jrrs/
# https://leetcode.cn/problems/range-module/

## wrong ans
from typing import List, Tuple, Optional


class Node:
    __slots__ = ('isTracked', 'lazy', 'left', 'right')

    def __init__(
        self,
        isTracked=False,  
        lazy=False,
        left: Optional['Node'] = None,
        right: Optional['Node'] = None,
    ) -> None:
        self.isTracked = isTracked
        self.lazy = lazy
        self.left = left
        self.right = right


class SegmentTree:
    def __init__(self,merge=lambda x,y:x+y, basev = 0, basef=lambda x:x) -> None:
        self._root = Node(isTracked=basev)
        self.merge = merge
        self.basef = basef
        self.basev = basev
        self.MINV = 0
        self.MAXV = int(1e9 + 10) ## node's max value

    def update(self, left: int, right: int, delta: bool) -> None:
        self._update(left, right, self.MINV, self.MAXV, self._root, delta)

    def query(self, left: int, right: int) -> bool:
        return self._query(left, right, self.MINV, self.MAXV, self._root)

    def _update(self, L: int, R: int, l: int, r: int, root: Node, delta: bool) -> None:
        if L <= l <= r <= R:
            root.isTracked = self.merge(root.isTracked,delta)
            root.lazy = True
            return

        self._pushDown(root)
        mid = (l + r) >> 1
        if L <= mid:
            self._update(L, R, l, mid, root.left, delta)
        if R >= mid + 1:
            self._update(L, R, mid + 1, r, root.right, delta)
        self._pushUp(root)

    def _query(self, L: int, R: int, l: int, r: int, root: Node) -> bool:
        if L <= l <= r <= R:
            return root.isTracked

        self._pushDown(root)
        mid = (l + r) >> 1
        res = self.basev
        if L <= mid:
            res =self.merge(res, self._query(L, R, l, mid, root.left))
        if R >= mid + 1:
            res = self.merge(res,self._query(L, R, mid + 1, r, root.right))
        return res

    def _pushUp(self, root: Node) -> None:
        root.isTracked = self.merge(root.left.isTracked,root.right.isTracked)

    def _pushDown(self, root: Node) -> None:
        if not root.left:
            root.left = Node(isTracked=self.basev)
        if not root.right:
            root.right = Node(isTracked=self.basev)
        if root.lazy:
            root.left.lazy = root.right.lazy = True
            root.left.isTracked = self.merge(root.left.isTracked,root.isTracked)
            root.right.isTracked = self.merge(root.right.isTracked,root.isTracked)
            root.lazy = False





from collections import defaultdict,deque
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        ans = 0 
        last = defaultdict(int)
        last2 = defaultdict(int)
        st = SegmentTree(merge=min)
        for i,x in enumerate(nums,1):
            st.update(i,i,ans)
            st.update(last[x]+1,i,-1)
            if last[x]:
                st.update(last2[x]+1,last[x],1)
            ans = k + st.query(1,i)
            last2[x] = last[x]
            last[x] = i 
        #print(ans)
        return ans +len(nums)


#re =Solution().minCost(nums = [1,2,1,2,1,3,3], k = 2)

re =Solution().minCost(nums = [1,2,1,2,1], k = 5)
print(re)