from typing import List, Tuple, Optional

from collections import defaultdict,deque
from functools import cache
import heapq
from heapq import heappop,heappush 
from sortedcontainers import SortedDict,SortedList
from collections import Counter

## https://leetcode.cn/circle/discuss/ZzhMI6/

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        c = Counter()
        cur = 0
        for a in nums:
            cur += (a%modulo ==k)
            cur = cur %modulo
            c[cur] +=1
        ans = 0
        cur = 0
        for a in nums:
            rightF= (cur+k)%modulo
            ans += c[rightF]
            
            cur += (a%modulo ==k)
            cur = cur %modulo
            
            c[cur] -=1
        
        return ans





re =Solution().countInterestingSubarrays(nums = [3,1,9,6], modulo = 3, k = 0)
print(re)