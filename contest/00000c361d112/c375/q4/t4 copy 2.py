from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList

import math
INF  = math.inf
from collections import Counter


mod = 10**9 +7
def quickPow(x,y):
    ret =1
    cur = x 
    while y >0:
        if y & 1:
            ret = ret * cur % mod
        cur = cur *cur % mod
        y = y //2
    return ret

from bisect import bisect_right,bisect_left
class Span:
    def __init__(self):
        self.span = []
        
    def add(self,left,right):
        span = self.span
        # 找最左侧的与[left,right]相交的区间[l,r], r大到一定程度才会相交
        lidx = bisect_left(span,left,key=lambda itv:itv[1])
        # 找最右侧的与[left,right]相交的区间[l,r], l大到一定程度才不相交
        ridx = bisect_right(span,right,key=lambda itv:itv[0])
        
        for i in range(lidx,ridx):
            left = min(left,span[i][0])
            right = max(right, span[i][1])
        span[lidx:ridx] = [(left,right)]


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        dic = defaultdict(list)
        for i,a  in enumerate(nums):
            dic[a].append(i)
        n = len(nums)
        span = Span()
        for i in range(n):
            span.add(i,i)
        for vs in dic.values():
            l,r = vs[0],vs[-1]
            #print(l,r)
            span.add(l,r)
        
        return quickPow(2,len(span.span)-1)




re =Solution().numberOfGoodPartitions(nums = [2,4,2,7,4])
print(re)