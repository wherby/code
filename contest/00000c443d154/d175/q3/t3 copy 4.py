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


from typing import List

# 针对 Python 性能优化的快捷 max
def fmax(a, b):
    return a if a > b else b

class BIT:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i: int, val: int):
        i += 1
        while i <= self.n:
            if val > self.tree[i]:
                self.tree[i] = val
            else:
                break
            i += i & (-i)

    def query(self, i: int) -> int:
        i += 1
        res = 0
        while i > 0:
            if self.tree[i] > res:
                res = self.tree[i]
            i -= i & (-i)
        return res



class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ret = 0
        

        for bit in range(30):
            ls = [a for a in nums if (a >> bit) & 1]
            
            if not ls:
                continue
                

            ns = sorted(set(ls))
            if len(ns) <= ret:
                continue
                
            m = len(ns)
            index_map = {v: i for i, v in enumerate(ns)}

            bit_tree = BIT(m)
            
            for a in ls:
                idx = index_map[a]
                curM = bit_tree.tree[idx + 1]
                prev_best = bit_tree.query(idx - 1)
                if prev_best + 1 > curM:
                    bit_tree.update(idx, prev_best + 1)

            bit_max = bit_tree.query(m - 1)
            if bit_max > ret:
                ret = bit_max
                
        return ret





re =Solution().longestSubsequence([5,4,7])
print(re)