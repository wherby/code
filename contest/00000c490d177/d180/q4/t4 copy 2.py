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
import functools

class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        n = len(nums1)
        mod = 10**9+7
        ls = []
        for i in range(n):
            a,b = nums1[i],nums0[i]
            ls.append((a,b))
        def compare(f1, f2):
            u1, v1 = f1
            u2, v2 = f2
            if v1 == 0:
                return -1 
            elif v2 == 0:
                return 1
            elif u1 ==u2:
                if v1 < v2:
                    return -1 
                elif v1 > v2:
                    return 1
                else:
                    return 0 
            elif u1 > u2 :
                return -1 
            else:
                return 1


        ls.sort(key=functools.cmp_to_key(compare))
        ans = 0
        for u, v in ls:
            length = u + v
            segment_val = (pow(2, u, mod) - 1) * pow(2, v, mod) % mod
            ans = (ans * pow(2, length, mod) + segment_val) % mod
            
        return ans
            





nums1 = [1,1038,1,3725,6296,2962,4,2930,7976,5,1,8612,1363,4011,251,1321,831,7334,16,114,3784,9467,814,88,4318,3230]
nums0 = [0,10000,0,10000,6707,10000,1,10000,9765,126,16,7051,2746,9435,8604,5148,1054,913,1,2810,2756,800,5236,7699,9286,9353]

re =Solution().maxValue(nums1,nums0)
print(re)