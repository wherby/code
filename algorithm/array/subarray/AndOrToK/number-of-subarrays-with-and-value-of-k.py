#  https://leetcode.cn/contest/biweekly-contest-134/problems/number-of-subarrays-with-and-value-of-k/description/

from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pre  = defaultdict(int)
        sm = 0
        
        for a in nums:
            cur = defaultdict(int)
            for key,v in pre.items():
                cur[key&a] +=v
            cur[a]+=1
            sm += cur[k]
            pre = cur
        return sm