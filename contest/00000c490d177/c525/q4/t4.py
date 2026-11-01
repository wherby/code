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

class Solution:
    def countStaircase(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        lls = defaultdict(deque)
        for i, a in enumerate(nums):
            lls[a].append(i)

        vls = []
        t_idx = 1
        while True:
            t = (t_idx + 1) * t_idx // 2
            if t > n:
                break
            vls.append(t)
            t_idx += 1

        firstLs = SortedList([])
        for val, indices in lls.items():
            firstLs.add((indices[0], val))


        for i in range(n):
            break_outer_k1 = False

            for k1_idx, length in enumerate(vls):
                if break_outer_k1:
                    break

                k1 = k1_idx + 1
                if k1 > len(firstLs):
                    break

                sub_end = i + length - 1
                if sub_end >= n:
                    break

                isGood = True
                for j, (first_pos, val) in enumerate(firstLs[:k1]):
                    ridx = bisect_right(lls[val], sub_end)

                if ridx > j + 1:

                    break_outer_k1 = True
                    isGood = False
                    break
                elif ridx < j + 1:

                    isGood = False


                if isGood:
                    ans += 1
            val_i = nums[i]
            if lls[val_i] and lls[val_i][0] == i:
                firstLs.remove((i, val_i))
                lls[val_i].popleft()
                if lls[val_i]:
                    firstLs.add((lls[val_i][0], val_i))

        return ans






re =Solution().countStaircase([5,8,8,2,2,2])
print(re)