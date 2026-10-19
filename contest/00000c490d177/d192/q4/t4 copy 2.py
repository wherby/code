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
    def longestSubarray(self, nums: list[int], k: int) -> int:
        lst =[-1]*k 
        fst = [-2]*k 
        lls = [[] for _ in range(k)]
        cur = [0]*k
        acc = 0
        for i,a in enumerate(nums):
            a = a % k 
            acc = (acc+a)%k 
            lst[acc] = i 
            lls[a].append(i)
        acc = 0
        ans = 0
        for i,a in enumerate(nums):
            a = a %k
            if fst[acc] ==-2:
                fst[acc] = i-1
                ans = max(ans, lst[acc] - i+1 )
                for j,b in enumerate(lst):
                    if b>=i and b-i+1 > ans:
                        for i1 in range(3):
                            d = i1*k +j
                            if d >=acc and  (d-acc)%2 ==0  and (d-acc)//2 <k :
                                c = (d-acc)//2
                                while cur[c] < len(lls[c]) and lls[c][cur[c]]< i:
                                    cur[c] +=1
                                if cur[c] < len(lls[c]) and lls[c][cur[c]]<=b:
                                    ans = max(ans,b-i+1)
            
            acc =(acc+a)%k 
        return ans



re =Solution().longestSubarray([13,14,-7],8)
print(re)