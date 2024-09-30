# https://leetcode.cn/contest/biweekly-contest-139/problems/length-of-the-longest-increasing-path/description/
# 动态开点的setment tree都不能运行 《-- 如果left是0的话
# https://leetcode.cn/contest/biweekly-contest-139/problems/length-of-the-longest-increasing-path/submissions/564946585/
# 动态开点会超时
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
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        lls1,lls2 = [(0,0)],[(0,0)]
        a,b = tuple(coordinates[k])
        for x,y in coordinates:
            if x<a and y <b:
                lls1.append((a-x,b-y))
            if x > a and y > b:
                lls2.append((x-a,y-b))
        #print(lls1,lls2)
        def getNum(lls):
            dic = defaultdict(list)
            for x,y in lls:
                dic[x].append(y)
            seg = SegmentTree(merge=max,basev=0,ret=0)
            ret = 0
            key =sorted(dic.keys())
            for k in key:
                ls = dic[k]
                ls= list(set(ls))
                ls.sort(reverse=True)
                for b in ls:
                    c = seg.query(1,b)
                    d = seg.query(b+1,b+1)
                    #print(c,d,b)
                    if d< c+1:
                        seg.update(b+1,b+1,c+1 -d)
                    ret =max(ret,c+1)
            return ret
        #print(getNum(lls1),getNum(lls2))
        return getNum(lls1) + getNum(lls2)-1







re =Solution().maxPathLength(coordinates = [[2,1],[5,4],[9,8]], k = 0)
print(re)