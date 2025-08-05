# 莫队算法 
# 离线概率统计
# https://leetcode.cn/contest/biweekly-contest-162/problems/threshold-majority-queries/submissions/649281456/
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




from collections import defaultdict



class Solution:
    def subarrayMajority(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q = len(queries)
        block_size = int(math.sqrt(n)) + 1

        queries_with_index = [(li, ri, threshold, i) for i, (li, ri, threshold) in enumerate(queries)]

        def mo_cmp(query):
            li, ri, _, idx = query
            block = li // block_size
            if block % 2 == 0:
                return (block, ri)
            else:
                return (block, -ri)
        queries_with_index.sort(key=mo_cmp)

        freq = defaultdict(int)
        current_li, current_ri = 0, -1  # current interval is [current_li, current_ri]
        ans = [-1] * q

        for li, ri, threshold, original_idx in queries_with_index:
            # Move current_li to li
            while current_li > li:
                current_li -= 1
                num = nums[current_li]
                freq[num] += 1
            while current_ri < ri:
                current_ri += 1
                num = nums[current_ri]
                freq[num] += 1
            while current_li < li:
                num = nums[current_li]
                freq[num] -= 1
                if freq[num] == 0:
                    del freq[num]
                current_li += 1
            while current_ri > ri:
                num = nums[current_ri]
                freq[num] -= 1
                if freq[num] == 0:
                    del freq[num]
                current_ri -= 1
            
            max_freq = -1
            candidate = -1
            for num, count in freq.items():
                if count >= threshold:
                    if count > max_freq:
                        max_freq = count
                        candidate = num
                    elif count == max_freq:
                        if num < candidate:
                            candidate = num
            ans[original_idx] = candidate

        return ans




re =Solution().subarrayMajority(nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]])
print(re)