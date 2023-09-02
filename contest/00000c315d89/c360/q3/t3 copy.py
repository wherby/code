from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from collections import Counter
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        c = Counter(nums)
        cnt = 0 
        acc = 0
        for i in range(40):
            acc += c[1<<i] *(1<<i)
            if target&(1<<i):
                #print(i,acc)
                if acc < (1<<i):
                    j = i+1
                    while j <40:
                        if c[1<<j]>0:
                            cnt += j-i
                            c[1<<j] -=1
                            acc +=(1<<j) - (1<<i)
                            #print(cnt,j,i,acc)
                            break
                        j +=1
                else:
                    acc -=(1<<i)
        return cnt
            




re =Solution().minOperations(nums = [16,16,4], target = 3)
print(re)