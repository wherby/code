# https://leetcode.cn/problems/range-module/solution/python-dong-tai-kai-dian-xian-duan-shu-b-jrrs/
# https://leetcode.cn/problems/range-module/
from typing import Optional


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




class Solution(object):
    def lengthOfLIS(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mx=0
        st = SegmentTree(merge=max,basev=0)
        for a in nums:
            m= st.query(a-k,a-1)
            #print(m,a,mx)
            st.update(a,a,m+1)
            mx = max(mx,m+1)
        return mx
re =Solution().lengthOfLIS(nums = [4,2,1,4,3,4,5,8,15], k = 3)
print(re)