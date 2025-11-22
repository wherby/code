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
from itertools import pairwise
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n= len(nums)
        ls = [-1]
        for i in range(n):
            if i >0 and nums[i]< nums[i-1]:
                ls.append(i-1)
        ls.append(n-1)
        pls = [0]
        for a,b in pairwise(ls):
            pls.append(pls[-1] + (b-a) *(b-a+1)//2)
        ret = []
        for l, r in queries:
            k_s = bisect_left(ls, l) - 1
            k_e = bisect_left(ls, r) - 1
            cnt = pls[k_e] - pls[k_s]
            if k_s < k_e and ls[k_s] < l:
                s = ls[k_s] + 1
                e = ls[k_s+1]
                le = l - s 
                
                if le > 0:
                    term1 = e - s + 1        
                    term_last = e - (l - 1) + 1  
                    excluded_sum = (term1 + term_last) * le // 2
                    cnt -= excluded_sum
            
            if k_e + 1 < len(ls): 
                s_prime = ls[k_e] + 1
                
                if s_prime <= r: 
                    start_final = max(l, s_prime)
                    end_final = r

                    length_final = end_final - start_final + 1

                    if length_final > 0:
                        cnt += length_final * (length_final + 1) // 2
            ret.append(cnt)
        return ret





re =Solution().countStableSubarrays(nums = [3,1,2], queries = [[0,1],[1,2],[0,2]])
print(re)