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


from typing import List, Tuple, Optional
class Node:
    def __init__(self, l, r,v =0):
        self.left = None
        self.right = None
        self.l = l
        self.r = r
        self.mid = (l + r) >> 1
        self.v = v*(r-l+1)
        self.add = 0


class SegmentTree:
    def __init__(self):
        self.root = Node(0, int(1e9))

    def modify(self, l, r, v, node=None):
        if l > r:
            return
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            node.v = v*(r-l+1)
            node.add = v
            return
        self.pushdown(node)
        if l <= node.mid:
            self.modify(l, r, v, node.left)
        if r > node.mid:
            self.modify(l, r, v, node.right)
        self.pushup(node)

    def query(self, l, r, node=None):
        if l > r:
            return 0
        if node is None:
            node = self.root
        if node.l >= l and node.r <= r:
            return node.v
        self.pushdown(node)
        v = 0
        if l <= node.mid:
            v = sum([v, self.query(l, r, node.left)])
        if r > node.mid:
            v = sum([v, self.query(l, r, node.right)])
        return v

    def pushup(self, node):
        node.v = sum([node.left.v, node.right.v])

    def pushdown(self, node):
        if node.left is None:
            node.left = Node(node.l, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.r)
        if node.add:
            node.left.v = node.add*(node.left.r -node.left.l +1)
            node.right.v = node.add*(node.right.r -node.right.l +1)
            node.left.add = node.add
            node.right.add = node.add
            node.add = 0


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        sg = SegmentTree()
        for i in range(n-1):
            sg.modify(i,i,1)
        ret=[]
        for a,b in queries:
            sg.modify(a+1,b-1,0)
            ret.append(sg.query(0,n-1))
        return ret


re =Solution().shortestDistanceAfterQueries( n = 5, queries = [[1,4],[2,4]])
print(re)