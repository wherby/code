# https://leetcode.cn/problems/count-the-number-of-beautiful-subarrays/?envType=daily-question&envId=2025-03-06

from typing import List, Tuple, Optional
from collections import defaultdict,deque
class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        ret = 0
        dic = defaultdict(int)
        dic[0] =1
        acc = 0 
        for a in nums:
            acc = acc^a 
            ret += dic[acc]
            dic[acc] +=1
        return ret