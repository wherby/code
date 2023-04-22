from typing import List, Tuple, Optional

from typing import Optional

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
        self.MAXV = int(5e9 + 10) ## node's max value
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
            root.value +=delta
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
            return root.value

        self._pushDown(root)
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
    def fieldOfGreatestBlessing(self, fs: List[List[int]]) -> int:
        cands = []
        fs = [(a*2,b*2,c ) for a,b,c in fs ]
        for a,b,c in fs:
            cands.append((a-c,0,b-c,b+c))
            cands.append((a+c,1,b-c,b+c))
        cands.sort()
        st = SegmentTree(merge=max)
        ret =0
        for x,op,f,t in cands:
            if op == 0:
                st.update(f,t,1)
            else:
                st.update(f,t,-1)
            mx = st.query(0,st.MAXV)
            ret = max(ret,mx)
        return ret



ls = [[565,34,242],[299,628,870],[724,673,221],[128,267,917],[561,488,696],[341,71,604],[835,92,846],[945,696,973],[554,776,430],[209,134,594],[987,898,282],[819,154,462],[618,946,505],[561,40,677],[602,863,657],[295,83,718],[456,920,939],[94,717,813],[611,946,366],[818,850,85],[395,554,333],[325,700,628],[590,401,119],[248,858,499],[298,723,602],[189,538,646],[194,283,344],[842,535,866],[192,832,195]]
re =Solution().fieldOfGreatestBlessing(ls)
print(re)