# Block Decomposition 
# 分块算法， 会Timeout
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
        block_size = int(math.sqrt(n)) + 1
        num_blocks = (n + block_size - 1) // block_size
        
        # Preprocess block frequencies
        block_freq = [defaultdict(int) for _ in range(num_blocks)]
        for i in range(n):
            block_idx = i // block_size
            num = nums[i]
            block_freq[block_idx][num] += 1
        
        ans = []
        for li, ri, threshold in queries:
            block_li = li // block_size
            block_ri = ri // block_size
            
            freq = defaultdict(int)
            
            for block in range(block_li + 1, block_ri):
                for num, cnt in block_freq[block].items():
                    freq[num] += cnt
            
            left_end = min((block_li + 1) * block_size - 1, ri)
            for i in range(li, left_end + 1):
                num = nums[i]
                freq[num] += 1
            
            if block_li != block_ri:
                right_start = max(li, block_ri * block_size)
                for i in range(right_start, ri + 1):
                    num = nums[i]
                    freq[num] += 1
            
            max_freq = -1
            candidate = -1
            for num, cnt in freq.items():
                if cnt >= threshold:
                    if cnt > max_freq:
                        max_freq = cnt
                        candidate = num
                    elif cnt == max_freq:
                        if num < candidate:
                            candidate = num
            ans.append(candidate)
        
        return ans




re =Solution().subarrayMajority(nums = [1,1,2,2,1,1], queries = [[0,5,4],[0,3,3],[2,3,2]])
print(re)