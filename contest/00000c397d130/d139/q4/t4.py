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

    def query(self, left: int, right: int):
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
    
    def queryFirst(self,target):
        left =0
        right =self.MAXV+1
        while left < right:
            mid = (left + right)>>1
            if self.query(0,mid)<target:
                left=mid+1
            else:
                right = mid 
        if left ==self.MAXV+1:
            left = -1
        return left 
    
    def queryFirst2(self,target):
        node = self._root
        l,r = self.MINV,self.MAXV
        while l <r:
            if node.isTracked <target:
                return -1
            mid = (l + r) >> 1
            self._pushDown(node)
            if node.left.isTracked < target:
                node = node.right
                l,r = mid + 1, r
            else:
                node = node.left
                l,r = l,mid
        return l


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
            seg = SegmentTree(merge=max)
            ret = 0
            key =sorted(dic.keys())
            for k in key:
                ls = dic[k]
                ls= list(set(ls))
                ls.sort(reverse=True)
                for b in ls:
                    c = seg.query(0,b-1)
                    d = seg.query(0,b)
                    if c==d:
                        seg.update(b,c,1)
                    ret =max(ret,c+1)
            return ret
        return getNum(lls1) + getNum(lls2)-1







re =Solution().maxPathLength(coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1)
print(re)