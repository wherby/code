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
            root.isTracked = delta
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
        res = True
        if L <= mid:
            res =self.merge(res, self._query(L, R, l, mid, root.left))
        if R >= mid + 1:
            res = self.merge(res,self._query(L, R, mid + 1, r, root.right))
        return res

    def _pushUp(self, root: Node) -> None:
        root.isTracked = (
            root.left and root.left.isTracked and root.right and root.right.isTracked
        )

    def _pushDown(self, root: Node) -> None:
        if not root.left:
            root.left = Node(isTracked=self.basev)
        if not root.right:
            root.right = Node(isTracked=self.basev)
        if root.lazy:
            root.left.lazy = root.right.lazy = True
            root.left.isTracked = root.right.isTracked = root.isTracked
            root.lazy = False


class RangeModule:
    def __init__(self):
        self.tree = SegmentTree(merge=lambda a,b:a and b,basev=False)

    def addRange(self, left: int, right: int) -> None:
        """添加 半开区间 [left, right)"""
        self.tree.update(left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        """ 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true"""
        return self.tree.query(left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        """ 停止跟踪 半开区间 [left, right)"""
        self.tree.update(left, right - 1, False)


rm = RangeModule()
rm.addRange(4,10)
print(rm.queryRange(4,6))
print(rm.queryRange(2,6))